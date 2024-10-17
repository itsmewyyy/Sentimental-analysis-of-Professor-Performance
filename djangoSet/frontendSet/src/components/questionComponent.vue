<template>
  <div class="flex items-center p-2">
    <div
      class="rounded-lg flex flex-row items-center content-center bg-white p-4 min-w-full"
    >
      <div class="p-4 flex-1">
        <span v-if="body" class="font-medium text-darks-300 block">{{
          body
        }}</span>
        <span v-else class="font-medium text-darks-300 block"
          >No question available</span
        >
      </div>

      <div class="flex items-center p-2 space-x-14">
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
  </div>
</template>

<script setup lang="ts">
import { defineEmits, defineProps, ref } from "vue";
import { useRatingsStore } from "@/store/ratingStore";

const props = defineProps<{
  body: string;
  id: string;
}>();

const ratingStore = useRatingsStore();
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
  width: 16px;
  height: 16px;
}
</style>
