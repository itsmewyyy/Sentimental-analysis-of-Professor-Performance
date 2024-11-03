<script setup lang="ts">
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle, SquarePlus } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Toaster } from "@/components/ui/toast";
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
import { ref } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { Admin } from "@/components/databaseManagement/admins/type";
import { CirclePlus } from "lucide-vue-next";
import { useAdd } from "./composables/adminMutations";
import axios from "axios";
import type { AxiosError } from "axios";

type ErrorResponse = {
  error?: string;
  [key: string]: string[] | string | undefined;
};

// Reuse `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: addData } = useAdd();

const adminId = ref("");
const adminUsername = ref("");
const passWord = ref("");
const isSecretary = ref(false);
const isDean = ref(false);
const isMIS = ref(false);
const dept = ref("");
const confirmpassword = ref("");
const position = ref("");

const submitForm = async () => {
  try {
    isDean.value = position.value === "dean";
    isSecretary.value = position.value === "secretary";

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

    const Data: Admin = {
      admin_acc_id: adminId.value,
      admin_username: adminUsername.value,
      password: passWord.value,
      confirm_password: confirmpassword.value,
      is_dean: isDean.value,
      is_mis: isMIS.value,
      is_secretary: isSecretary.value,
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
      onError: (error) => {
        const axiosError = error as AxiosError<ErrorResponse>;
        // Check if the error is a validation error from the server
        if (axiosError.response && axiosError.response.status === 400) {
          const errorData = axiosError.response.data;

          // Check for specific errors
          if (errorData.error) {
            // Handle custom error message like "Passwords do not match"
            toast({
              variant: "destructive",
              title: "Error",
              description: errorData.error,
            });
          } else {
            // Loop through field-specific errors
            Object.keys(errorData).forEach((field) => {
              const fieldError = errorData[field];

              // If fieldError is an array of strings, join them
              if (Array.isArray(fieldError)) {
                toast({
                  variant: "destructive",
                  title: "Error",
                  description: `${field}: ${fieldError.join(", ")}`,
                });
              } else if (typeof fieldError === "string") {
                // Handle single error string case
                toast({
                  variant: "destructive",
                  title: "Error",
                  description: `${field}: ${fieldError}`,
                });
              }
            });
          }
        } else {
          // Handle any unexpected errors
          toast({
            variant: "destructive",
            title: "Submission Error",
            description: error.message || "Failed to add. Please try again.",
          });
        }
        console.error("Submission Error:", error);
      },
    });
  } catch (error) {
    // Catch block for handling errors outside of the mutation (like the dept API call)
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
          <Label html-for="Admin-Id" class="text-xs">Admin ID</Label>
          <Input id="Admin-Id" type="" default-value="" v-model="adminId" />
        </div>
        <div class="grid gap-2">
          <Label html-for="username" class="text-xs">Username</Label>
          <Input id="username" default-value="" v-model="adminUsername" />
        </div>
        <div class="grid gap-2">
          <Label html-for="password" class="text-xs">Password</Label>
          <Input
            id="password"
            type="password"
            default-value=""
            v-model="passWord"
          />
        </div>
        <div class="grid gap-2">
          <Label html-for="cpassword" class="text-xs">Confirm Password</Label>
          <Input
            id="cpassword"
            type="password"
            default-value=""
            v-model="confirmpassword"
          />
        </div>
        <div class="grid gap-2">
          <Label for="college" class="text-xs">Department</Label>
          <Select class="sm:w-[300px]" v-model="dept">
            <SelectTrigger class="sm:w-full">
              <SelectValue placeholder="Select Department" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="CON" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="pink" fill="pink" />
                    College of Nursing (CON)
                  </span>
                </SelectItem>
                <SelectItem value="COE" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="orange" fill="orange" />
                    College of Engineering (COE)
                  </span>
                </SelectItem>
                <SelectItem value="CBA" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="yellow" fill="yellow" />
                    College of Business Administration (CBA)
                  </span>
                </SelectItem>
                <SelectItem value="COED" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="blue" fill="blue" />
                    College of Education (COED)
                  </span>
                </SelectItem>
                <SelectItem value="CAS" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="violet" fill="violet" />
                    College of Arts and Sciences (CAS)
                  </span>
                </SelectItem>
                <SelectItem value="CCS" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="grey" fill="grey" />
                    College of Computer Studies (CCS)
                  </span>
                </SelectItem>
                <SelectItem value="CIHM" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle class="w-3.5 h-3.5" color="red" fill="red" />
                    College of International Hospitality Management (CIHM)
                  </span>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <Label for="college" class="text-xs">Select Position</Label>
        <div class="grid gap-2">
          <RadioGroup class="flex space-x-4" v-model="position">
            <div class="flex items-center">
              <RadioGroupItem id="r1" value="dean" />
              <Label for="r1" class="ml-2">Dean</Label>
            </div>
            <div class="flex items-center">
              <RadioGroupItem id="r2" value="secretary" />
              <Label for="r2" class="ml-2">Secretary</Label>
            </div>
          </RadioGroup>
        </div>

        <Button type="submit" class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
          >Confirm</Button
        >
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
          <p>Add New Admin</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[505px]">
        <DialogHeader>
          <DialogTitle>New Admin</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new admin
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <Drawer v-else v-model:open="isOpen">
      <DrawerTrigger as-child> </DrawerTrigger>
      <DrawerContent>
        <DrawerHeader class="text-left">
          <DrawerTitle>New Admin</DrawerTitle>
          <DrawerDescription>
            Make changes to your profile here. Click save when you're done.
          </DrawerDescription>
        </DrawerHeader>
        <GridForm />
        <DrawerFooter class="pt-2">
          <DrawerClose as-child>
            <Button variant="outline"> Cancel </Button>
          </DrawerClose>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  </div>
</template>
