<script setup lang="ts">
import type { Feedback } from "@/components/feedbacks/columns";
import { onMounted, ref, watch } from "vue";
import { columns } from "./columns";
import DataTable from "./DataTable.vue";

const data = ref<Feedback[]>([]);

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

async function getData(): Promise<Feedback[]> {
  try {
    const professorIdentifier = localStorage.getItem("professor");
    const yearsemIdentifier = localStorage.getItem("current_year_sem");
    const collegeIdentifier = localStorage.getItem("college"); // Retrieve the college identifier

    const response = await fetch(
      `http://127.0.0.1:8000/api/professor-feedbacks/?year_sem=${yearsemIdentifier}&professor_id=${professorIdentifier}`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    // Filter feedbacks for the specified professor, semester, and college
    if (result && Array.isArray(result) && result.length > 0) {
      return result
        .flatMap((item) => item.professor_feedback_list)
        .filter(
          (professor) =>
            professor.id === professorIdentifier &&
            professor.dept_id === collegeIdentifier // Use collegeIdentifier for local filtering
        )
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
  <div class="container py-10">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
