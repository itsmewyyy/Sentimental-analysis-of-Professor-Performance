<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { NumQuestion } from "./type";
import DataTable from "@/components/databaseManagement/numericalQuestions/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<NumQuestion[]> {
  const response = await fetch(
    "https://sentiment-professor-feedback-1.onrender.com/api/numerical-questions/"
  );
  if (!response.ok) {
    throw new Error("Failed to fetch");
  }
  return await response.json();
}

const { data } = useQuery<NumQuestion[]>({
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
