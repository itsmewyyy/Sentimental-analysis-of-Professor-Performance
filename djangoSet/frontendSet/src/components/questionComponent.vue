<template>
  <div
    class="rounded-lg flex flex-row items-center question-container bg-white px-4 py-8 max-w-full"
  >
    <div class="flex-1">
      <slot name="ts"></slot>
      <div
        v-if="header"
        class="flex mb-2 text-xl font-semibold tracking-tight justify-between items-center"
      >
        <div>{{ header }}</div>
        <slot name="hs" class="max-h-8"></slot>
      </div>
      <span v-if="body" class="mb-3 font-normal block">{{ body }}</span>
      <slot name="bs"></slot>
    </div>
    <div class="flex items-center space-x-20 p-4">
      <input type="radio" :value="1" v-model="selected" class="radio-large" />
      <input type="radio" :value="2" v-model="selected" class="radio-large" />
      <input type="radio" :value="3" v-model="selected" class="radio-large" />
      <input type="radio" :value="4" v-model="selected" class="radio-large" />
      <input type="radio" :value="5" v-model="selected" class="radio-large" />
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionComponent",
  data() {
    return {
      selected: null,
    };
  },
  props: {
    header: String,
    body: String,
  },
};
</script>

<style scoped>
.radio-large {
  width: 22px; /* Adjusted width */
  height: 22px; /* Adjusted height */
  accent-color: #5f965e; /* Optional: matches the color to your design */
}
</style>
