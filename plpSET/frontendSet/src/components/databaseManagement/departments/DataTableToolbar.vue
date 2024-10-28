<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Department } from "@/components/databaseManagement/departments/columns";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { CirclePlus } from "lucide-vue-next";

interface DataTableToolbarProps {
  table: Table<Department>;
}

const props = defineProps<DataTableToolbarProps>();
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-2">
      <Input
        placeholder="Filter by College"
        :model-value="(table.getColumn('department_desc')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[50px] lg:w-[150px]"
        @input="
          table
            .getColumn('department_desc')
            ?.setFilterValue($event.target.value)
        "
      />
    </div>
    <Button class="h-8 text-sm p-4 bg-plpgreen-200 hover:bg-plpgreen-400">
      <CirclePlus class="mr-2 h-4 w-4" />
      <p>Add</p></Button
    >
  </div>
</template>
