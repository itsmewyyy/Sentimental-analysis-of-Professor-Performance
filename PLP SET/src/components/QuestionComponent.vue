<template>
  <div :class="['rounded-lg shadow', computedClassesMain, 'flex', 'question-container']">
    <div class="p-4 flex-1">
      <slot name="ts"></slot>
      <div v-if="header" class="flex mb-2 text-xl font-semibold tracking-tight justify-between items-center">
        <div>{{ header }}</div>
        <slot name="hs" class="max-h-8"></slot>
      </div>
      <span v-if="body" class="mb-3 font-normal block">{{ body }}</span>
      <slot name="bs"></slot>
    </div>
    <div class="flex items-center space-x-6 p-4"> 
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
  name: 'QuestionComponent',
  data() {
    return {
      selected: null,
    };
  },
  props: {
    header: String,
    body: String,
    size: {
      type: String,
      validator: function (value) {
        return ['lg', '3xl'].includes(value);
      },
      default: 'lg',
    },
    type: {
      type: String,
      validator: function (value) {
        return ['white', 'yellow-50'].includes(value);
      },
      default: 'white',
    },
  },
  computed: {
    computedClassesMain() {
      const styleClasses = {
        white: 'bg-white',
        'yellow-50': 'bg-yellow-50'
      };

      const sizeClasses = {
        lg: 'max-w-lg',
        '3xl': 'max-w-3xl',
      };

      return [styleClasses[this.type] || styleClasses['white'], sizeClasses[this.size]];
    },
  },
};
</script>

<style scoped>
.radio-large {
  width: 16px; /* Adjusted width */
  height: 16px; /* Adjusted height */
  accent-color: currentColor; /* Optional: matches the color to your design */
  margin-right: 6px; /* Adjusted space between radio buttons */
}

.question-container {
  padding: 1rem; /* Reduced padding inside the QuestionComponent */
  margin: 0.75rem; /* Reduced margin outside the QuestionComponent */
}
</style>
