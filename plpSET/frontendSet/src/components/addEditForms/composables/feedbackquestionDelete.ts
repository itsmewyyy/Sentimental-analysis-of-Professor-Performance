import { useDelete } from "@/components/addEditForms/composables/feedbackquestionMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { FeedbackQuestion } from "@/components/databaseManagement/feedbackquestions/type";

export function itemDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: FeedbackQuestion) => {
    if (confirm("Are you sure you want to delete this?")) {
      deleteItem(item.feedback_question_id, {
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

  const handleStoreItem = (item: FeedbackQuestion) => {
    localStorage.setItem("question_id", item.feedback_question_id);
  };

  return { handleDelete, handleStoreItem };
}
