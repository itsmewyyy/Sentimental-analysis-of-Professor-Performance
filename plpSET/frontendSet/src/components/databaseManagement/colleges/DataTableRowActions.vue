<script setup lang="ts">
import type { Row } from "@tanstack/vue-table";
import type { Department } from "./type";
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
import { Pencil } from "lucide-vue-next";
import { Trash } from "lucide-vue-next";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Ellipsis } from "lucide-vue-next";
import { computed } from "vue";
import editCollege from "@/components/addEditForms/editCollege.vue";

interface DataTableRowActionsProps {
  row: Row<Department>;
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
                <editCollege></editCollege>
              </DropdownMenuItem>
              <DropdownMenuItem
                class="flex justify-between items-center cursor-pointer"
                @click="deleteRow"
              >
                Delete
                <Trash color="red" width="12" />
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
