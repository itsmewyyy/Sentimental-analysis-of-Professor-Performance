import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/colleges/DataTableRowActions.vue";
import type { Department } from "./type";
import { itemDelete } from "@/components/addEditForms/composables/collegeDelete";

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
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = itemDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: Department) => handleDelete(item),
        onStoreItem: (item: Department) => handleStoreItem(item),
      });
    },
  },
];
