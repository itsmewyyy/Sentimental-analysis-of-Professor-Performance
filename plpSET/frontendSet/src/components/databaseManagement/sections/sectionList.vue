<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { Section } from "./type";
import DataTable from "@/components/databaseManagement/sections/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<Section[]> {
  const response = await fetch("http://127.0.0.1:8000/api/section-list/");
  if (!response.ok) {
    throw new Error("Failed to fetch");
  }
  return await response.json();
}

const { data } = useQuery<Section[]>({
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
