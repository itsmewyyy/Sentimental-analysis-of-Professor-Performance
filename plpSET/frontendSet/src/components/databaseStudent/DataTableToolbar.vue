<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Student } from "@/components/databaseStudent/type";
import Button from "../ui/button/Button.vue";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { CirclePlus } from "lucide-vue-next";
import AddStudent from "../addEditForms/AddStudent.vue";

interface DataTableToolbarProps {
  table: Table<Student>;
}

const props = defineProps<DataTableToolbarProps>();
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-2">
      <Input
        placeholder="Filter by Student ID"
        :model-value="(table.getColumn('student_id')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[50px] lg:w-[150px]"
        @input="
          table.getColumn('student_id')?.setFilterValue($event.target.value)
        "
      />
      <Input
        placeholder="Filter by Name"
        :model-value="(table.getColumn('full_name')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[150px] lg:w-[250px]"
        @input="
          table.getColumn('full_name')?.setFilterValue($event.target.value)
        "
      />
    </div>
    <AddStudent></AddStudent>
  </div>
</template>
