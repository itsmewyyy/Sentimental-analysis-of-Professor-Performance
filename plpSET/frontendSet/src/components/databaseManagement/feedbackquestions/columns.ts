import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/feedbackquestions/DataTableRowActions.vue";
import type { FeedbackQuestion } from "./type";
import { itemDelete } from "@/components/addEditForms/composables/feedbackquestionDelete";

export const columns: ColumnDef<FeedbackQuestion>[] = [
  {
    accessorKey: "feedback_question_id",
    header: () => h("div", { class: "text-center text-xs" }, "Feedback ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("feedback_question_id")
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
        onDelete: (item: FeedbackQuestion) => handleDelete(item),
        onStoreItem: (item: FeedbackQuestion) => handleStoreItem(item),
      });
    },
  },
];
