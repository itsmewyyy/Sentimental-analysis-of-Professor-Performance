<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Circle } from "lucide-vue-next";
import { CirclePlus } from "lucide-vue-next";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
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
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import axios from "axios";
import { useAdd } from "./composables/professorMutations";
import { Professor } from "@/components/databaseManagement/professors/type";

// Reuse `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();

const { mutate: addData } = useAdd();

const professorId = ref("");
const department = ref("");
const surname = ref("");
const middleName = ref("");
const firstName = ref("");
const extenstionName = ref("");
const status = ref("");
const isdean = ref(false);

const submitForm = async () => {
  try {
    const DataResponse = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/department-list/?department_id=${department.value}`
    );
    const statusResponse = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/professor-status/?professor_status_id=${status.value}`
    );

    const matchedData = DataResponse.data.find(
      (d) => d.department_id === department.value
    );
    const matchedStatus = statusResponse.data.find(
      (st) => st.professor_status_id === status.value
    );

    const departmentId = matchedData.department_id;
    const statusId = matchedStatus.professor_status_id;

    const Data: Professor = {
      full_name: null,
      department_desc: null,
      professor_id: professorId.value,
      surname: surname.value,
      department: departmentId,
      middle_name: middleName.value,
      first_name: firstName.value,
      is_dean: isdean.value,
      status: statusId,
      extension_name: extenstionName.value,
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
        <!-- Group 1: Professor ID, Status (Responsive) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <Label for="professor-id" class="text-xs">Professor ID</Label>
            <Input
              id="professor-id"
              default-value=""
              class="w-full"
              v-model="professorId"
            />
          </div>
          <div>
            <Label for="status" class="text-xs">Status</Label>
            <Select class="w-full" v-model="status">
              <SelectTrigger class="w-full">
                <SelectValue placeholder="Select Status" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Status</SelectLabel>
                  <SelectItem value="FT">
                    <div class="flex items-center gap-2">
                      <Circle
                        class="w-3.5 h-3.5"
                        color="yellow"
                        fill="yellow"
                      />
                      <span>Full Time</span>
                    </div>
                  </SelectItem>
                  <SelectItem value="PT">
                    <div class="flex items-center gap-2">
                      <Circle class="w-3.5 h-3.5" color="grey" fill="grey" />
                      <span>Part Time</span>
                    </div>
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
        </div>

        <!-- Group 2: Surname, Middle Name, First Name, Extension Name -->
        <div class="grid grid-cols-1 sm:grid-cols-4 gap-16">
          <div>
            <Label for="surname" class="text-xs">Surname</Label>
            <Input
              id="surname"
              default-value=""
              class="w-[160px]"
              v-model="surname"
            />
          </div>
          <div>
            <Label for="middle-name" class="text-xs">Middle Name</Label>
            <Input
              id="middle-name"
              default-value=""
              class="w-[160px]"
              v-model="middleName"
            />
          </div>
          <div>
            <Label for="firstname" class="text-xs">Firstname</Label>
            <Input
              id="firstname"
              default-value=""
              class="w-[160px]"
              v-model="firstName"
            />
          </div>
          <div class="flex items-start">
            <div class="w-full">
              <Label for="extension-name" class="text-xs">Extension Name</Label>
              <Input
                id="extension-name"
                default-value=""
                class="w-full"
                v-model="extenstionName"
              />
            </div>
          </div>
        </div>

        <!-- Group 3: Department -->
        <div>
          <Label for="department" class="text-xs">Department</Label>
          <Select class="w-full" v-model="department">
            <SelectTrigger class="w-full">
              <SelectValue placeholder="Select Department" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="CON">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="pink" fill="pink" />
                    <span>College of Nursing (CON)</span>
                  </div>
                </SelectItem>
                <SelectItem value="COE">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="orange" fill="orange" />
                    <span>College of Engineering (COE)</span>
                  </div>
                </SelectItem>
                <SelectItem value="CBA">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="yellow" fill="yellow" />
                    <span>College of Business Administration (CBA)</span>
                  </div>
                </SelectItem>
                <SelectItem value="COED">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="blue" fill="blue" />
                    <span>College of Education (COED)</span>
                  </div>
                </SelectItem>
                <SelectItem value="CAS">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="violet" fill="violet" />
                    <span>College of Arts and Sciences (CAS)</span>
                  </div>
                </SelectItem>
                <SelectItem value="CCS">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="grey" fill="grey" />
                    <span>College of Computer Studies (CCS)</span>
                  </div>
                </SelectItem>
                <SelectItem value="CIHM">
                  <div class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="red" fill="red" />
                    <span
                      >College of International Hospitality Management
                      (CIHM)</span
                    >
                  </div>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>

        <!-- Checkbox: Assign as Dean -->
        <div class="flex items-center gap-2">
          <Checkbox
            id="terms1"
            :checked="isdean"
            @update:checked="(newValue) => (isdean = newValue)"
          />
          <div class="leading-none">
            <label
              for="terms1"
              class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
            >
              Assign as Dean
            </label>
            <p class="text-xs text-darks-200/80">
              Check this box if the professor is being added as a Dean.
            </p>
          </div>
        </div>

        <Button
          type="submit"
          class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
        >
          Add Professor
        </Button>
      </form>
    </UseTemplate>

    <!-- Add Professor Button with Tooltip (triggers form) -->
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
          <p>Add Professor</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogContent class="sm:max-w-[700px]">
        <DialogHeader>
          <DialogTitle>Add Professor</DialogTitle>
          <DialogDescription>
            Enter Professor Information Below. Review and Confirm the Details
            Before Adding.
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <!-- Drawer for Mobile View -->
    <Drawer v-else v-model:open="isOpen">
      <DrawerContent>
        <DrawerHeader>
          <DrawerTitle>Add Professor</DrawerTitle>
          <DrawerDescription>
            Enter Professor Information Below.
          </DrawerDescription>
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
