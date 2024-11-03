<script setup lang="ts">
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Pencil } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { useToast } from "@/components/ui/toast/use-toast";
import { Textarea } from "@/components/ui/textarea";
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
import { CirclePlus } from "lucide-vue-next";
import { useEdit } from "./composables/numquestionMutations";
import { NumQuestion } from "@/components/databaseManagement/numericalQuestions/type";
import axios from "axios";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: EditData } = useEdit();

const numquestionId = ref("");
const questioncategory = ref("dsads");
const question = ref("");
const categories = ref([]);

const fetchData = async () => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/numerical-questioncrud/${numquestionId.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      numquestionId.value = info.numerical_question_id || "";
      questioncategory.value = info.category || "";
      question.value = info.question || "";
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    toast({
      title: "Error",
      description: "Failed to fetch data.",
    });
  }
};

onMounted(async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/numerical-categories/"
    );
    categories.value = response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
  }

  const savedData = localStorage.getItem("question_id");
  if (savedData) {
    numquestionId.value = savedData;
    fetchData();
  }
});

const submitForm = async () => {
  try {
    const matchResponse = await axios.get(
      `http://127.0.0.1:8000/api/numerical-categories/?category_id=${questioncategory.value}`
    );

    const matchedData = matchResponse.data.find(
      (c) => c.category_id === questioncategory.value
    );

    if (!matchedData) {
      throw new Error("No matching section found for the given value.");
    }

    const categoryId = matchedData.category_id;

    const Data: NumQuestion = {
      numerical_question_id: numquestionId.value,
      question: question.value,
      category: categoryId,
    };

    EditData(Data, {
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
    <UseTemplate>
      <form class="grid items-start gap-4 px-4" @submit.prevent="submitForm">
        <div class="grid gap-2">
          <Label html-for="numerical-question-id" class="text-xs">
            Numerical Question ID
          </Label>
          <Input
            id="numerical-question-id"
            default-value=""
            v-model="numquestionId"
          />
        </div>
        <div class="grid gap-2">
          <Label html-for="category" class="text-xs">Category</Label>
          <Select class="sm:w-[300px]" v-model="questioncategory">
            <SelectTrigger class="sm:w-full">
              <SelectValue placeholder="Select Category" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Categories</SelectLabel>
                <SelectItem
                  v-for="(cat, index) in categories"
                  :key="index"
                  :value="cat.category_id"
                >
                  <div class="flex items-center gap-2">
                    {{ cat.category_id }}
                  </div>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <div class="grid w-full gap-1.5">
          <Label for="message-2">New Question</Label>
          <Textarea
            id="message-2"
            placeholder="Type your question here."
            v-model="question"
          />
        </div>
        <Button
          type="submit"
          class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
        >
          Add Question
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
      <DialogTrigger as-child />
      <DialogContent class="sm:max-w-[600px]">
        <DialogHeader>
          <DialogTitle>Add Question</DialogTitle>
          <DialogDescription>
            Please enter the information for the new question.
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <!-- Drawer for Mobile View -->
    <Drawer v-else v-model:open="isOpen">
      <DrawerTrigger as-child />
      <DrawerContent>
        <DrawerHeader class="text-left">
          <DrawerTitle>Add Question</DrawerTitle>
          <DrawerDescription>Add a new question here.</DrawerDescription>
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
