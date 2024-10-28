import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/programs/DataTableRowActions.vue";

export interface Program {
  program_id: string;
  program_desc: string;
  dept_id: string;
}

export const columns: ColumnDef<Program>[] = [
  {
    accessorKey: "program_id",
    header: () => h("div", { class: "text-center text-xs" }, "Program Code"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("program_id")
      );
    },
  },
  {
    accessorKey: "program_desc",
    header: () =>
      h("div", { class: "text-center text-xs" }, "Program Description"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("program_desc")
      );
    },
  },
  {
    accessorKey: "dept_id",
    header: () => h("div", { class: "text-center text-xs" }, "College"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("dept_id")
      );
    },
  },

  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
