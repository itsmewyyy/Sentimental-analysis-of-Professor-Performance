<script setup lang="ts">
import { onMounted, ref } from "vue";
import { type Student } from "./type";
import { columns } from "./columns";
import DataTable from "@/components/databaseStudent/DataTable.vue";
import { useRoute } from "vue-router";
import { useQuery } from "@tanstack/vue-query";

const route = useRoute();
const sectionId = route.params.sectionId as string;

async function fetchCategories(): Promise<Student[]> {
  const response = await fetch(
    `http://127.0.0.1:8000/api/section/${sectionId}/`
  );
  if (!response.ok) {
    throw new Error("Failed to fetch categories");
  }
  return await response.json();
}

const { data } = useQuery<Student[]>({
  queryKey: ["items", sectionId],
  queryFn: fetchCategories,
  initialData: [],
  refetchOnWindowFocus: true,
});
</script>

<template>
  <div class="py-10 mx-auto w-full">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>
