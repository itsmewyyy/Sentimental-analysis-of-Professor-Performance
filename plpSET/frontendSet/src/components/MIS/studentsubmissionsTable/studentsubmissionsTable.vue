<script setup lang="ts">
import type { StudentFeedback } from "./columns";
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import DataTable from "./DataTable.vue";

const data = ref<StudentFeedback[]>([]);

async function getData(): Promise<StudentFeedback[]> {
  try {
    const response = await fetch(
      `https://sentiment-professor-feedback-1.onrender.com/api/incomplete-evaluations/`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch feedback data");
    }

    const result = await response.json();

    console.log("API response:", result);

    if (Array.isArray(result)) {
      return result.map((student) => ({
        studentId: student.student_id,
        name: student.name,
        section: student.section,
        program: student.program,
        incomplete_subject_count: student.incomplete_count,
        total_subject_count: student.total_count,
      }));
    } else {
      console.error("API response is not an array:", result);
      return [];
    }
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
  <div class="px-4 py-8">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
