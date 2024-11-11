import { useDelete } from "@/components/addEditForms/composables/adminMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Admin } from "@/components/databaseManagement/admins/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Admin) => {
    deleteItem(item.admin_acc_id, {
      onSuccess: () => {
        toast({
          title: "Success",
          description: "Deleted successfully.",
        });
      },
      onError: (error) => {
        toast({
          title: "Error",
          description: error.message || "Failed to delete information.",
        });
      },
    });
  };

  const handleStoreItem = (item: Admin) => {
    localStorage.setItem("admin_info", item.admin_acc_id);
  };

  return { handleDelete, handleStoreItem };
}
