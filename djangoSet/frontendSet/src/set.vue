<template>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" />
  <link
    href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap"
    rel="stylesheet"
  />

  <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar bg-black h-screen"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>
  <section class="bg-white max-w-full max-h-screen p-16 pt-20 overflow-scroll">
    <div
      class="bg-gray-100 round-16 max-w-screen-2xl ml-32 max-h-max flex flex-col items-center pt-16 pb-40 space-y-12"
    >
      <div class="flex flex-col">
        <h1>
          Welcome to Pamantasan ng Lungsod ng Pasig Student Evaluation on
          Teaching
        </h1>
        <div class="flex flex-row">
          <p>You are currently evaluating</p>
          <p>Riegie D. Tan, DIT</p>
        </div>
      </div>

      <div class="flex flex-col space-y-4">
        <cardComponent header="A. Teacher "></cardComponent>
        <cardComponent header="A. ewan ko "></cardComponent>
      </div>
    </div>
  </section>
</template>

<script>
import cardComponent from "./components/cardComponent.vue";
import CardFeedback from "./components/cardFeedback.vue";
import questionComponent from "./components/questionComponent.vue";
import { onMounted } from "vue";

export default {
  name: "ParentComponent",
  components: {
    cardComponent,
    questionComponent,
  },
};
</script>

<style scoped>
.round-16 {
  border-radius: 16px;
}
.w-collapsed-sidebar {
  width: 102px;
  background-color: #f8f8f8;
}
</style>
