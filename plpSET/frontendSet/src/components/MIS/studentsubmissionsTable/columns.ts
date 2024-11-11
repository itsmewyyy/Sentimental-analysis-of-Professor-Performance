import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";

export interface StudentFeedback {
  studentId: string;
  name: string;
  section: string;
  program: string;
  incomplete_subject_count: number;
  total_subject_count: number;
}

export const columns: ColumnDef<StudentFeedback>[] = [
  {
    accessorKey: "studentId",
    header: () => h("div", { class: "text-center text-xs" }, "Student ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("studentId")
      );
    },
  },
  {
    accessorKey: "name",
    header: () => h("div", { class: "text-center text-xs" }, "Name"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("name")
      );
    },
  },
  {
    accessorKey: "section",
    header: () => h("div", { class: "text-center text-xs" }, "Section"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("section")
      );
    },
  },
  {
    accessorKey: "program",
    header: () => h("div", { class: "text-center text-xs" }, "Program"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("program")
      );
    },
  },
  {
    accessorKey: "incomplete_subject_count",
    header: () => h("div", { class: "text-center text-xs" }, "Pendings"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("incomplete_subject_count")
      );
    },
  },
  {
    accessorKey: "total_subject_count",
    header: () => h("div", { class: "text-center text-xs" }, "Total Subjects"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("total_subject_count")
      );
    },
  },
];
