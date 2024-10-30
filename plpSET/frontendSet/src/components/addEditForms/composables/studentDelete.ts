import { useDelete } from "@/components/addEditForms/composables/studentMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Student } from "@/components/databaseStudent/type";

export function studentDelete() {
  const { toast } = useToast();
  const { mutate: deleteItem } = useDelete();

  const handleDelete = (item: Student) => {
    if (confirm("Are you sure you want to delete this student?")) {
      deleteItem(item.student_id, {
        onSuccess: () => {
          toast({
            title: "Success",
            description: "Student deleted successfully.",
          });
        },
        onError: (error) => {
          toast({
            title: "Error",
            description:
              error.message || "Failed to delete student information.",
          });
        },
      });
    }
  };

  const handleStoreItem = (item: Student) => {
    localStorage.setItem("student", item.student_id);
  };

  return { handleDelete, handleStoreItem };
}
