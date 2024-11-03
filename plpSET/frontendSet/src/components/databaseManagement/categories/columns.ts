import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/categories/DataTableRowActions.vue";
import { categoryDelete } from "@/components/addEditForms/composables/categoryDelete";
import type { Category } from "./type";

export const columns: ColumnDef<Category>[] = [
  {
    accessorKey: "category_id",
    header: () => h("div", { class: "text-center text-xs" }, "Category ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("category_id")
      );
    },
  },
  {
    accessorKey: "category_desc",
    header: () =>
      h("div", { class: "text-center text-xs" }, "Category Description"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("category_desc")
      );
    },
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = categoryDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (category: Category) => handleDelete(category),
        onStoreItem: (category: Category) => handleStoreItem(category),
      });
    },
  },
];
