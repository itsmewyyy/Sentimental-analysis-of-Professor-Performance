import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/numericalQuestions/DataTableRowActions.vue";
import type { NumQuestion } from "./type";
import { itemDelete } from "@/components/addEditForms/composables/numquestionDelete";

export const columns: ColumnDef<NumQuestion>[] = [
  {
    accessorKey: "numerical_question_id",
    header: () => h("div", { class: "text-center text-xs" }, "Question ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("numerical_question_id")
      );
    },
  },
  {
    accessorKey: "category",
    header: () => h("div", { class: "text-center text-xs" }, "Category"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("category")
      );
    },
  },
  {
    accessorKey: "question",
    header: () => h("div", { class: "text-center text-xs" }, "Question"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("question")
      );
    },
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = itemDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: NumQuestion) => handleDelete(item),
        onStoreItem: (item: NumQuestion) => handleStoreItem(item),
      });
    },
  },
];
