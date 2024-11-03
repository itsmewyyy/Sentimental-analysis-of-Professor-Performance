import { useDelete } from "@/components/addEditForms/composables/collegeMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Department } from "@/components/databaseManagement/colleges/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Department) => {
    if (confirm("Are you sure you want to delete this?")) {
      deleteItem(item.department_id, {
        onSuccess: () => {
          toast({
            title: "Success",
            description: "Deleted successfully.",
          });
        },
        onError: (error) => {
          toast({
            title: "Error",
            description: error.message || "Failed to delete.",
          });
        },
      });
    }
  };

  const handleStoreItem = (item: Department) => {
    localStorage.setItem("college", item.department_id);
  };

  return { handleDelete, handleStoreItem };
}
