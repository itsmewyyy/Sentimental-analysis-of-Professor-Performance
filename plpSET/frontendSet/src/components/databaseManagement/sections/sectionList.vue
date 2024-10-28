<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns, type Section } from "./columns";
import DataTable from "@/components/databaseManagement/sections/DataTable.vue";

const data = ref<Section[]>([]);

async function getData(): Promise<Section[]> {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/section-list/`);

    if (!response.ok) {
      throw new Error("Failed to fetch professor");
    }

    const result = await response.json();

    if (Array.isArray(result)) {
      return result;
    } else {
      console.warn(
        "No programs found or unexpected response structure:",
        result
      );
      return [];
    }
  } catch (error) {
    console.error("Error fetching programs:", error);
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
