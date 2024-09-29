<template>
  <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>

  <section class="max-w-full">
    <section
      class="relative bg-white min-h-screen pt-20 overflow-y-auto font-raleway pb-40 pl-40 pr-8"
    >
      <div
        class="relative bg-darks-50 rounded-3xl w-full pt-12 pb-28 space-y-8 p-12 border border-black/10"
      >
        <div class="flex flex-col space-y-3 text-darks-700">
          <div class="flex flex-row text-4xl space-x-2">
            <h1>You are currently evaluating</h1>
            <h1 class="font-bold text-plpgreen-400">Riegie Tan</h1>
          </div>
          <p class="text-sm font-normal text-darks-200/80">
            Want to evaluate a different instructor? Select a course from the
            dropdown menu and the corresponding professor will be displayed
            automatically.
          </p>
        </div>

        <form action="">
          <div class="space-y-4">
            <div class="flex flex-col items-center space-y-12">
              <CardFeedback>
                  <TextAreaComponent
                      v-for="question in questions"
                      :key = "question.feedback_question_id"
                      :id="question.feedback_question_id"
                      :label = "question.feedback_question_id + '. ' + question.question"
                  />
              </CardFeedback>
            </div>
            <div>
              <router-link to = "/SETNumericalRating">
                <button
              type="button"
              class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-darks-50 focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
            >
              Back
            </button>
              </router-link>
           
            <button
              type="button"
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

<script>
import axios from 'axios';
import CardFeedback from "@/components/cardFeedback.vue";
import TextAreaComponent from "@/components/textareaComponent.vue"; 

export default {
  components: {
    TextAreaComponent,
    CardFeedback,
  },

  data() {
    return {
     questions: [], 
    };
  },

  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/feedback-questions/");
      this.questions = response.data;
      console.log("Questions:", this.questions); 
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  }
};
</script>

<style scoped>
.w-collapsed-sidebar {
  width: 102px;
}
</style>
