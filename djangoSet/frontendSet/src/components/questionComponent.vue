<template>
  <div
    class="rounded-lg flex flex-row items-center content-center bg-white p-4 min-w-full"
  >
    <div class="pt-4 flex-1 pl-2 question">
      <span v-if="body" class="mb-3 font-medium text-darks-800 block">{{
        body
      }}</span>
      <span v-else class="mb-3 font-medium text-darks-800 block"
        >No question available</span
      >
    </div>

    <div class="flex items-center space-x-20 p-4 p-4">
      <input
        type="radio"
        :value="5"
        v-model="selected"
        class="radio-large text-plpgreen-400 focus:ring-plpgreen-200"
        @change="emitRating"
      />
      <input
        type="radio"
        :value="4"
        v-model="selected"
        class="radio-large text-plpgreen-200 focus:ring-plpgreen-200"
        @change="emitRating"
      />
      <input
        type="radio"
        :value="3"
        v-model="selected"
        class="radio-large text-plpgreen-200 focus:ring-plpgreen-200"
        @change="emitRating"
      />
      <input
        type="radio"
        :value="2"
        v-model="selected"
        class="radio-large text-plpgreen-200 focus:ring-plpgreen-200"
        @change="emitRating"
      />
      <input
        type="radio"
        :value="1"
        v-model="selected"
        class="radio-large text-plpgreen-200 focus:ring-plpgreen-200"
        @change="emitRating"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineEmits, defineProps, ref } from "vue";

const props = defineProps<{
  body: string;
  id: string;
}>();

const selected = ref<number | null>(null);

const emit = defineEmits<{
  (
    e: "rating-selected",
    payload: { questionId: String; rating: number | null }
  ): void;
}>();

function emitRating() {
  emit("rating-selected", { questionId: props.id, rating: selected.value });
  console.log("Rating selected:", {
    questionId: props.id,
    rating: selected.value,
  });
}
</script>

<style scoped>
.radio-large {
  width: 22px;
  height: 22px;
}
</style>
