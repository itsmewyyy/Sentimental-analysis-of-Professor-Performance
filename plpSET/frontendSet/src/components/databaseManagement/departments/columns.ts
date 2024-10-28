import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/departments/DataTableRowActions.vue";

export interface Department {
  department_id: string;
  department_desc: string;
}

export const columns: ColumnDef<Department>[] = [
  {
    accessorKey: "department_id",
    header: () => h("div", { class: "text-center text-xs" }, "College Code"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("department_id")
      );
    },
  },
  {
    accessorKey: "department_desc",
    header: () =>
      h("div", { class: "text-center text-xs" }, "College Description"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("department_desc")
      );
    },
  },
  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
