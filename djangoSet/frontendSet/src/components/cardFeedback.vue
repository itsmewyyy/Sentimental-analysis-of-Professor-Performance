<template>
  <div :class="['relative rounded-lg shadow', computedClassesMain]">
    <div class="p-4">
      <div
        v-if="header"
        class="header-container flex mb-2 text-xl font-semibold tracking-tight justify-between items-center"
      >
        <div>{{ header }}</div>
      </div>
      <slot name="default"></slot>
      <slot name="footer-slot"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardFeedback",
  props: {
    header: String,
    size: {
      type: String,
      validator: function (value) {
        return ["lg", "3xl"].includes(value);
      },
      default: "lg",
    },
    type: {
      type: String,
      validator: function (value) {
        return ["white", "yellow-50"].includes(value);
      },
      default: "white",
    },
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
  padding-top: 1rem;
  padding-left: 1rem;
}
</style>
