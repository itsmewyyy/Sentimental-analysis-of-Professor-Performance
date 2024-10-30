import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Department } from "@/components/databaseManagement/colleges/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Department>({
    mutationFn: async (Item: Department) => {
      await axios.post("http://127.0.0.1:8000/api/collegecrud/", Item);
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
        `http://127.0.0.1:8000/api/collegecrud/${updatedItem.department_id}/`,
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
      await axios.delete(`http://127.0.0.1:8000/api/collegecrud/${Item}/`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error deleting items:", error);
    },
  });
}
