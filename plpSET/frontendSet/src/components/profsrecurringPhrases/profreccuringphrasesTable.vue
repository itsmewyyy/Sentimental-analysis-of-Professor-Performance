<script setup lang="ts">
import type { Phrase } from "./columns";
import { onMounted, ref } from "vue";
import { columns } from "@/components/profsrecurringPhrases/columns";
import DataTable from "@/components/profsrecurringPhrases/DataTable.vue";

const data = ref<Phrase[]>([]);
const professorIdentifier = localStorage.getItem("professor");
const yearsemIdentifier = localStorage.getItem("current_year_sem");

async function getData(): Promise<Phrase[]> {
  if (!professorIdentifier) {
    console.error("Professor ID not found in localStorage.");
    return [];
  }

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/recurring-phrases/?year_sem=${yearsemIdentifier}&professor_id=${professorIdentifier}`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    if (Array.isArray(result) && result.length > 0) {
      const phraseCounts: Record<
        string,
        { count: number; sentiment: string; phrase: string }
      > = {};

      result
        .filter((item) => item.year_sem === yearsemIdentifier)
        .flatMap((item) => item.professor_phrases)
        .filter((professor) => professor.id === professorIdentifier)
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
