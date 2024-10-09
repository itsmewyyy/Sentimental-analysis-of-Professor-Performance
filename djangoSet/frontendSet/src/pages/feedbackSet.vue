<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import CardFeedback from "@/components/cardFeedback.vue";
import TextAreaComponent from "@/components/textareaComponent.vue";
import sidebarStudent from "@/components/sidebarStudent.vue";
import navbar from "@/components/navbar.vue";
import { useRatingsStore } from "@/store/ratingStore";
import { useRouter } from "vue-router";

const questions = ref<any[]>([]);
const router = useRouter();
const ratingsStore = useRatingsStore();

// Fetch questions from API
async function fetchData() {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/feedback-questions/"
    );
    questions.value = response.data;
    console.log("Questions:", questions.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

// Store feedback ratings in the store
function handleFeedback(questionId, feedback) {
  ratingsStore.setFeedbackRating(questionId, feedback); // Store feedback
}

// Submit both numerical ratings and feedback
async function submitAll() {
  const data = {
    numericalRatings: ratingsStore.numericalRatings,
    feedbackRatings: ratingsStore.feedbackRatings,
    student_enrolled_subj_id: "21-00270-24-25-1-CS02", // Use the student_subj_id from the store or from session whatever
  };

  console.log("Data being submitted:", data);

  try {
    await axios.post("http://127.0.0.1:8000/api/submit-ratings/", data);
    alert("Ratings submitted successfully!");
    ratingsStore.clearAllRatings(); // Clear the store after submission
    router.push("/"); // Redirect to a success page
  } catch (error) {
    console.error("Error submitting ratings:", error);
  }
}

onMounted(fetchData);

// Sidebar and Navbar
const isSidebarOpen = ref(false);
function toggleSidebar() {
  isSidebarOpen.value = !isSidebarOpen.value;
}
</script>

<template>
  <navbar :toggleSidebar="toggleSidebar" />
  <sidebarStudent :isSidebarOpen="isSidebarOpen" />

  <section
    class="transition-all duration-500"
    :class="{
      'ml-72': isSidebarOpen,
      'ml-20': !isSidebarOpen,
    }"
  >
    <section
      class="relative bg-white min-h-screen pt-20 overflow-y-auto font-raleway pb-16 pl-16 pr-12"
    >
      <div
        class="relative bg-white rounded-3xl w-full pt-12 pb-28 space-y-8 p-12 border border-black/15"
      >
        <div class="flex flex-col space-y-0">
          <h1 class="text-4xl font-bold text-darks-700">Noreen Perez</h1>
          <p class="text-base font-thin text-darks-200">
            College of Computer Studies
          </p>
        </div>

        <form @submit.prevent="submitAll">
          <!-- Prevent default form submission -->
          <div class="space-y-4">
            <div class="flex flex-col items-center space-y-12">
              <CardFeedback>
                <TextAreaComponent
                  v-for="question in questions"
                  :key="question.feedback_question_id"
                  :id="question.feedback_question_id + '.'"
                  :label="
                    question.feedback_question_id + '. ' + question.question
                  "
                  @input="
                    (value) =>
                      handleFeedback(question.feedback_question_id, value)
                  "
                />
              </CardFeedback>
            </div>
            <div>
              <router-link to="/SETNumericalRating">
                <button
                  type="button"
                  class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-darks-50 focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
                >
                  Back
                </button>
              </router-link>

              <button
                type="submit"
                class="text-white bg-plpgreen-200 hover:bg-plpgreen-400 focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
              >
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>
    </section>
  </section>
</template>
