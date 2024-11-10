import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { NumQuestion } from "@/components/databaseManagement/numericalQuestions/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, NumQuestion>({
    mutationFn: async (Item: NumQuestion) => {
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/numerical-questioncrud/",
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

  return useMutation<void, Error, NumQuestion>({
    mutationFn: async (updatedItem: NumQuestion) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/numerical-questioncrud/${updatedItem.numerical_question_id}/`,
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
        `https://sentiment-professor-feedback-1.onrender.com/api/numerical-questioncrud/${Item}/`
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
