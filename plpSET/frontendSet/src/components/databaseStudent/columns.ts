import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "./DataTableRowActions.vue";

export interface Student {
  student_id: string;
  full_name: string;
  section: string;
}

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
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
