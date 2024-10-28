<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns, type Department } from "./columns";
import DataTable from "@/components/databaseManagement/departments/DataTable.vue";

const data = ref<Department[]>([]);

async function getData(): Promise<Department[]> {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/department-list/`);

    if (!response.ok) {
      throw new Error("Failed to fetch professor");
    }

    const result = await response.json();

    if (Array.isArray(result)) {
      return result;
    } else {
      console.warn(
        "No departments found or unexpected response structure:",
        result
      );
      return [];
    }
  } catch (error) {
    console.error("Error fetching departments:", error);
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
