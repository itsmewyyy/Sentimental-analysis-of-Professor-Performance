import { useDelete } from "@/components/addEditForms/composables/numquestionMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { NumQuestion } from "@/components/databaseManagement/numericalQuestions/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: NumQuestion) => {
    deleteItem(item.numerical_question_id, {
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
  };

  const handleStoreItem = (item: NumQuestion) => {
    localStorage.setItem("question_id", item.numerical_question_id);
  };

  return { handleDelete, handleStoreItem };
}
