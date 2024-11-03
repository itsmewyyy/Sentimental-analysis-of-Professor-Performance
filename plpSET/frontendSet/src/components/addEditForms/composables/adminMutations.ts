import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Admin } from "@/components/databaseManagement/admins/type";
import axios from "axios";

export function useAdd() {
  const queryClient = useQueryClient();

  return useMutation<void, Error, Admin>({
    mutationFn: async (Item: Admin) => {
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/admininfocrud/",
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

  return useMutation<void, Error, Admin>({
    mutationFn: async (updatedItem: Admin) => {
      await axios.put(
        `https://sentiment-professor-feedback-1.onrender.com/api/admininfocrud/${updatedItem.admin_acc_id}/`,
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
        `https://sentiment-professor-feedback-1.onrender.com/api/admininfocrud/${Item}/`
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
