import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Professor } from "@/components/databaseManagement/professors/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Professor>({
    mutationFn: async (Item: Professor) => {
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/professorinfocrud/",
        Item
      );
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error adding items:", error);
    },
  });
}

export function useEdit() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Professor>({
    mutationFn: async (updatedItem: Professor) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/professorinfocrud/${updatedItem.professor_id}/`,
        updatedItem
      );
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error updating category:", error);
    },
  });
}

export function useDelete() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, string>({
    mutationFn: async (Item: string) => {
      await axios.delete(
        `https://sentiment-professor-feedback-1.onrender.com/api/professorinfocrud/${Item}/`
      );
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error deleting items:", error);
    },
  });
}
