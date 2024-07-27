<template>
  <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>

  <section class="max-w-full">
    <section
      class="relative bg-white min-h-screen pt-16 overflow-y-auto font-raleway pb-40 pl-36 pr-4"
    >
      <div
        class="relative bg-darks-50 rounded-2xl w-full pt-12 pb-28 space-y-4 p-12 border border-black/10"
      >
        <div class="flex flex-col space-y-20 text-darks-800">
          <h1 class="text-4xl font-bold max-w-4xl">
            Welcome to Pamantasan ng Lungsod ng Pasig Student Evaluation of
            Teaching
          </h1>
          <div class="flex flex-row text-xl space-x-1">
            <p>You are currently evaluating</p>
            <p class="font-bold">Riegie D. Tan, DIT</p>
          </div>
        </div>

        <div class="space-y-4">
          <div class="flex flex-col items-center space-y-8">
            <cardComponent
              header="B. The use of social media platforms (Ex. Facebook, Google Classroom, and etc.) "
            >
              <template #content>
                <questioncomponent body="Qasdasmndasm,dnasjkd" />
                <questioncomponent body="Question 2" />
              </template>
            </cardComponent>
          </div>

          <button
            type="button"
            class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-plpgreen-400 hover:text-white focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
          >
            Next
          </button>
        </div>
      </div>
    </section>
  </section>
</template>

<script>
import cardComponent from "./components/cardNumerical.vue";
import CardFeedback from "./components/cardFeedback.vue";
import questioncomponent from "./components/questionComponent.vue";

export default {
  components: {
    cardComponent,
    questioncomponent,
  },
};
</script>

<style scoped>
.w-collapsed-sidebar {
  width: 102px;
}
</style>
