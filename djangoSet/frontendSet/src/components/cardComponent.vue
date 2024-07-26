<template>
  <div
    class="flex flex-col rounded-lg border px-40 py-20 space-y-2 bg-slate-200 max-w-7xl"
  >
    <div class="space-y-16">
      <div class="ml-4">
        <div v-if="header" class="flex text-xl font-semibold">
          <div>{{ header }}</div>
        </div>
        <slot name="default"></slot>
        <slot name="footer-slot"></slot>
      </div>
      <div class="flex flex-row mr-2">
        <div class="flex-1"></div>
        <div class="flex items-center space-x-24 mr-8 pb-2">
          <p>5</p>
          <p>4</p>
          <p>3</p>
          <p>2</p>
          <p>1</p>
        </div>
      </div>
    </div>

    <div class="space-y-2 items-center">
      <questioncomponent
        body="Articulates course policies, procedures and gnfdngkdj hdsfjkhsdfjkhsdfjkhsdf
      hajskdads asdasdad sdhasjkdhsajkd asdkasdkjlahsdjkashd adasda sd jashdajksdhasjkd?"
      />
      <questioncomponent
        body="2Articulates course policies, procedures and gnfdngkdj"
      />
      <questioncomponent body="Question 2" />
      <questioncomponent body="Question 2" />
      <questioncomponent body="Question 2" />
    </div>
  </div>
</template>

<script>
import questioncomponent from "./questionComponent.vue";
export default {
  name: "CardComponent",
  components: {
    questioncomponent,
  },
  props: {
    header: String,
  },
  computed: {
    computedClassesMain() {
      const styleClasses = {
        white: "bg-white",
        "yellow-50": "bg-yellow-50",
      };

      const sizeClasses = {
        lg: "max-w-lg",
        "3xl": "max-w-3xl",
      };

      return [
        styleClasses[this.type] || styleClasses["white"],
        sizeClasses[this.size],
      ];
    },
  },
};
</script>

<style scoped>
.header-container {
  padding-top: 1rem; /* Add top padding */
  padding-left: 1rem; /* Add left padding */
}

/* Position the number container in the upper-right corner of the card */
.number-container {
  position: absolute;
  top: 1rem; /* Adjust top spacing as needed */
  right: 1rem; /* Adjust right spacing as needed */
}
</style>
