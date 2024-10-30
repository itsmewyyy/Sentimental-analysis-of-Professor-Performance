import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Student } from "@/components/databaseStudent/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Student>({
    mutationFn: async (Item: Student) => {
      await axios.post("http://127.0.0.1:8000/api/students/", Item);
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

  return useMutation<void, Error, Student>({
    mutationFn: async (updatedItem: Student) => {
      await axios.put(
        `http://127.0.0.1:8000/api/students/${updatedItem.student_id}/`,
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
      await axios.delete(`http://127.0.0.1:8000/api/students/${Item}/`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error deleting items:", error);
    },
  });
}
