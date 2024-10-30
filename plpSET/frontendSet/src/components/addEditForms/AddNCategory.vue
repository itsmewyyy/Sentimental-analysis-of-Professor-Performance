<script setup lang="ts">
import { ref } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";
import axios from "axios";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { CirclePlus } from "lucide-vue-next";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAddCategory } from "./composables/categoryMutations";
import { Category } from "../databaseManagement/categories/type";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();

// Define reactive variables for form fields
const categoryId = ref("");
const categoryDesc = ref("");
const { mutate: addCategory } = useAddCategory();

const submitForm = () => {
  const categoryData: Category = {
    category_id: categoryId.value,
    category_desc: categoryDesc.value,
  };

  addCategory(categoryData, {
    onSuccess: () => {
      isOpen.value = false;
      toast({ title: "Success", description: "Category added successfully!" });
    },
    onError: (error) => {
      toast({ title: "Error", description: error.message || "Add failed." });
    },
  });
};
</script>

<template>
  <div>
    <!-- Reusable Form Template -->
    <UseTemplate>
      <form class="grid items-start gap-4 px-4" @submit.prevent="submitForm">
        <div class="grid gap-2">
          <Label html-for="category-id" class="text-xs">Category ID</Label>
          <Input id="category-id" default-value="" v-model="categoryId" />
          <p class="text-gray-500 ml-2 italic text-xs">e.g. A, B, C, D</p>
          <!-- Helper Text -->
        </div>
        <div class="grid gap-2">
          <Label html-for="category-description" class="text-xs"
            >Category Description</Label
          >
          <Input
            id="category-description"
            default-value=""
            v-model="categoryDesc"
          />
        </div>
        <Button
          type="submit"
          class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
        >
          Add Numerical Category
        </Button>
      </form>
    </UseTemplate>

    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger>
          <Button
            class="h-8 text-sm p-4 bg-plpgreen-200 hover:bg-plpgreen-400"
            @click="isOpen = true"
          >
            <CirclePlus class="mr-2 h-4 w-4" />
            <p>Add</p></Button
          >
        </TooltipTrigger>
        <TooltipContent>
          <p>Add New Category</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[505px]">
        <DialogHeader>
          <DialogTitle>New Category</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new Category
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <!-- Drawer for Mobile View -->
    <Drawer v-else v-model:open="isOpen">
      <DrawerTrigger as-child> </DrawerTrigger>
      <DrawerContent>
        <DrawerHeader class="text-left">
          <DrawerTitle>New Category</DrawerTitle>
          <DrawerDescription>Add a new category here</DrawerDescription>
        </DrawerHeader>
        <GridForm />
        <DrawerFooter class="pt-2">
          <DrawerClose as-child>
            <Button variant="outline">Cancel</Button>
          </DrawerClose>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  </div>
</template>
