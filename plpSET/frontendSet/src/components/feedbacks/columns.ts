import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";

// Define the Feedback interface
export interface Feedback {
  question_id: string;
  sentiment: string;
  text: string;
}

interface Professors {
  id: string;
  name: string;
  dept_id: string;
  dept_desc: string;
  feedbacks: Feedback[];
}

interface Summary {
  year_sem: string;
  professor_feedback_list: Professors[];
}

// Define the columns to reflect each field in Feedback
export const columns: ColumnDef<Feedback>[] = [
  {
    accessorKey: "question_id",
    header: () => h("div", { class: "text-center text-xs" }, "Question ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("question_id")
      );
    },
  },
  {
    accessorKey: "text",
    header: () => h("div", { class: "text-center text-xs" }, "Feedback Text"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("text")
      );
    },
  },
  {
    accessorKey: "sentiment",
    header: () => h("div", { class: "text-center text-xs" }, "Sentiment"),
    cell: ({ row }) => {
      const sentiment = row.getValue("sentiment") as string;
      const colorClass =
        sentiment === "Positive"
          ? "text-plpgreen-400"
          : sentiment === "Negative"
          ? "text-reds-800"
          : sentiment === "Neutral"
          ? "text-plpyellow-200"
          : "text-darks-500";

      return h(
        "div",
        { class: `text-center font-normal ${colorClass}` },
        sentiment
      );
    },
  },
];
