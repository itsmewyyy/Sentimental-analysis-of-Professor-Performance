<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Category } from "@/components/databaseManagement/categories/columns";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { Search } from "lucide-vue-next";
import AddNCategory from "@/components/addEditForms/AddNCategory.vue";

interface DataTableToolbarProps {
  table: Table<Category>;
}

const props = defineProps<DataTableToolbarProps>();
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center relative">
      <span class="absolute left-3">
        <Search class="h-4 w-4 text-gray-500" />
      </span>
      <Input
        placeholder="Search"
        :model-value="(table.getColumn('category_desc')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[150px] lg:w-[250px] pl-10"
        @input="
          table.getColumn('category_desc')?.setFilterValue($event.target.value)
        "
      />
    </div>
    <AddNCategory></AddNCategory>
  </div>
</template>
