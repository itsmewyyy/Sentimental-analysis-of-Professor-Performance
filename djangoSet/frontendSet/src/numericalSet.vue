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
        class="relative bg-darks-50 rounded-3xl w-full pt-12 pb-28 space-y-8 p-20 border border-black/10"
      >
        <div class="flex flex-col space-y-3 text-darks-700">
          <div class="flex flex-row text-4xl space-x-2">
            <h1>You are currently evaluating</h1>
            <h1 class="font-bold text-plpgreen-400">Riegie D. Tan, DIT</h1>
          </div>
          <p class="text-sm font-thin text-darks-800">
            Want to evaluate a different instructor? Select a course from the dropdown menu to display the corresponding professor.
          </p>
        </div>


        <form action="">
          <div class="space-y-4">
          <div class="flex flex-col items-center space-y-8">
            <cardComponent
              header="B. The use of social media platforms (Ex. Facebook, Google Classroom, and etc.) "
            >
              <template #content>
                <questioncomponent body="Artculates course policies blablabalab and babla balab?" />
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
        </form>
      
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
