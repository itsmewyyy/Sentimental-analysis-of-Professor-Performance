<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Program } from "./type";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";

import { Search } from "lucide-vue-next";
import AddProgram from "@/components/addEditForms/AddProgram.vue";

interface DataTableToolbarProps {
  table: Table<Program>;
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
        placeholder="Search program"
        :model-value="(table.getColumn('program_desc')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[150px] lg:w-[250px] pl-10"
        @input="
          table.getColumn('program_desc')?.setFilterValue($event.target.value)
        "
      />
    </div>
    <AddProgram></AddProgram>
  </div>
</template>
