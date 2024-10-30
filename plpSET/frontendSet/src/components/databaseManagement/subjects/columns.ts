import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/subjects/DataTableRowActions.vue";
import { itemDelete } from "@/components/addEditForms/composables/subjectDelete";
import type { Subject } from "./type";

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
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = itemDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: Subject) => handleDelete(item),
        onStoreItem: (item: Subject) => handleStoreItem(item),
      });
    },
  },
];
