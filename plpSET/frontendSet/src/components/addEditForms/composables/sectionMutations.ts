import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Section } from "@/components/databaseManagement/sections/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Section>({
    mutationFn: async (Item: Section) => {
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/sectioncrud/",
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

  return useMutation<void, Error, Section>({
    mutationFn: async (updatedItem: Section) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/sectioncrud/${updatedItem.section_id}/`,
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
      await axios.delete(`http://127.0.0.1:8000/api/sectioncrud/${Item}/`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] });
    },
    onError: (error) => {
      console.error("Error deleting items:", error);
    },
  });
}
