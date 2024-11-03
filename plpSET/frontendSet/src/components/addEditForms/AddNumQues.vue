<script setup lang="ts">
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
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
import { useAdd } from "./composables/numquestionMutations";
import { NumQuestion } from "@/components/databaseManagement/numericalQuestions/type";
import axios from "axios";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: addData } = useAdd();

const numquestionId = ref("");
const questioncategory = ref("dsads");
const question = ref("");
const categories = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/numerical-categories/"
    );
    categories.value = response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
  }
});

const submitForm = async () => {
  try {
    const matchResponse = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/numerical-categories/?category_id=${questioncategory.value}`
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

    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger>
          <Button
            class="h-8 text-sm p-4 bg-plpgreen-200 hover:bg-plpgreen-400"
            @click="isOpen = true"
          >
            <CirclePlus class="mr-2 h-4 w-4" />
            <p>Add</p>
          </Button>
        </TooltipTrigger>
        <TooltipContent>
          <p>Add Question to Database</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

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
