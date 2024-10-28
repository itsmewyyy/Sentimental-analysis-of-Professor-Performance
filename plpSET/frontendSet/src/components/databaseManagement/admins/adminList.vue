<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns, type Admin } from "./columns";
import DataTable from "@/components/databaseManagement/admins/DataTable.vue";

const data = ref<Admin[]>([]);

async function getData(): Promise<Admin[]> {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/admin-list/`);

    if (!response.ok) {
      throw new Error("Failed to fetch admin");
    }

    const result = await response.json();

    if (Array.isArray(result)) {
      return result;
    } else {
      console.warn("No admins found or unexpected response structure:", result);
      return [];
    }
  } catch (error) {
    console.error("Error fetching admins:", error);
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
