<script setup lang="ts">
import type { Phrase } from "./columns";
import { onMounted, ref } from "vue";
import { columns } from "@/components/profsrecurringPhrases/columns";
import DataTable from "@/components/profsrecurringPhrases/DataTable.vue";

const data = ref<Phrase[]>([]);
const professorIdentifier = localStorage.getItem("professor");
const yearsemIdentifier = "24-25-1";

async function getData(): Promise<Phrase[]> {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/recurring-phrases/?year_sem=${yearsemIdentifier}&professor_id=${professorIdentifier}`
    );
    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    if (result && Array.isArray(result) && result.length > 0) {
      return result
        .filter((item) => item.year_sem === yearsemIdentifier) // Ensure we filter by year_sem first
        .flatMap((item) => item.professor_phrases) // Then flatten the professor phrases
        .filter((professor) => professor.id === professorIdentifier) // Filter by professor ID
        .flatMap((professor) =>
          professor.recurring_phrases.map((recurring_phrase) => ({
            count: recurring_phrase.count,
            sentiment: recurring_phrase.sentiment,
            phrase: recurring_phrase.phrase,
          }))
        );
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
