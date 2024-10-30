<script setup lang="ts">
import type { Row } from "@tanstack/vue-table";
import type { Subject } from "./columns";
import { Pencil } from 'lucide-vue-next';
import { Trash } from 'lucide-vue-next';
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
import { Ellipsis } from "lucide-vue-next";
import { computed } from "vue";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger
} from '@/components/ui/tooltip'

interface DataTableRowActionsProps {
  row: Row<Subject>;
}

const props = defineProps<DataTableRowActionsProps>();
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
            <DropdownMenuTrigger as-child>
              <Ellipsis class="h-4 w-4" />
            </DropdownMenuTrigger>
            <DropdownMenuContent align="center" class="w-[160px]">
              <DropdownMenuItem class="flex justify-between items-center">
                Edit
                <Pencil color="green" width="12" />
              </DropdownMenuItem>
              <DropdownMenuItem class="flex justify-between items-center">
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
