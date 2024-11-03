<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { Professor } from "./type";
import DataTable from "@/components/databaseManagement/professors/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<Professor[]> {
  const response = await fetch(
    `https://sentiment-professor-feedback-1.onrender.com/api/professor-list/`
  );
  if (!response.ok) {
    throw new Error("Failed to fetch categories");
  }
  return await response.json();
}

const { data } = useQuery<Professor[]>({
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
