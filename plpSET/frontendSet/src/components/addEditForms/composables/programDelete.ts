import { useDelete } from "@/components/addEditForms/composables/programMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Program } from "@/components/databaseManagement/programs/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Program) => {
    if (confirm("Are you sure you want to delete this?")) {
      deleteItem(item.program_id, {
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

  const handleStoreItem = (item: Program) => {
    localStorage.setItem("program", item.program_id);
  };

  return { handleDelete, handleStoreItem };
}
