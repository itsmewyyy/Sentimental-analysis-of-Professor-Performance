<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { Department } from "./type";
import DataTable from "@/components/databaseManagement/colleges/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<Department[]> {
  const response = await fetch("http://127.0.0.1:8000/api/department-list/");
  if (!response.ok) {
    throw new Error("Failed to fetch");
  }
  return await response.json();
}

const { data } = useQuery<Department[]>({
  queryKey: ["items"],
  queryFn: fetchCategories,
  initialData: [],
});
</script>

<template>
  <div class="py-10 mx-auto w-full">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
