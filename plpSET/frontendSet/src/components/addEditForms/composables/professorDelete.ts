import { useDelete } from "@/components/addEditForms/composables/professorMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Professor } from "@/components/databaseManagement/professors/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Professor) => {
    if (confirm("Are you sure you want to delete this student?")) {
      deleteItem(item.professor_id, {
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
    }
  };

  const handleStoreItem = (item: Professor) => {
    localStorage.setItem("professor", item.professor_id);
  };

  return { handleDelete, handleStoreItem };
}
