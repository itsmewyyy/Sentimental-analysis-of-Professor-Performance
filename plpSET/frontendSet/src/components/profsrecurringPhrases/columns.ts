import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";

export interface Phrase {
  count: number;
  sentiment: string;
  phrase: string;
}

interface Professors {
  id: string;
  name: string;
  dept_id: string;
  dept_desc: string;
  recurring_phrases: Phrase[];
}

interface Summary {
  year_sem: string;
  professor_phrases: Professors[];
}

// Define the columns to reflect each field in Feedback
export const columns: ColumnDef<Phrase>[] = [
  {
    accessorKey: "count",
    header: () => h("div", { class: "text-center text-xs" }, "Count"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("count")
      );
    },
  },
  {
    accessorKey: "phrase",
    header: () => h("div", { class: "text-center text-xs" }, "Phrase"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("phrase")
      );
    },
  },
  {
    accessorKey: "sentiment",
    header: () => h("div", { class: "text-center text-xs" }, "Sentiment"),
    cell: ({ row }) => {
      const sentiment = row.getValue("sentiment") as string;
      const colorClass =
        sentiment === "positive"
          ? "text-plpgreen-400"
          : sentiment === "negative"
          ? "text-reds-800"
          : sentiment === "neutral"
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
