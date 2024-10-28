import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/admins/DataTableRowActions.vue";

export interface Admin {
  admin_acc_id: string;
  admin_username: string;
  dept_id: string;
  is_mis: boolean;
  is_dean: boolean;
  is_secretary: boolean;
}

export const columns: ColumnDef<Admin>[] = [
  {
    accessorKey: "admin_acc_id",
    header: () => h("div", { class: "text-center text-xs" }, "Admin ID"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("admin_acc_id")
      );
    },
  },
  {
    accessorKey: "admin_username",
    header: () => h("div", { class: "text-center text-xs" }, "Username"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("admin_username")
      );
    },
  },
  {
    accessorKey: "dept_id",
    header: () => h("div", { class: "text-center text-xs" }, "Department"),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center font-normal" },
        row.getValue("dept_id")
      );
    },
  },
  {
    accessorKey: "role",
    header: () => h("div", { class: "text-center text-xs" }, "Role"),
    cell: ({ row }) => {
      const { is_dean, is_secretary, is_mis } = row.original;

      let role = "";
      if (is_dean) role = "Dean";
      else if (is_secretary) role = "Secretary";
      else if (is_mis) role = "MIS";

      return h("div", { class: "text-center font-normal" }, role);
    },
  },

  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
