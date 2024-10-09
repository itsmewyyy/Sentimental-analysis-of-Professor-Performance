<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { useRatingsStore } from "@/store/ratingStore";
import cardComponent from "@/components/cardNumerical.vue";
import questioncomponent from "@/components/questionComponent.vue";
import navbar from "@/components/navbar.vue";
import sidebarStudent from "@/components/sidebarStudent.vue";

const categories = ref<any[]>([]);
const router = useRouter();

// Fetch questions
async function fetchData() {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/categories-and-questions/"
    );
    categories.value = response.data;
    console.log("Categories:", categories.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

onMounted(fetchData);

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

// Navigate to the feedback page
function goToFeedback() {
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
    router.push("/SETFeedback"); // Navigate to the feedback page
  } else {
    alert("Please rate all the questions before proceeding.");
  }
}

//Sidebar
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
        class="relative bg-white rounded-3xl w-full pt-12 pb-28 space-y-8 p-20 border border-black/15"
      >
        <div class="flex flex-col space-y-0">
          <h1 class="text-4xl font-bold text-darks-700">Noreen Perez</h1>
          <p class="text-base font-thin text-darks-200">
            College of Computer Studies
          </p>
        </div>

        <form @submit.prevent="goToFeedback">
          <div class="space-y-4">
            <div
              v-for="(category, index) in categories"
              :key="index"
              class="flex flex-col items-center space-y-8"
            >
              <cardComponent
                :header="category.category_id + ' ' + category.category_desc"
                :categoryId="category.category_id"
              >
                <questioncomponent
                  v-for="question in category.questions"
                  :key="question.numerical_question_id"
                  :body="question.question"
                  @rating-selected="handleRatingSelection"
                  :id="question.numerical_question_id"
                />
              </cardComponent>
            </div>

            <button
              type="submit"
              class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-plpgreen-400 hover:text-white focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
            >
              Next
            </button>
          </div>
        </form>
      </div>
    </section>
  </section>
</template>
