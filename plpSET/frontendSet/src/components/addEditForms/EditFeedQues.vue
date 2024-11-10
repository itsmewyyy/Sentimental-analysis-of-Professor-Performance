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
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Pencil } from "lucide-vue-next";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FeedbackQuestion } from "@/components/databaseManagement/feedbackquestions/type";
import axios from "axios";
import { useEdit } from "./composables/feedbackquestionMutations";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
const { mutate: Edit } = useEdit();

const feedbackquestionId = ref("");
const question = ref("");

const fetchInfo = async () => {
  try {
    const response = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/feedback-questioncrud/${feedbackquestionId.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      // Set the values to the reactive variables
      feedbackquestionId.value = info.feedback_question_id || "";
      question.value = info.question || "";
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
  const savedItem = localStorage.getItem("question_id");
  if (savedItem) {
    feedbackquestionId.value = savedItem;
    fetchInfo();
  }
});

const submitForm = () => {
  const Data: FeedbackQuestion = {
    feedback_question_id: feedbackquestionId.value,
    question: question.value,
  };

  Edit(Data, {
    onSuccess: () => {
      isOpen.value = false;
      toast({
        title: "Success",
        description: "Feedback question updated successfully!",
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
