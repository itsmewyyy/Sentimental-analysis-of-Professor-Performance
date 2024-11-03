import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { FeedbackQuestion } from "@/components/databaseManagement/feedbackquestions/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, FeedbackQuestion>({
    mutationFn: async (Item: FeedbackQuestion) => {
      await axios.post(
        "http://127.0.0.1:8000/api/feedback-questioncrud/",
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

  return useMutation<void, Error, FeedbackQuestion>({
    mutationFn: async (updatedItem: FeedbackQuestion) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/feedback-questioncrud/${updatedItem.feedback_question_id}/`,
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
        `https://sentiment-professor-feedback-1.onrender.com/api/feedback-questioncrud/${Item}/`
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
