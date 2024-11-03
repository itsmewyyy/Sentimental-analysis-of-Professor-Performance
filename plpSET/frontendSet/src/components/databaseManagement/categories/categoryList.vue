<script setup lang="ts">
import { onMounted, ref } from "vue";
import { type Category } from "./type";
import { columns } from "./columns";
import DataTable from "@/components/databaseManagement/categories/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<Category[]> {
  const response = await fetch(
    `https://sentiment-professor-feedback-1.onrender.com/api/numerical-categories/`
  );
  if (!response.ok) {
    throw new Error("Failed to fetch categories");
  }
  return await response.json();
}

const { data } = useQuery<Category[]>({
  queryKey: ["categories"],
  queryFn: fetchCategories,
  initialData: [],
});
</script>

<template>
  <div class="py-10 mx-auto w-full">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
