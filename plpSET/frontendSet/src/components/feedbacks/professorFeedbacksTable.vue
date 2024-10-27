<script setup lang="ts">
import type { Feedback } from "@/components/feedbacks/columns";
import { onMounted, ref } from "vue";
import { columns } from "@/components/feedbacks/columns";
import DataTable from "@/components/feedbacks/DataTable.vue";

const data = ref<Feedback[]>([]);
const professorIdentifier = localStorage.getItem("professor");
const yearsemIdentifier = "24-25-1";

async function getData(): Promise<Feedback[]> {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/professor-feedbacks/?year_sem=${yearsemIdentifier}&professor_id=${professorIdentifier}`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    // Extract feedbacks for the specified professor and semester
    if (result && Array.isArray(result) && result.length > 0) {
      return result
        .flatMap((item) => item.professor_feedback_list)
        .filter((professor) => professor.id === professorIdentifier)
        .flatMap((professor) =>
          professor.feedbacks.map((feedback) => ({
            question_id: feedback.question_id,
            sentiment: feedback.sentiment,
            text: feedback.text,
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
