<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Section } from "./type";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { CirclePlus } from "lucide-vue-next";
import { Search } from "lucide-vue-next";
import AddSection from "@/components/addEditForms/AddSection.vue";

interface DataTableToolbarProps {
  table: Table<Section>;
}

const props = defineProps<DataTableToolbarProps>();
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-0 relative">
      <span class="absolute left-3">
        <Search class="h-4 w-4 text-gray-500" />
      </span>
      <Input
        placeholder="Search section code"
        :model-value="(table.getColumn('section_id')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[150px] lg:w-[250px] pl-10"
        @input="
          table.getColumn('section_id')?.setFilterValue($event.target.value)
        "
      />
    </div>
    <AddSection></AddSection>
  </div>
</template>
