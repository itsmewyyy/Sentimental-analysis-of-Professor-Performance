import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/professors/DataTableRowActions.vue";

export interface Professor {
  professor_id: string;
  surname: string;
  first_name: string;
  middle_name: string;
  full_name: string;
  department: string;
  department_desc: string;
  is_dean: boolean;
  status: string;
}

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
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
