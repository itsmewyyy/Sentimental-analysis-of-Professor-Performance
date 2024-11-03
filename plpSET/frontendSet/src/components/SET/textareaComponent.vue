<script setup lang="ts">
import { ref, defineProps, watch, defineEmits, onMounted } from "vue";
import { useRatingsStore } from "@/store/ratingStore"; // Ensure the correct path

const props = defineProps<{
  id: string;
  label: string;
  initialText?: string;
}>();

const emit = defineEmits<{
  (event: "input", value: string): void;
}>();

const ratingsStore = useRatingsStore();
const inputValue = ref(props.initialText || "");

// Load initial feedback from the store when the component mounts
onMounted(() => {
  inputValue.value = ratingsStore.feedbackRatings[props.id] || ""; // Set feedback from store
});

// Watch for changes in the store's feedback for this specific question
watch(
  () => ratingsStore.feedbackRatings[props.id],
  (newVal) => {
    inputValue.value = newVal || ""; // Update inputValue when store changes
  }
);

watch(inputValue, (newValue) => {
  emit("input", newValue);
  if (newValue !== ratingsStore.feedbackRatings[props.id]) {
    ratingsStore.setFeedbackRating(props.id, newValue);
  }
});
</script>

<template>
  <div class="px-12 py-10 bg-white rounded-lg space-y-4">
    <label :for="id" class="block text-base font-medium text-darks-300">{{
      label
    }}</label>
    <div class="relative">
      <textarea
        :id="id"
        v-model="inputValue"
        rows="1"
        style="resize: none"
        class="block w-full px-0 text-sm text-darks-800 bg-white border-0 focus:ring-0"
        placeholder="Write a feedback..."
        required
      ></textarea>
      <div class="absolute bottom-0 left-0 w-full h-0.5 bg-gray-100"></div>
    </div>
  </div>
</template>

<style scoped></style>
