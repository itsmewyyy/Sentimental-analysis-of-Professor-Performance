<script setup lang="ts">
import { useAdd } from "@/components/addEditForms/composables/studentMutations";
import { useToast } from "@/components/ui/toast/use-toast";
import * as XLSX from "xlsx";
import axios from "axios";
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { Button } from "@/components/ui/button";
import { FileUp } from "lucide-vue-next";
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
import { PinInputInput } from "radix-vue";

const { toast } = useToast();
const [UseTemplate, GridForm] = createReusableTemplate();
const { mutate: addData } = useAdd();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);

const studentId = ref("");
const section = ref("");
const surname = ref("");
const middleName = ref("");
const firstName = ref("");
const extensionName = ref("");
const status = ref("Regular");

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    loadExcelFile(file);
  }
};

const loadExcelFile = (file) => {
  const reader = new FileReader();

  reader.onload = (e) => {
    if (e.target.result instanceof ArrayBuffer) {
      const data = new Uint8Array(e.target.result); // Ensure ArrayBuffer
      const workbook = XLSX.read(data, { type: "array" }); // Process data as array

      const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
      const rows = XLSX.utils.sheet_to_json(firstSheet, { header: 1 });

      const toTitleCase = (str) => {
        return str
          .toLowerCase()
          .split(" ")
          .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
          .join(" ");
      };

      rows.slice(1).forEach((row) => {
        const studentData = {
          studentId: row[0],
          surname: toTitleCase(row[1]),
          firstName: toTitleCase(row[2]),
          middleName: row[3] ? toTitleCase(row[3]) : "",
          extensionName: row[4] ? toTitleCase(row[4]) : "",
        };

        // Submit each row's data
        submitForm(studentData);
      });
    } else {
      console.error("File read result is not an ArrayBuffer");
    }
  };

  reader.onerror = (error) => {
    console.error("File reading error:", error);
  };

  reader.readAsArrayBuffer(file); // Read the file as ArrayBuffer
};

const submitForm = async (studentData) => {
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

    const sectionId = matchedSection ? matchedSection.section_id : null;
    const statusId = matchedStatus ? matchedStatus.student_status_id : null;

    const Data = {
      full_name: null,
      student_id: studentData.studentId,
      section: sectionId,
      surname: studentData.surname,
      middle_name: studentData.middleName,
      first_name: studentData.firstName,
      extension_name: studentData.extensionName,
      status: statusId,
    };

    addData(Data, {
      onSuccess: () => {
        toast({
          title: "Success",
          description: "Students added successfully!",
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

onMounted(() => {
  const savedSection = localStorage.getItem("section");
  if (savedSection) {
    section.value = savedSection;
  }
});
</script>

<template>
  <div>
    <UseTemplate>
      <form class="items-center px-4" @submit.prevent="submitForm">
        <Input
          type="file"
          @change="handleFileUpload"
          class="px-12 pb-20 pt-10 w-full"
        />
      </form>
    </UseTemplate>

    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger>
          <Button
            class="items-center space-x-2 bg-plpgreen-200 hover:bg-plpgreen-400"
            @click="isOpen = true"
            ><FileUp class="w-5 h-5" />
            <p>Upload</p>
          </Button>
        </TooltipTrigger>
        <TooltipContent>
          <p>Upload Students</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogContent class="sm:max-w-[700px]">
        <DialogHeader>
          <DialogTitle>Upload Students</DialogTitle>
          <DialogDescription>
            Upload Students from Class List
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <Drawer v-else v-model:open="isOpen">
      <DrawerContent>
        <DrawerHeader>
          <DrawerTitle>Upload Students</DrawerTitle>
          <DrawerDescription>Upload Students from Class List</DrawerDescription>
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
