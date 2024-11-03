import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import DataTableRowActions from "@/components/databaseManagement/admins/DataTableRowActions.vue";
import type { Admin } from "./type";
import { itemDelete } from "@/components/addEditForms/composables/adminDelete";

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
    cell: ({ row }) => {
      const { handleDelete, handleStoreItem } = itemDelete();

      return h(DataTableRowActions, {
        row,
        onDelete: (item: Admin) => handleDelete(item),
        onStoreItem: (item: Admin) => handleStoreItem(item),
      });
    },
  },
];
