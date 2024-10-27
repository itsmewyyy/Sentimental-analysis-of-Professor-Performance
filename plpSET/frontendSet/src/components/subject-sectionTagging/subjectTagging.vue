<script setup lang="ts">
import { ref, computed, Ref } from "vue";
import ScrollArea from "../ui/scroll-area/ScrollArea.vue"; // Assuming this is your scroll area component

type Framework = {
  value: string;
  label: string;
};

const FRAMEWORKS: Framework[] = [
  { value: "next.js", label: "Next.js" },
  { value: "sveltekit", label: "SvelteKit" },
  { value: "nuxt.js", label: "Nuxt.js" },
  { value: "remix", label: "Remix" },
  { value: "astro", label: "Astro" },
  { value: "wordpress", label: "WordPress" },
  { value: "express.js", label: "Express.js" },
  { value: "nest.js", label: "Nest.js" },
];

const inputRef = ref<HTMLInputElement | null>(null);
const open = ref<boolean>(false);
const selected = ref<Framework[]>([FRAMEWORKS[1]]);
const inputValue = ref<string>("");

const handleUnselect = (framework: Framework): void => {
  selected.value = selected.value.filter((s) => s.value !== framework.value);
};

const handleKeyDown = (e: KeyboardEvent): void => {
  const input = inputRef.value;
  if (input) {
    if (e.key === "Delete" || e.key === "Backspace") {
      if (inputValue.value === "") {
        selected.value.pop();
      }
    }
    if (e.key === "Escape") {
      input.blur();
    }
  }
};

const selectables = computed((): Framework[] =>
  FRAMEWORKS.filter((framework) => !selected.value.includes(framework))
);
</script>

<template>
  <div @keydown="handleKeyDown" class="overflow-visible bg-transparent w-1/2">
    <div
      class="group rounded-md px-3 py-2 text-sm ring-offset-white focus-within:ring-2 focus-within:ring-plpgreen-200 focus-within:ring-offset-2 cursor-pointer"
    >
      <div class="flex flex-wrap gap-1">
        <div
          v-for="framework in selected"
          :key="framework.value"
          class="bg-gray-100 text-gray-800 rounded-md px-2 py-1 text-sm flex items-center"
        >
          {{ framework.label }}
          <button
            class="ml-1 rounded-md outline-none focus:ring-1 focus:ring-plpgreen-200 focus:ring-offset-1"
            @keydown.enter="handleUnselect(framework)"
            @mousedown.prevent.stop
            @click="handleUnselect(framework)"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-3 w-3 text-gray-400 hover:text-gray-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        <input
          ref="inputRef"
          v-model="inputValue"
          @blur="open = false"
          @focus="open = true"
          placeholder="Select subject/s"
          class="bg-transparent outline-none placeholder-gray-400 cursor-pointer caret-transparent"
        />
      </div>
    </div>

    <div v-if="open && selectables.length > 0" class="relative mt-2">
      <div
        class="absolute top-0 z-10 w-full rounded-md border bg-white text-gray-900 shadow-md outline-none animate-in p-2"
      >
        <ScrollArea class="h-54">
          <div class="h-full overflow-auto">
            <div
              v-for="framework in selectables"
              :key="framework.value"
              class="cursor-pointer p-2 hover:bg-gray-100 text-sm"
              @mousedown.prevent.stop
              @click="
                () => {
                  selected.push(framework);
                  inputValue = '';
                }
              "
            >
              {{ framework.label }}
            </div>
          </div>
        </ScrollArea>
      </div>
    </div>
  </div>
</template>
