<script setup lang="ts">
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
import { Pencil } from "lucide-vue-next";
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
import { useEdit } from "./composables/programMutations";
import axios from "axios";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: editData } = useEdit();

const programId = ref("");
const programdescription = ref("");
const dept = ref("");

const fetchInfo = async () => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/programcrud/${programId.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      // Set the values to the reactive variables
      programId.value = info.program_id || "";
      programdescription.value = info.program_desc || "";
      dept.value = info.dept_id || "";
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
  const savedItem = localStorage.getItem("program");
  if (savedItem) {
    programId.value = savedItem;
    fetchInfo();
  }
});

const submitForm = async () => {
  try {
    const matchResponse = await axios.get(
      `http://127.0.0.1:8000/api/department-list/?department_id=${dept.value}`
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

    editData(Data, {
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
