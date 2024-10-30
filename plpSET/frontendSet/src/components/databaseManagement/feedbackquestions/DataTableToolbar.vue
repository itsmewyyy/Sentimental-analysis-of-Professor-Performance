<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { FeedbackQuestion } from "./type";
import { Button } from "@/components/ui/button";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { Search } from "lucide-vue-next";

import AddFeedQues from "@/components/addEditForms/AddFeedQues.vue";

interface DataTableToolbarProps {
  table: Table<FeedbackQuestion>;
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
        :model-value="(table.getColumn('question')?.getFilterValue() as string) ?? ''"
        class="h-10 w-[150px] lg:w-[250px] pl-10"
        @input="
          table.getColumn('question')?.setFilterValue($event.target.value)
        "
      />
    </div>
    <AddFeedQues></AddFeedQues>
  </div>
</template>
