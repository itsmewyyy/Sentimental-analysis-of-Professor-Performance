<template>

  <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>

  <section
    class="relative bg-white min-h-screen pt-16 overflow-y-auto font-raleway pb-40 pl-36 pr-4"
  >
    <div
      class="relative bg-darks-50 rounded-2xl w-full pt-12 pb-28 space-y-12 p-12 border border-black/10"
    >
      <div class="flex flex-col space-y-4 text-darks-800">
        <h1 class="text-4xl font-bold max-w-4xl">
          Welcome to Pamantasan ng Lungsod ng Pasig Student Evaluation of
          Teaching
        </h1>
        <div class="flex flex-row text-xl space-x-1">
          <p>You are currently evaluating</p>
          <p class="font-semibold">Riegie D. Tan, DIT</p>
        </div>
      </div>

      <div class="space-y-4">
        <div class="flex flex-col items-center space-y-8">
          <CardFeedback>
            <template #content>
              <TextAreaComponent
                id="feedback"
                label="1. How do you feel under his/her class?"
                placeholder="Write your feedback here..."
                rows="default"
                cols="default"
                size="md"
                color="blue-50"
              />

              <TextAreaComponent
                id="feedback"
                label="2. huwasap"
                placeholder="Write your feedback here..."
                rows="default"
                cols="60"
                size="md"
                color="blue-50"
              />

              <TextAreaComponent
                id="feedback"
                label="Feedback"
                placeholder="Write your feedback here..."
                rows="default"
                cols="60"
                size="md"
                color="blue-50"
              />

              <TextAreaComponent
                id="feedback"
                label="Feedback"
                placeholder="Write your feedback here..."
                rows="default"
                cols="60"
                size="md"
                color="blue-50"
              />
              <TextAreaComponent
                id="feedback"
                label="Feedback"
                placeholder="Write your feedback here..."
                rows="default"
                cols="60"
                size="md"
                color="blue-50"
              />
            </template>
          </CardFeedback>
        </div>

        <div>
          <button
            type="button"
            class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-darks-50 focus:ring-4 focus:ring-gray-100 font-semibold rounded-lg text-sm px-12 py-2.5 me-2 mb-2"
          >
            Back
          </button>
          <button
            type="button"
            class="text-white bg-plpgreen-200 hover:bg-plpgreen-400 focus:ring-4 focus:ring-gray-100 font-semibold rounded-lg text-sm px-12 py-2.5 me-2 mb-2"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import CardFeedback from "./components/cardFeedback.vue";
import TextAreaComponent from "./components/textareaComponent.vue"; // Adjusted path

export default {
  components: {
    TextAreaComponent,
    CardFeedback,
  },
};
</script>


<style scoped>

.w-collapsed-sidebar {
  width: 102px;
}
</style>
