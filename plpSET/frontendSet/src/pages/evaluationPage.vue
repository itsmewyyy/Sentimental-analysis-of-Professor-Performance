<script setup lang="ts">
import { ref, onMounted, computed, watch } from "vue";
import TextAreaComponent from "@/components/SET/textareaComponent.vue";
import navbar from "@/components/navigation/NavBarStudent.vue";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";
import cardComponent from "@/components/SET/cardNumerical.vue";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import questioncomponent from "@/components/SET/questionComponent.vue";
// @ts-ignore
import type { CarouselApi } from "@/components/ui/carousel";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { useRouter } from "vue-router";
import { useRatingsStore } from "@/store/ratingStore";
import axios from "axios";
import { useAuthStore } from "@/store/student";
const authStore = useAuthStore();
authStore.restoreSession();

// Define interfaces
interface ProfessorInfo {
  surname: string;
  first_name: string;
  department_desc: string;
}

interface SubjectName {
  subject_code: string;
  subject_desc: string;
}

interface Subject {
  student_enrolled_subj_id: string;
  prof_info: ProfessorInfo;
  subj_name: SubjectName;
  is_evaluated: boolean;
}

interface EnrolledSubject {
  student_id: string;
  section: string;
  subjects: Subject[];
}

//
const router = useRouter();
const ratingsStore = useRatingsStore();
const { toast } = useToast();
const enrolledSubjects = ref<EnrolledSubject[]>([]);
const selectedSubject = ref<Subject | null>(null);
const categories = ref<any[]>([]);
const questions = ref<any[]>([]);

//Define for counts
const totalCategoryCount = ref(0);
const totalFeedbackQuestionCount = ref(0);
const currentCategory = ref(0);
const currentFeedback = ref(0);
const feedbackApi = ref<CarouselApi>();
const categoryApi = ref<CarouselApi>();

//Declare for Feedback Question Count
function setFeedbackApi(val: CarouselApi) {
  feedbackApi.value = val;
}

watch(feedbackApi, (api) => {
  if (!api) return;

  currentCategory.value = 1; // Reset to the first category

  api.scrollTo(0); // Scroll to the first item in the carousel

  currentFeedback.value = api.selectedScrollSnap() + 1;

  api.on("select", () => {
    currentFeedback.value = api.selectedScrollSnap() + 1;
  });
});

//Declare for Category Count
function setCategoryApi(val: CarouselApi) {
  categoryApi.value = val;
}

watch(categoryApi, (api) => {
  if (!api) return;

  currentCategory.value = 1; // Reset to the first category

  api.scrollTo(0); // Scroll to the first item in the carousel

  currentCategory.value = api.selectedScrollSnap() + 1;

  api.on("select", () => {
    currentCategory.value = api.selectedScrollSnap() + 1;
  });
});

//mount data

onMounted(() => {
  fetchSubjects();
  fetchData();
  fetchFeedbackData();
});

// Fetch professor and department info
const fetchSubjects = async () => {
  try {
    const student_id = localStorage.getItem("student_id"); // Fetch student ID from localStorage
    const response = await axios.get<Subject[]>(
      `https://sentiment-professor-feedback-1.onrender.com/api/enrolled_subjs/${student_id}`
    );

    enrolledSubjects.value = [
      { student_id, section: "", subjects: response.data },
    ];

    // Retrieve selected subject based on student_enrolled_subj_id from localStorage
    const student_enrolled_subj_id = localStorage.getItem(
      "student_enrolled_subj_id"
    );
    selectedSubject.value =
      enrolledSubjects.value[0].subjects.find(
        (subject) =>
          subject.student_enrolled_subj_id === student_enrolled_subj_id
      ) || null;

    console.log("API response:", response.data);
  } catch (error) {
    console.error("Error fetching subjects:", error);
  }
};

const professorInfo = computed(() => {
  return selectedSubject.value ? selectedSubject.value.prof_info : null;
});

const departmentDesc = computed(() => {
  return selectedSubject.value
    ? selectedSubject.value.prof_info.department_desc
    : "";
});

// Fetch categories and questions
async function fetchData() {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/categories-and-questions/"
    );
    categories.value = response.data;
    totalCategoryCount.value = categories.value.length;
    console.log("Categories:", categories.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

// Watch for changes in localStorage and fetch subjects accordingly
watch(
  () => localStorage.getItem("student_enrolled_subj_id"),
  (newId) => {
    if (newId) {
      fetchSubjects();
    }
  }
);

// Handle rating selection from question components
function handleRatingSelection({
  questionId,
  rating,
}: {
  questionId: string;
  rating: number | null;
}) {
  const ratingsStore = useRatingsStore();
  // Update the rating in the store using the question ID as the key
  ratingsStore.setNumericalRating(questionId, rating);
}

// Fetch questions from API
async function fetchFeedbackData() {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/feedback-questions/"
    );
    questions.value = response.data;
    totalFeedbackQuestionCount.value = questions.value.length;
    console.log("Questions:", questions.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

// Store feedback ratings in the store
function handleFeedback(questionId, feedback) {
  if (ratingsStore.feedbackRatings[questionId] !== feedback) {
    ratingsStore.setFeedbackRating(questionId, feedback);
  }
}
// Submit both numerical ratings and feedback
async function submitAll() {
  // Get the student_enrolled_subj_id from the localstorage
  const student_enrolled_subj_id = localStorage.getItem(
    "student_enrolled_subj_id"
  );

  if (!student_enrolled_subj_id) {
    console.error("No enrolled subject ID found.");
    return;
  }

  ratingsStore.setStudentEnrolledSubjId(student_enrolled_subj_id);

  const allFeedbackAnswered = questions.value.every((question) => {
    return ratingsStore.feedbackRatings.hasOwnProperty(
      question.feedback_question_id
    );
  });

  if (!allFeedbackAnswered) {
    alert("Please answer all feedback questions before submitting.");
    return;
  }

  // Prepare the data for submission
  const data = {
    numericalRatings: ratingsStore.numericalRatings,
    feedbackRatings: ratingsStore.feedbackRatings,
    student_enrolled_subj_id: ratingsStore.studentEnrolledSubjId, // Use the studentEnrolledSubjId from the store
  };

  console.log("Data being submitted:", data);

  try {
    await axios.post(
      "https://sentiment-professor-feedback-1.onrender.com/api/submit-ratings/",
      data
    );
    localStorage.removeItem("student_enrolled_subj_id"); // Remove item
    ratingsStore.clearAllRatings(); // Clear the store after submission

    // Show toast notification
    toast({
      title: "Submission Successful",
      description: "Your feedback has been submitted successfully!",
    });

    router.push("/StudentDashboard"); // Redirect to student dashboard
  } catch (error) {
    console.error("Error submitting ratings:", error);
  }
}

// Step tracking
const currentStep = ref(1);
const isNext = ref(true);

// Move to feedback
function goToNext() {
  const ratingsStore = useRatingsStore();

  // Check if all questions have been rated
  const allRated = categories.value.every((category) =>
    category.questions.every((question) =>
      ratingsStore.numericalRatings.hasOwnProperty(
        question.numerical_question_id
      )
    )
  );

  if (allRated) {
    isNext.value = true;
    currentStep.value++;
  } else {
    alert("Please rate all the questions before proceeding.");
  }
}

// Move to previous form
function goToPrev() {
  isNext.value = false;
  currentStep.value--;
}
</script>

<template>
  <Toaster />
  <navbar />
  <section class="pt-32 pl-32 pr-32 pb-auto">
    <form>
      <div class="sliding-container w-full space-y-2">
        <transition :name="isNext ? 'slide-next' : 'slide-prev'" mode="out-in">
          <div :key="currentStep" class="sliding-content">
            <!-- Numerical -->
            <div
              v-if="currentStep === 1"
              class="slide w-11/12 bg-white border border-black/15 h-5/6 pb-6 pt-8 px-16 rounded-lg"
            >
              <div class="flex flex-wrap space-y-8">
                <div class="flex space-x-4 items-center">
                  <Avatar class="w-20 h-20">
                    <AvatarImage
                      src="https://i.pinimg.com/564x/92/73/47/927347b099b1f06d5b1b49ba31b27de9.jpg"
                    />
                    <AvatarFallback>OM</AvatarFallback>
                  </Avatar>
                  <div class="flex flex-col">
                    <!-- Dynamic professor name and department -->
                    <h1 class="text-4xl font-bold text-darks-500">
                      {{
                        professorInfo
                          ? professorInfo.first_name +
                            " " +
                            professorInfo.surname
                          : "Loading..."
                      }}
                    </h1>
                    <p class="text-base text-darks-200/80">
                      {{ departmentDesc }}
                    </p>
                  </div>
                </div>
                <div class="w-full justify-center space-y-6">
                  <Carousel
                    class="w-full bg-plpgreen-100/40 rounded-lg pt-9 pb-6"
                    @init-api="setCategoryApi"
                  >
                    <CarouselContent>
                      <!-- Iterate through categories to create CarouselItems -->
                      <CarouselItem
                        v-for="(category, index) in categories"
                        :key="index"
                      >
                        <cardComponent
                          :header="
                            category.category_id + ' ' + category.category_desc
                          "
                          :categoryId="category.category_id"
                        >
                          <!-- Iterate through questions for each category -->

                          <questioncomponent
                            v-for="question in category.questions"
                            :key="question.numerical_question_id"
                            :body="question.question"
                            @rating-selected="handleRatingSelection"
                            :id="question.numerical_question_id"
                          />
                        </cardComponent>
                      </CarouselItem>
                    </CarouselContent>
                    <CarouselPrevious @click.prevent />
                    <CarouselNext @click.prevent />
                  </Carousel>
                  <div class="text-center text-sm text-darks-100">
                    Category {{ currentCategory }} of {{ totalCategoryCount }}
                  </div>
                </div>
              </div>
            </div>

            <!-- Feedback -->
            <div
              v-if="currentStep === 2"
              class="slide w-11/12 bg-white border border-black/15 h-5/6 pb-6 pt-8 px-16 rounded-lg"
            >
              <div class="flex flex-wrap space-y-8">
                <div class="flex space-x-4 items-center">
                  <Avatar class="w-20 h-20">
                    <AvatarImage
                      src="https://i.pinimg.com/564x/92/73/47/927347b099b1f06d5b1b49ba31b27de9.jpg"
                    />
                    <AvatarFallback>OM</AvatarFallback>
                  </Avatar>
                  <div class="flex flex-col">
                    <!-- Dynamic professor name and department -->
                    <h1 class="text-4xl font-bold text-darks-700">
                      {{
                        professorInfo
                          ? professorInfo.first_name +
                            " " +
                            professorInfo.surname
                          : "Loading..."
                      }}
                    </h1>
                    <p class="text-base text-darks-800">
                      {{ departmentDesc }}
                    </p>
                  </div>
                </div>
                <div class="w-full justify-center space-y-6">
                  <Carousel
                    class="w-full h-64 bg-plpgreen-100/40 rounded-lg p-12"
                    @init-api="setFeedbackApi"
                  >
                    <CarouselContent>
                      <CarouselItem
                        v-for="question in questions"
                        :key="question.feedback_question_id"
                      >
                        <TextAreaComponent
                          :id="String(question.feedback_question_id)"
                          :label="
                            question.feedback_question_id +
                            '. ' +
                            question.question
                          "
                          @input="
                            (value) =>
                              handleFeedback(
                                question.feedback_question_id,
                                value
                              )
                          "
                        />
                      </CarouselItem>
                    </CarouselContent>
                    <CarouselPrevious @click.prevent />
                    <CarouselNext @click.prevent />
                  </Carousel>
                  <div class="text-center text-sm text-darks-100">
                    Question {{ currentFeedback }} of
                    {{ totalFeedbackQuestionCount }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>

        <div>
          <div>
            <!--Buttons for navigation and submission-->
            <button
              v-if="currentStep === 2"
              @click.prevent="goToPrev"
              class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-plpgreen-400 hover:text-white focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
            >
              Back
            </button>
            <button
              @click.prevent="submitAll"
              v-if="currentStep === 2"
              type="submit"
              class="text-white bg-plpgreen-200 hover:bg-plpgreen-400 focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
            >
              Submit
            </button>
          </div>
          <button
            v-if="currentStep === 1"
            @click.prevent="goToNext"
            class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-plpgreen-400 hover:text-white focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
          >
            Next
          </button>
        </div>
      </div>
    </form>
  </section>
</template>

<style scoped>
.sliding-container {
  position: relative;
  overflow: hidden;
  height: auto;
}

.sliding-content {
  display: flex;
  transition: transform 800ms ease-in-out;
  width: 200%;
}

.slide {
  width: 50%;
  flex-shrink: 0;
}

.slide-next-enter-active,
.slide-prev-leave-active {
  transition: transform 800ms ease-in-out;
}

.slide-next-enter {
  transform: translateX(100%);
}
.slide-next-leave-to {
  transform: translateX(-100%);
}

/* Slide for Previous */
.slide-prev-enter-active,
.slide-next-leave-active {
  transition: transform 800ms ease-in-out;
}

.slide-prev-enter {
  transform: translateX(-100%);
}
.slide-prev-leave-to {
  transform: translateX(100%);
}
</style>
