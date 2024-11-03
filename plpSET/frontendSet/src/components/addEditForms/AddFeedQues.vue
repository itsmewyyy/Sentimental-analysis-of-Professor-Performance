<script setup lang="ts">
import { ref } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Toaster } from "@/components/ui/toast";
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
import { CirclePlus } from "lucide-vue-next";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAdd } from "./composables/feedbackquestionMutations";
import { FeedbackQuestion } from "@/components/databaseManagement/feedbackquestions/type";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: Add } = useAdd();

const feedbackquestionId = ref("");
const question = ref("");

const submitForm = () => {
  const Data: FeedbackQuestion = {
    feedback_question_id: feedbackquestionId.value,
    question: question.value,
  };

  Add(Data, {
    onSuccess: () => {
      isOpen.value = false;
      toast({
        title: "Success",
        description: "Feedback question added successfully!",
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
    <Toaster />

    <!-- Reusable Form Template -->
    <UseTemplate>
      <form class="grid items-start gap-4 px-4" @submit.prevent="submitForm">
        <div class="grid gap-2">
          <Label html-for="feedback-question-id" class="text-xs"
            >Feedback Question ID</Label
          >
          <Input
            id="feedback-question-id"
            default-value=""
            v-model="feedbackquestionId"
          />
        </div>
        <div class="grid w-full gap-1.5">
          <Label for="message-2">Question</Label>
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
          Add Feedback Question
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
          <p>Add New Feedback Question</p>
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
            To get started, please enter the information for the new question.
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
