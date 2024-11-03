<script setup lang="ts">
import { ref, computed, Ref, onMounted } from "vue";
import ScrollArea from "../ui/scroll-area/ScrollArea.vue"; // Assuming this is your scroll area component
import axios from "axios";

type Section = {
  section_id: string;
  name: string;
};

type Program = {
  program_id: string;
  program_desc: string;
  sections: Section[];
};

type YearLevel = {
  year_level_id: number;
  year_level_desc: string;
  programs: Program[];
};

type College = {
  name: string;
  description: string;
  years: YearLevel[];
};

type Framework = {
  value: string;
  label: string;
};

const FRAMEWORKS = ref<Framework[]>([]);

const inputRef = ref<HTMLInputElement | null>(null);
const open = ref<boolean>(false);
const selected = ref<Framework[]>([]);
const inputValue = ref<string>("");

const emits = defineEmits(["updateSections"]);

const loadSectionsByCollege = async () => {
  const college = localStorage.getItem("college");
  if (college) {
    try {
      const response = await axios.get(
        "https://sentiment-professor-feedback-1.onrender.com/api/colleges/"
      );
      const colleges: College[] = response.data;

      const selectedCollege = colleges.find((c) => c.name === college);
      if (selectedCollege) {
        FRAMEWORKS.value = selectedCollege.years.flatMap((year) =>
          year.programs.flatMap((program) =>
            program.sections.map((section) => ({
              value: section.section_id,
              label: section.section_id,
            }))
          )
        );
      }
    } catch (error) {
      console.error("Error loading sections:", error);
    }
  }
};

onMounted(() => {
  loadSectionsByCollege();
});

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
  FRAMEWORKS.value.filter((framework) => !selected.value.includes(framework))
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
          placeholder="Select section/s"
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
                  emits('updateSections', selected);
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
