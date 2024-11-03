import { useDelete } from "@/components/addEditForms/composables/subjectMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Subject } from "@/components/databaseManagement/subjects/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Subject) => {
    if (confirm("Are you sure you want to delete this?")) {
      deleteItem(item.subject_code, {
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

  const handleStoreItem = (item: Subject) => {
    localStorage.setItem("subject", item.subject_code);
  };

  return { handleDelete, handleStoreItem };
}
