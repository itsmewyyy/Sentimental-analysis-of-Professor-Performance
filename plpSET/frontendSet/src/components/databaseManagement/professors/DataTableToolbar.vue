<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Professor } from "./type";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { CirclePlus } from "lucide-vue-next";
import { Search } from "lucide-vue-next";
import AddProf from "@/components/addEditForms/AddProf.vue";

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
    <AddProf></AddProf>
  </div>
</template>
