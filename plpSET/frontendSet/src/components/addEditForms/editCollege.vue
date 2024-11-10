<script setup lang="ts">
import { ref, onMounted } from "vue";
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
import { Pencil } from "lucide-vue-next";
import { Label } from "@/components/ui/label";
import { useEdit } from "./composables/collegeMutations";
import { Department } from "@/components/databaseManagement/colleges/type";
import axios from "axios";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();

const { mutate: Edit } = useEdit();

const departmentId = ref("");
const description = ref("");

const fetchInfo = async () => {
  try {
    const response = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/collegecrud/${departmentId.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      // Set the values to the reactive variables
      departmentId.value = info.department_id || "";
      description.value = info.department_desc || "";
    }
  } catch (error) {
    console.error("Error fetching:", error);
    toast({
      title: "Error",
      description: "Failed to fetch.",
    });
  }
};

onMounted(() => {
  const savedItem = localStorage.getItem("college");
  if (savedItem) {
    departmentId.value = savedItem;
    fetchInfo();
  }
});

const submitForm = () => {
  const Data: Department = {
    department_id: departmentId.value,
    department_desc: description.value,
  };

  Edit(Data, {
    onSuccess: () => {
      isOpen.value = false;
      toast({
        title: "Success",
        description: "College updated successfully!",
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
