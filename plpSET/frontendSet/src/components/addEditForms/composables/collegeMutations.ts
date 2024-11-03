import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Department } from "@/components/databaseManagement/colleges/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Department>({
    mutationFn: async (Item: Department) => {
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/collegecrud/",
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

  return useMutation<void, Error, Department>({
    mutationFn: async (updatedItem: Department) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/collegecrud/${updatedItem.department_id}/`,
        updatedItem
      );
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error updating items:", error);
    },
  });
}

export function useDelete() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, string>({
    mutationFn: async (Item: string) => {
      await axios.delete(
        `https://sentiment-professor-feedback-1.onrender.com/api/collegecrud/${Item}/`
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
