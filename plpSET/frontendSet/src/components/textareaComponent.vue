<script setup lang="ts">
import { ref, defineProps, watch, defineEmits } from "vue";

const props = defineProps<{
  id: string;
  label: string;
  initialText?: string;
}>();

const emit = defineEmits<{
  (event: "input", value: string): void;
}>();

const inputValue = ref(props.initialText || "");

watch(
  () => props.initialText,
  (newVal) => {
    inputValue.value = newVal || "";
  }
);

// Emit changes to inputValue
watch(inputValue, (newValue) => {
  emit("input", newValue);
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
