<script setup lang="ts">
import type { Phrase } from "./columns";
import { onMounted, ref } from "vue";
import { columns } from "@/components/collegerecurringPhrases/columns";
import DataTable from "@/components/collegerecurringPhrases/DataTable.vue";

const data = ref<Phrase[]>([]);
const collegeIdentifier = localStorage.getItem("college");
const yearsemIdentifier = localStorage.getItem("current_year_sem");

async function getData(): Promise<Phrase[]> {
  try {
    const response = await fetch(
      `https://sentiment-professor-feedback-1.onrender.com/api/recurring-college-phrases/?year_sem=${yearsemIdentifier}&dept_id=${collegeIdentifier}`
    );
    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    if (result && Array.isArray(result) && result.length > 0) {
      // Create a map to store aggregated phrase counts
      const phraseCounts: {
        [key: string]: { count: number; sentiment: string; phrase: string };
      } = {};

      result
        .filter((item) => item.year_sem === yearsemIdentifier)
        .flatMap((item) => item.college_phrases)
        .filter((college) => college.dept_id === collegeIdentifier)
        .flatMap((college) => college.recurring_phrases)
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
