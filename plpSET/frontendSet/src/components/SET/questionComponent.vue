<template>
  <div class="flex items-center pb-1.5">
    <div
      class="rounded-md flex flex-row items-center content-center bg-white p-4 sm:p-5 min-w-full"
    >
      <div class="p-2 sm:p-4 flex-1">
        <span
          v-if="body"
          class="font-medium text-darks-200 block text-sm sm:text-base"
        >
          {{ body }}
        </span>
        <span v-else class="font-medium text-darks-300 text-xs sm:text-sm"
          >No question available</span
        >
      </div>

      <div class="flex items-center p-1 space-x-4 sm:space-x-8 lg:space-x-14">
        <input
          v-for="rating in [5, 4, 3, 2, 1]"
          :key="rating"
          type="radio"
          :value="rating"
          v-model="selected"
          class="radio-large w-4 h-4 sm:w-5 sm:h-5 text-plpgreen-200 focus:ring-plpgreen-200"
          @change="emitRating"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineEmits, defineProps, ref, onMounted } from "vue";
import { useRatingsStore } from "@/store/ratingStore";

const props = defineProps<{
  body: string;
  id: string;
}>();

const ratingsStore = useRatingsStore();
const selected = ref<number | null>(null);

onMounted(() => {
  selected.value = ratingsStore.numericalRatings[props.id] || null;
});

const emit = defineEmits<{
  (
    e: "rating-selected",
    payload: { questionId: string; rating: number | null }
  ): void;
}>();

function emitRating() {
  emit("rating-selected", { questionId: props.id, rating: selected.value });
  ratingsStore.setNumericalRating(props.id, selected.value);
  console.log("Rating selected:", {
    questionId: props.id,
    rating: selected.value,
  }); // Store the numerical rating in the ratings store
}
</script>

<style scoped>
.radio-large {
  width: 16px;
  height: 16px;
}
</style>
