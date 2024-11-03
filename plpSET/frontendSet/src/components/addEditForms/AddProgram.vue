<script setup lang="ts">
import { ref } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
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
import { Program } from "@/components/databaseManagement/programs/type";
import { CirclePlus } from "lucide-vue-next";
import { useAdd } from "./composables/programMutations";
import axios from "axios";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();

const { mutate: addData } = useAdd();

const programId = ref("");
const programdescription = ref("");
const dept = ref("");

const submitForm = async () => {
  try {
    const matchResponse = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/department-list/?department_id=${dept.value}`
    );

    const matchedData = matchResponse.data.find(
      (d) => d.department_id === dept.value
    );

    if (!matchedData) {
      throw new Error("No matching data found for the given value.");
    }

    const deptId = matchedData.department_id;

    const Data: Program = {
      program_id: programId.value,
      program_desc: programdescription.value,
      dept_id: deptId,
    };

    addData(Data, {
      onSuccess: () => {
        isOpen.value = false;
        toast({
          title: "Success",
          description: "Added successfully!",
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
          <Label html-for="program-code" class="text-xs">Program Code</Label>
          <Input id="program-code" default-value="" v-model="programId" />
          <p class="text-xs text-gray-500 ml-2 italic">e.g. BSCS, BSN, BSHM</p>
          <!-- Helper Text -->
        </div>
        <div class="grid gap-2">
          <Label html-for="program-description" class="text-xs"
            >Program Description</Label
          >
          <Input
            id="program-description"
            default-value=""
            v-model="programdescription"
          />
          <p class="text-xs text-gray-500 ml-2 italic">
            e.g. Bachelor of Science in Computer Science
          </p>
          <!-- Helper Text -->
        </div>
        <div class="grid gap-2">
          <Label html-for="college" class="text-xs">Department</Label>
          <Select class="sm:w-[300px]" v-model="dept">
            <SelectTrigger class="sm:w-full">
              <SelectValue placeholder="Select Department" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
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
          Add Program
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
          <p>Add New Program</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[505px]">
        <DialogHeader>
          <DialogTitle>New Program</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new program
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
          <DrawerTitle>New Program</DrawerTitle>
          <DrawerDescription>Add a new program here</DrawerDescription>
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
