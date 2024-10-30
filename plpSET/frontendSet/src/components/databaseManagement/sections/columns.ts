import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/sections/DataTableRowActions.vue";
import { itemDelete } from "@/components/addEditForms/composables/sectionDelete";
import type { Section } from "./type";

export const columns: ColumnDef<Section>[] = [
  {
    accessorKey: "section_id",
    header: () => h("div", { class: "text-center text-xs" }, "Section Code"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("section_id")
      );
    },
  },
  {
    accessorKey: "name",
    header: () => h("div", { class: "text-center text-xs" }, "Section Name"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("name")
      );
    },
  },
  {
    accessorKey: "program",
    header: () => h("div", { class: "text-center text-xs" }, "Program"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("program")
      );
    },
  },
  {
    accessorKey: "year_level",
    header: () => h("div", { class: "text-center text-xs" }, "Year Level"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("year_level")
      );
    },
  },

  {
    id: "actions",
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = itemDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: Section) => handleDelete(item),
        onStoreItem: (item: Section) => handleStoreItem(item),
      });
    },
  },
];
