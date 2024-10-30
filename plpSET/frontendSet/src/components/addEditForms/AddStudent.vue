<script setup lang="ts">
import { Circle, SquarePlus } from "lucide-vue-next";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";
import { Button } from "@/components/ui/button";
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
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import axios from "axios";
import { CirclePlus } from "lucide-vue-next";
import type { Student } from "@/components/databaseStudent/type";
import { useAdd } from "@/components/addEditForms/composables/studentMutations";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: addData } = useAdd();

const studentId = ref("21-00000");
const section = ref("");
const surname = ref("");
const middleName = ref("");
const firstName = ref("");
const extensionName = ref("");
const status = ref("");

onMounted(() => {
  const savedSection = localStorage.getItem("section");
  if (savedSection) {
    section.value = savedSection;
  }
});

const submitForm = async () => {
  try {
    const sectionResponse = await axios.get(
      `http://127.0.0.1:8000/api/section-list/?section_id=${section.value}`
    );
    const statusResponse = await axios.get(
      `http://127.0.0.1:8000/api/student-status/?student_status_desc=${status.value}`
    );

    const matchedSection = sectionResponse.data.find(
      (s) => s.section_id === section.value
    );
    const matchedStatus = statusResponse.data.find(
      (st) => st.student_status_desc === status.value
    );

    const sectionId = matchedSection.section_id;
    const statusId = matchedStatus.student_status_id;

    const Data: Student = {
      full_name: null,
      student_id: studentId.value,
      section: sectionId, // Send the section ID
      surname: surname.value,
      middle_name: middleName.value,
      first_name: firstName.value,
      extension_name: extensionName.value,
      status: statusId, // Send the status ID
    };

    addData(Data, {
      onSuccess: () => {
        isOpen.value = false;
        toast({
          title: "Success",
          description: "Student added successfully!",
        });
      },
    });
  } catch (error) {
    toast({
      title: "Submission Error",
      description: error.message || "Failed to add student. Please try again.",
    });
    console.error("Submission Error:", error);
  }
};
</script>

<template>
  <div>
    <UseTemplate>
      <!-- Form template with @submit.prevent to call submitForm -->
      <form class="grid items-start gap-4 px-4" @submit.prevent="submitForm">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <Label for="student-id" class="text-xs">Student ID</Label>
            <Input id="student-id" v-model="studentId" class="w-full" />
          </div>
          <div>
            <Label for="section" class="text-xs">Section Code</Label>
            <Input id="section" v-model="section" class="w-full" />
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-4 gap-16">
          <div>
            <Label for="surname" class="text-xs">Surname</Label>
            <Input id="surname" v-model="surname" class="w-[160px]" />
          </div>
          <div>
            <Label for="middle-name" class="text-xs">Middle Name</Label>
            <Input id="middle-name" v-model="middleName" class="w-[160px]" />
          </div>
          <div>
            <Label for="firstname" class="text-xs">Firstname</Label>
            <Input id="firstname" v-model="firstName" class="w-[160px]" />
          </div>
          <div class="flex items-start">
            <div class="w-full">
              <Label for="extension-name" class="text-xs">Extension Name</Label>
              <Input
                id="extension-name"
                v-model="extensionName"
                class="w-full"
              />
            </div>
          </div>
        </div>

        <div>
          <Label for="department" class="text-xs">Status</Label>
          <Select v-model="status" class="w-full">
            <SelectTrigger class="w-full">
              <SelectValue placeholder="Select Status" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="Regular">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="green" fill="green" />
                    <span>Regular</span>
                  </div>
                </SelectItem>
                <SelectItem value="Irregular">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="yellow" fill="yellow" />
                    <span>Irregular</span>
                  </div>
                </SelectItem>
                <SelectItem value="Leave of Absence">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="grey" fill="grey" />
                    <span>Leave of Absence (LOA)</span>
                  </div>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>

        <Button type="submit" class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
          >Add Student</Button
        >
      </form>
    </UseTemplate>

    <!-- Tooltip and dialog/drawer components remain as-is -->
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
          <p>Add Student to Library</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogContent class="sm:max-w-[700px]">
        <DialogHeader>
          <DialogTitle>Add Student</DialogTitle>
          <DialogDescription>
            Enter Student Information Below. Review and Confirm the Details
            Before Adding.
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <Drawer v-else v-model:open="isOpen">
      <DrawerContent>
        <DrawerHeader>
          <DrawerTitle>Add Student</DrawerTitle>
          <DrawerDescription
            >Enter Student Information Below.</DrawerDescription
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
