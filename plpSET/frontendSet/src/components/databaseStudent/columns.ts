import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "./DataTableRowActions.vue";
import axios from "axios";
import type { Student } from "./type";
import { studentDelete } from "@/components/addEditForms/composables/studentDelete";

export const columns: ColumnDef<Student>[] = [
  {
    accessorKey: "student_id",
    header: () => h("div", { class: "text-center text-xs" }, "Student ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("student_id")
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
    accessorKey: "section",
    header: () => h("div", { class: "text-center text-xs" }, "Section"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("section")
      );
    },
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = studentDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: Student) => handleDelete(item),
        onStoreItem: (item: Student) => handleStoreItem(item),
      });
    },
  },
];
