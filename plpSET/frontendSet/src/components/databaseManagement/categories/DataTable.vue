<script setup lang="ts" generic="TData, TValue">
import type { ColumnDef, ColumnFiltersState } from "@tanstack/vue-table";
import type { Category } from "./columns";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { ref } from "vue";
import {
  getFacetedRowModel,
  getFacetedUniqueValues,
  getFilteredRowModel,
  FlexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useVueTable,
} from "@tanstack/vue-table";
import { Button } from "@/components/ui/button";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
import { FileUp } from "lucide-vue-next";
import { valueUpdater } from "@/lib/utils";
import DataTablePagination from "@/components/databaseManagement/categories/DataTablePagination.vue";
import DataTableToolbar from "@/components/databaseManagement/categories/DataTableToolbar.vue";

interface DataTableProps {
  columns: ColumnDef<Category, any>[];
  data: Category[];
}

const props = defineProps<DataTableProps>();

const columnFilters = ref<ColumnFiltersState>([]);

const table = useVueTable({
  get data() {
    return props.data;
  },
  get columns() {
    return props.columns;
  },
  state: {
    get columnFilters() {
      return columnFilters.value;
    },
  },
  enableRowSelection: true,

  onColumnFiltersChange: (updaterOrValue) =>
    valueUpdater(updaterOrValue, columnFilters),
  getCoreRowModel: getCoreRowModel(),
  getFilteredRowModel: getFilteredRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
  getFacetedRowModel: getFacetedRowModel(),
  getFacetedUniqueValues: getFacetedUniqueValues(),
});
</script>

<template>
  <div class="space-y-2 w-full">
    <DataTableToolbar :table="table" />
    <ScrollArea class="h-[540px]">
      <div class="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow
              v-for="headerGroup in table.getHeaderGroups()"
              :key="headerGroup.id"
              class="h-4"
            >
              <TableHead v-for="header in headerGroup.headers" :key="header.id">
                <FlexRender
                  v-if="!header.isPlaceholder"
                  :render="header.column.columnDef.header"
                  :props="header.getContext()"
                />
              </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <template v-if="table.getRowModel().rows?.length">
              <TableRow
                v-for="row in table.getRowModel().rows"
                :key="row.id"
                :data-state="row.getIsSelected() && 'selected'"
              >
                <TableCell v-for="cell in row.getVisibleCells()" :key="cell.id">
                  <FlexRender
                    :render="cell.column.columnDef.cell"
                    :props="cell.getContext()"
                  />
                </TableCell>
              </TableRow>
            </template>

            <TableRow v-else>
              <TableCell :colspan="columns.length" class="text-center py-40">
                <div class="space-y-4">
                  <p class="text-reds-200">No results.</p>
                </div>
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </div></ScrollArea
    >
    <DataTablePagination :table="table" />
  </div>
</template>
