<script setup lang="ts">
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { Pencil } from "lucide-vue-next";
import { Circle } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Subject } from "@/components/databaseManagement/subjects/type";
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
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useEdit } from "./composables/subjectMutations";
import axios from "axios";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: editData } = useEdit();

const subjectCode = ref("");
const subjectDesc = ref("");
const assocCollege = ref("");

const fetchInfo = async () => {
  try {
    const response = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/subjectcrud/${subjectCode.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      // Set the values to the reactive variables
      subjectCode.value = info.subject_code || "";
      subjectDesc.value = info.subject_desc || "";
      assocCollege.value = info.assoc_college || "";
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
  const savedItem = localStorage.getItem("subject");
  if (savedItem) {
    subjectCode.value = savedItem;
    fetchInfo();
  }
});

const submitForm = async () => {
  try {
    const matchResponse = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/department-list/?department_id=${assocCollege.value}`
    );

    const matchedData = matchResponse.data.find(
      (d) => d.department_id === assocCollege.value
    );

    if (!matchedData) {
      throw new Error("No matching data found for the given value.");
    }

    const deptId = matchedData.department_id;

    const Data: Subject = {
      subject_code: subjectCode.value,
      subject_desc: subjectDesc.value,
      assoc_college: deptId,
    };

    editData(Data, {
      onSuccess: () => {
        isOpen.value = false;
        toast({
          title: "Success",
          description: "Subject updated successfully!",
        });
      },
    });
  } catch (error) {
    toast({
      title: "Submission Error",
      description: error.message || "Failed to add. Please try again.",
    });
    console.error("Submission Error:", error);
  }
};
</script>

<template>
  <div>
    <!-- Reusable Form Template -->
    <UseTemplate>
      <form class="grid items-start gap-4 px-4" @submit.prevent="submitForm">
        <div class="grid gap-2">
          <Label html-for="subject-code" class="text-xs">Subject Code</Label>
          <Input
            id="subject-code"
            default-value="GE001"
            v-model="subjectCode"
          />
          <p class="text-xs text-gray-500 ml-2 italic">e.g. GE001, GE002</p>
          <!-- Helper Text -->
        </div>
        <div class="grid gap-2">
          <Label html-for="subject-description" class="text-xs"
            >Subject Description</Label
          >
          <Input
            id="subject-description"
            default-value=""
            v-model="subjectDesc"
          />
        </div>
        <div class="grid gap-2">
          <Label html-for="college" class="text-xs">Department</Label>
          <Select class="sm:w-[300px]" v-model="assocCollege">
            <SelectTrigger class="sm:w-full">
              <SelectValue placeholder="Select Department" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel></SelectLabel>
                <SelectItem value="CON">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="pink" fill="pink" />
                    College of Nursing (CON)
                  </div>
                </SelectItem>
                <SelectItem value="COE">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="orange" fill="orange" />
                    College of Engineering (COE)
                  </div>
                </SelectItem>
                <SelectItem value="CBA">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="yellow" fill="yellow" />
                    College of Business Administration (CBA)
                  </div>
                </SelectItem>
                <SelectItem value="COED">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="blue" fill="blue" />
                    College of Education (COED)
                  </div>
                </SelectItem>
                <SelectItem value="CAS">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="violet" fill="violet" />
                    College of Arts and Sciences (CAS)
                  </div>
                </SelectItem>
                <SelectItem value="CCS">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="grey" fill="grey" />
                    College of Computer Studies (CCS)
                  </div>
                </SelectItem>
                <SelectItem value="CIHM">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="red" fill="red" />
                    College of International Hospitality Management (CIHM)
                  </div>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <Button
          type="submit"
          class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
        >
          Add Subject
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
          <DialogTitle>New Subject</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new subject
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
          <DrawerTitle>New Subject</DrawerTitle>
          <DrawerDescription>Add a new subject here</DrawerDescription>
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
