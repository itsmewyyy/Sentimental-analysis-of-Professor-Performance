<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Professor } from "@/components/databaseManagement/professors/columns";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { CirclePlus } from "lucide-vue-next";
import { Search } from "lucide-vue-next";

interface DataTableToolbarProps {
  table: Table<Professor>;
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
        placeholder="Search professor"
        :model-value="(table.getColumn('full_name')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[150px] lg:w-[250px] pl-10"
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
