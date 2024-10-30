import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/subjects/DataTableRowActions.vue";

export interface Subject {
  subject_code: string;
  subject_desc: string;
  assoc_college: string;
}

export const columns: ColumnDef<Subject>[] = [
  {
    accessorKey: "subject_code",
    header: () => h("div", { class: "text-center text-xs" }, "Subject Code"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("subject_code")
      );
    },
  },
  {
    accessorKey: "subject_desc",
    header: () =>
      h("div", { class: "text-center text-xs" }, "Subject Description"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("subject_desc")
      );
    },
  },
  {
    accessorKey: "assoc_college",
    header: () =>
      h("div", { class: "text-center text-xs" }, "Associated College"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("assoc_college")
      );
    },
  },
  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
