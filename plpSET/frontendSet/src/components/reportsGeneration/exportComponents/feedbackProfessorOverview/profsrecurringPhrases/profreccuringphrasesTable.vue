<script setup lang="ts">
import type { Phrase } from "./columns";
import { onMounted, ref, watch } from "vue";
import { columns } from "./columns";
import DataTable from "./DataTable.vue";

const data = ref<Phrase[]>([]);

const props = defineProps({
  refreshChart: Boolean,
});

watch(
  () => props.refreshChart,
  async (newValue) => {
    console.log("refreshChart changed:", newValue);
    data.value = await getData();
  }
);

async function getData(): Promise<Phrase[]> {
  const professorIdentifier = localStorage.getItem("professor");
  const yearsemIdentifier = "24-25-1";
  const collegeIdentifier = localStorage.getItem("college");

  if (!professorIdentifier) {
    console.error("Professor ID not found in localStorage.");
    return [];
  }

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/recurring-phrases/?year_sem=${yearsemIdentifier}`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    if (Array.isArray(result) && result.length > 0) {
      // Filter professors based on college
      const filteredProfessors = result
        .filter((item) => item.year_sem === yearsemIdentifier)
        .flatMap((item) => item.professor_phrases)
        .filter(
          (professor) =>
            professor.id === professorIdentifier &&
            (professor.dept_id === collegeIdentifier ||
              professor.dept_desc === collegeIdentifier)
        );

      // Process phrases
      const phraseCounts: Record<
        string,
        { count: number; sentiment: string; phrase: string }
      > = {};

      filteredProfessors
        .flatMap((professor) => professor.recurring_phrases)
        .forEach((recurring_phrase) => {
          const phraseKey = recurring_phrase.phrase;

          if (phraseCounts[phraseKey]) {
            phraseCounts[phraseKey].count += Number(recurring_phrase.count);
          } else {
            phraseCounts[phraseKey] = {
              count: Number(recurring_phrase.count),
              sentiment: recurring_phrase.sentiment,
              phrase: recurring_phrase.phrase,
            };
          }
        });

      return Object.values(phraseCounts);
    }

    return [];
  } catch (error) {
    console.error("Error fetching data:", error);
    return [];
  }
}

onMounted(async () => {
  data.value = await getData();
});
</script>

<template>
  <div class="container py-10 mx-auto">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
