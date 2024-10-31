<script setup lang="ts">
import type { Phrase } from "./columns";
import { onMounted, ref } from "vue";
import { columns } from "@/components/collegerecurringPhrases/columns";
import DataTable from "@/components/collegerecurringPhrases/DataTable.vue";

const data = ref<Phrase[]>([]);
const collegeIdentifier = localStorage.getItem("college");
const yearsemIdentifier = "24-25-1";

async function getData(): Promise<Phrase[]> {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/recurring-college-phrases/?year_sem=${yearsemIdentifier}&dept_id=${collegeIdentifier}`
    );
    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    if (result && Array.isArray(result) && result.length > 0) {
      return result
        .filter((item) => item.year_sem === yearsemIdentifier) // Filter by year_sem
        .flatMap((item) => item.college_phrases) // Flatten professor phrases
        .filter((college) => college.dept_id === collegeIdentifier) // Filter by dept_id
        .flatMap((college) =>
          college.recurring_phrases.map((recurring_phrase) => ({
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
