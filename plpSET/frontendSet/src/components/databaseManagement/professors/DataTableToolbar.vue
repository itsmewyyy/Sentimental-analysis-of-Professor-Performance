<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Professor } from "@/components/databaseManagement/professors/columns";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { CirclePlus } from "lucide-vue-next";

interface DataTableToolbarProps {
  table: Table<Professor>;
}

const props = defineProps<DataTableToolbarProps>();
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-2">
      <Input
        placeholder="Filter by Name"
        :model-value="(table.getColumn('full_name')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[50px] lg:w-[150px]"
        @input="
          table.getColumn('full_name')?.setFilterValue($event.target.value)
        "
      />
    </div>
    <Button class="h-8 text-sm p-4 bg-plpgreen-200 hover:bg-plpgreen-400">
      <CirclePlus class="mr-2 h-4 w-4" />
      <p>Add</p></Button
    >
  </div>
</template>
