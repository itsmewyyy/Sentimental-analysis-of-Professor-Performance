<script setup lang="ts">
import { onMounted, ref } from "vue";
import { columns } from "./columns";
import type { Admin } from "./type";
import DataTable from "@/components/databaseManagement/admins/DataTable.vue";
import { useQuery } from "@tanstack/vue-query";

async function fetchCategories(): Promise<Admin[]> {
  const response = await fetch(`http://127.0.0.1:8000/api/admin-list/`);
  if (!response.ok) {
    throw new Error("Failed to fetch categories");
  }
  return await response.json();
}

const { data } = useQuery<Admin[]>({
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
