<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { FeedbackQuestion } from "./type";
import DataTable from "@/components/databaseManagement/feedbackquestions/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<FeedbackQuestion[]> {
  const response = await fetch(
    "https://sentiment-professor-feedback-1.onrender.com/api/feedback-questions/"
  );
  if (!response.ok) {
    throw new Error("Failed to fetch");
  }
  return await response.json();
}

const { data } = useQuery<FeedbackQuestion[]>({
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
