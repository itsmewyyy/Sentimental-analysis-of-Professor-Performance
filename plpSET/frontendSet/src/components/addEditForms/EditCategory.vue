<script setup lang="ts">
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
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
import { Pencil } from "lucide-vue-next";
import { useEditCategory } from "./composables/categoryMutations";
import type { Category } from "@/components/databaseManagement/categories/type";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: editCategory } = useEditCategory();

// Define reactive variables for form fields
const categoryId = ref("");
const categoryDesc = ref("");

const fetchInfo = async () => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/categorycrud/${categoryId.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      // Set the values to the reactive variables
      categoryId.value = info.category_id || "";
      categoryDesc.value = info.category_desc || "";
    }
  } catch (error) {
    console.error("Error fetching category:", error);
    toast({
      title: "Error",
      description: "Failed to fetch category.",
    });
  }
};

onMounted(() => {
  const savedItem = localStorage.getItem("category");
  if (savedItem) {
    categoryId.value = savedItem;
    fetchInfo();
  }
});

const submitForm = () => {
  const categoryData: Category = {
    category_id: categoryId.value,
    category_desc: categoryDesc.value,
  };

  editCategory(categoryData, {
    onSuccess: () => {
      isOpen.value = false;
      toast({
        title: "Success",
        description: "Category updated added successfully!",
      });
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
          Update Numerical Category
        </Button>
      </form>
    </UseTemplate>

    <Button
      type="button"
      class="h-6 border-none bg-transparent hover:bg-transparent w-[160px] flex items-center"
      @click="isOpen = true"
      @click.stop
    >
      <div class="relative flex items-center">
        <p class="text-sm text-darks-900 absolute right-12 mr-2">Edit</p>

        <Pencil color="green" width="12" class="absolute left-9 ml-1.5" />
      </div>
    </Button>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[505px]">
        <DialogHeader>
          <DialogTitle>Update Category</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the Category.
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
          <DrawerTitle>Update Category</DrawerTitle>
          <DrawerDescription
            >Enter the information for the Category.</DrawerDescription
          >
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
