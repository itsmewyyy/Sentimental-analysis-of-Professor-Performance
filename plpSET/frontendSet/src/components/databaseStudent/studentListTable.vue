<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns, type Student } from "./columns";
import DataTable from "@/components/databaseStudent/DataTable.vue";
import { useRoute } from "vue-router";

const route = useRoute();
const data = ref<Student[]>([]);
const sectionId = route.params.sectionId as string;

async function getData(): Promise<Student[]> {
  if (!sectionId) {
    console.error("Section ID is missing");
    return [];
  }

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/section/${sectionId}/`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch student data");
    }

    const result = await response.json();

    if (Array.isArray(result)) {
      return result;
    } else {
      console.warn(
        "No students found or unexpected response structure:",
        result
      );
      return [];
    }
  } catch (error) {
    console.error("Error fetching students:", error);
    return [];
  }
}

onMounted(async () => {
  data.value = await getData();
});
</script>

<template>
  <div class="py-10 mx-auto w-full">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
