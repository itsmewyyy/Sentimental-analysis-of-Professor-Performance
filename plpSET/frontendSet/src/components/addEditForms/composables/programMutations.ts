import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Program } from "@/components/databaseManagement/programs/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Program>({
    mutationFn: async (Item: Program) => {
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/programcrud/",
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

  return useMutation<void, Error, Program>({
    mutationFn: async (updatedItem: Program) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/programcrud/${updatedItem.program_id}/`,
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
        `https://sentiment-professor-feedback-1.onrender.com/api/programcrud/${Item}/`
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
