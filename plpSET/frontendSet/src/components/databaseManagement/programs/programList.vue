<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { Program } from "./type";
import DataTable from "@/components/databaseManagement/programs/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<Program[]> {
  const response = await fetch("http://127.0.0.1:8000/api/program-list/");
  if (!response.ok) {
    throw new Error("Failed to fetch");
  }
  return await response.json();
}

const { data } = useQuery<Program[]>({
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
