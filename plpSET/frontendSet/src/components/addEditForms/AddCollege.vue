<script setup lang="ts">
import { ref } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { Button } from "@/components/ui/button";
import { useToast } from "@/components/ui/toast/use-toast";
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
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Input } from "@/components/ui/input";
import { CirclePlus } from "lucide-vue-next";
import { Label } from "@/components/ui/label";
import { useAdd } from "./composables/collegeMutations";
import { Department } from "@/components/databaseManagement/colleges/type";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();

const { mutate: Add } = useAdd();

const departmentId = ref("");
const description = ref("");

const submitForm = () => {
  const Data: Department = {
    department_id: departmentId.value,
    department_desc: description.value,
  };

  Add(Data, {
    onSuccess: () => {
      isOpen.value = false;
      toast({
        title: "Success",
        description: "Department added successfully!",
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
          <Label html-for="department-code" class="text-xs"
            >Department Code</Label
          >
          <Input id="department-code" default-value="" v-model="departmentId" />
          <p class="text-xs text-gray-500 ml-2 italic">e.g. CCS, CON, CBA</p>
          <!-- Helper Text -->
        </div>
        <div class="grid gap-2">
          <Label html-for="department-description" class="text-xs"
            >Department Description</Label
          >
          <Input
            id="department-description"
            default-value=""
            v-model="description"
          />
          <p class="text-xs text-gray-500 ml-2 italic">
            e.g. College of Computer Studies, College of Nursing
          </p>
          <!-- Helper Text -->
        </div>

        <Button
          type="submit"
          class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
        >
          Add Department
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
          <p>Add New College</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[505px]">
        <DialogHeader>
          <DialogTitle>New Department</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new department
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
          <DrawerTitle>New Department</DrawerTitle>
          <DrawerDescription>Add a new department here</DrawerDescription>
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
