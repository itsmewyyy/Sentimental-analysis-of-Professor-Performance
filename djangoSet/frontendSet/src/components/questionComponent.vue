<template>
  <div
    class="rounded-lg flex flex-row items-center question-container bg-white p-8 min-w-full"
  >
    <div class="flex-1">
      <span v-if="body" class="mb-3 font-medium text-darks-800 block">{{
        body
      }}</span>
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
    body: String,
  },
};
</script>

<style scoped>
.radio-large {
  width: 22px;
  height: 22px;
  accent-color: #5f965e;
}
</style>
