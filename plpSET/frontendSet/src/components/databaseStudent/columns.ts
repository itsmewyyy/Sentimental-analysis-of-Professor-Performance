import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "./DataTableRowActions.vue";
import type { Student } from "./type";
import { studentDelete } from "@/components/addEditForms/composables/studentDelete";
import DataTableColumnHeader from "./DataTableColumnHeader.vue";

export const columns: ColumnDef<Student>[] = [
  {
    accessorKey: "student_id",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Student ID" }),
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
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "Name" }),
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
    header: () => h("div", { class: "text-xs text-center" }, "Section"),
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
