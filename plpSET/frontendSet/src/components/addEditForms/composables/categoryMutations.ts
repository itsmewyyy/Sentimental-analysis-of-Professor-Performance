import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Category } from "@/components/databaseManagement/categories/type";
import axios from "axios";

export function useAddCategory() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Category>({
    mutationFn: async (newCategory: Category) => {
      await axios.post("http://127.0.0.1:8000/api/categorycrud/", newCategory);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["categories"] });
    },
    onError: (error) => {
      console.error("Error adding category:", error);
    },
  });
}

export function useEditCategory() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Category>({
    mutationFn: async (updatedCategory: Category) => {
      await axios.put(
        `http://127.0.0.1:8000/api/categorycrud/${updatedCategory.category_id}/`,
        updatedCategory
      );
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["categories"] });
    },
    onError: (error) => {
      console.error("Error updating category:", error);
    },
  });
}

export function useDeleteCategory() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, string>({
    mutationFn: async (categoryId: string) => {
      await axios.delete(
        `http://127.0.0.1:8000/api/categorycrud/${categoryId}/`
      );
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["categories"] });
    },
    onError: (error) => {
      console.error("Error deleting category:", error);
    },
  });
}
