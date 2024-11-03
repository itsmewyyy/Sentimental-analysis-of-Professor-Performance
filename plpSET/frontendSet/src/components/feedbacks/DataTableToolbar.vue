<script setup lang="ts">
import type { Table } from "@tanstack/vue-table";
import type { Feedback } from "@/components/feedbacks/columns";
import Button from "../ui/button/Button.vue";
import Input from "@/components/ui/input/Input.vue";
import { computed } from "vue";
import { question_id, sentiment } from "@/components/feedbacks/data";
import DataTableFacetedFilter from "@/components/feedbacks/DataTableFacetedFilter.vue";

interface DataTableToolbarProps {
  table: Table<Feedback>;
}

const props = defineProps<DataTableToolbarProps>();

const isFiltered = computed(
  () => props.table.getState().columnFilters.length > 0
);

import { X } from "lucide-vue-next";
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-2">
      <Input
        placeholder="Filter texts..."
        :model-value="(table.getColumn('text')?.getFilterValue() as string) ?? ''"
        class="h-8 w-[150px] lg:w-[250px]"
        @input="table.getColumn('text')?.setFilterValue($event.target.value)"
      />
      <DataTableFacetedFilter
        v-if="table.getColumn('question_id')"
        :column="table.getColumn('question_id')"
        title="Question"
        :options="question_id"
      />
      <DataTableFacetedFilter
        v-if="table.getColumn('sentiment')"
        :column="table.getColumn('sentiment')"
        title="Sentiment"
        :options="sentiment"
      />

      <Button
        v-if="isFiltered"
        variant="ghost"
        class="h-8 px-2 lg:px-3 text-darks-500"
        @click="table.resetColumnFilters()"
      >
        Reset <X class="ml-2 h-4 w-4" />
      </Button>
    </div>
  </div>
</template>
