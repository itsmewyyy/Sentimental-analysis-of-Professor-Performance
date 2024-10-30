import { useDeleteCategory } from "@/components/addEditForms/composables/categoryMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import type { Category } from "@/components/databaseManagement/categories/type";

export function categoryDelete() {
  const { toast } = useToast();
  const { mutate: deleteCategory } = useDeleteCategory();

  const handleDelete = (category: Category) => {
    if (confirm("Are you sure you want to delete this category?")) {
      deleteCategory(category.category_id, {
        onSuccess: () => {
          toast({
            title: "Success",
            description: "Category deleted successfully.",
          });
        },
        onError: (error) => {
          toast({
            title: "Error",
            description: error.message || "Failed to delete category.",
          });
        },
      });
    }
  };

  const handleStoreItem = (category: Category) => {
    localStorage.setItem("category", category.category_id);
  };

  return { handleDelete, handleStoreItem };
}
