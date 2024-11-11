<script setup lang="ts">
import type { Row } from "@tanstack/vue-table";
import type { FeedbackQuestion } from "./type";
import { Pencil } from "lucide-vue-next";
import { Trash } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Ellipsis } from "lucide-vue-next";
import { computed } from "vue";
import EditFeedQues from "@/components/addEditForms/EditFeedQues.vue";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

interface DataTableRowActionsProps {
  row: Row<FeedbackQuestion>;
}

const props = defineProps<DataTableRowActionsProps>();

const emit = defineEmits(["delete", "storeItem"]);

const deleteRow = () => {
  emit("delete", props.row.original);
};

const storeItems = () => {
  emit("storeItem", props.row.original);
};
</script>

<template>
  <TooltipProvider>
    <Tooltip>
      <TooltipTrigger as-child>
        <Button
          variant="ghost"
          class="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
        >
          <DropdownMenu>
            <DropdownMenuTrigger as-child @click="storeItems">
              <Ellipsis class="h-4 w-4" />
            </DropdownMenuTrigger>
            <DropdownMenuContent align="center" class="w-[160px]">
              <DropdownMenuItem>
                <EditFeedQues></EditFeedQues>
              </DropdownMenuItem>
              <DropdownMenuItem @click.stop>
                <AlertDialog>
                  <AlertDialogTrigger @click.stop
                    ><div
                      class="flex flex-row justify-between items-center cursor-pointer"
                    >
                      <p>Delete</p>
                      <Trash color="red" width="12" class="ml-20" />
                    </div>
                  </AlertDialogTrigger>
                  <AlertDialogContent>
                    <AlertDialogHeader>
                      <AlertDialogTitle
                        >Are you absolutely sure?</AlertDialogTitle
                      >
                      <AlertDialogDescription>
                        This action cannot be undone. This will delete the
                        selected Feedback Question.
                      </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                      <AlertDialogCancel>Cancel</AlertDialogCancel>
                      <AlertDialogAction
                        @click="deleteRow"
                        class="bg-plpgreen-200 hover:bg-plpgreen-300"
                        >Continue</AlertDialogAction
                      >
                    </AlertDialogFooter>
                  </AlertDialogContent>
                </AlertDialog>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <span class="sr-only">Open menu</span>
        </Button>
      </TooltipTrigger>
      <TooltipContent>
        <p>Actions</p>
      </TooltipContent>
    </Tooltip>
  </TooltipProvider>
</template>
