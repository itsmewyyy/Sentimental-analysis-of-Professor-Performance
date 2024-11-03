import { useDelete } from "@/components/addEditForms/composables/sectionMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Section } from "@/components/databaseManagement/sections/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Section) => {
    if (confirm("Are you sure you want to delete this?")) {
      deleteItem(item.section_id, {
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

  const handleStoreItem = (item: Section) => {
    localStorage.setItem("section", item.section_id);
  };

  return { handleDelete, handleStoreItem };
}
