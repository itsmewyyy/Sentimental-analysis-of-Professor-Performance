import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Subject } from "@/components/databaseManagement/subjects/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Subject>({
    mutationFn: async (Item: Subject) => {
      await axios.post("http://127.0.0.1:8000/api/subjectcrud/", Item);
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

  return useMutation<void, Error, Subject>({
    mutationFn: async (updatedItem: Subject) => {
      await axios.put(
        `http://127.0.0.1:8000/api/subjectcrud/${updatedItem.subject_code}/`,
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
      await axios.delete(`http://127.0.0.1:8000/api/subjectcrud/${Item}/`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error deleting items:", error);
    },
  });
}
