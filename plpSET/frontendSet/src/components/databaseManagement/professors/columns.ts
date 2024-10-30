import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/professors/DataTableRowActions.vue";
import type { Professor } from "./type";
import { itemDelete } from "@/components/addEditForms/composables/professorDelete";

export const columns: ColumnDef<Professor>[] = [
  {
    accessorKey: "professor_id",
    header: () => h("div", { class: "text-center text-xs" }, "Professor ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("professor_id")
      );
    },
  },
  {
    accessorKey: "full_name",
    header: () => h("div", { class: "text-center text-xs" }, "Name"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("full_name")
      );
    },
  },
  {
    accessorKey: "department_desc",
    header: () => h("div", { class: "text-center text-xs" }, "Department"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("department_desc")
      );
    },
  },
  {
    accessorKey: "status",
    header: () => h("div", { class: "text-center text-xs" }, "Status"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("status")
      );
    },
  },
  {
    accessorKey: "is_dean",
    header: () => h("div", { class: "text-center text-xs" }, "Dean Status"),
    cell: ({ row }) => {
      const isDean = row.getValue("is_dean");
      return h(
        "div",
        { class: "text-center font-normal" },
        isDean ? "Dean" : ""
      );
    },
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = itemDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: Professor) => handleDelete(item),
        onStoreItem: (item: Professor) => handleStoreItem(item),
      });
    },
  },
];
