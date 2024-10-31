<script setup lang="ts">
import type { Column } from "@tanstack/vue-table";
import type { Student } from "./type";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { cn } from "@/lib/utils";
import { ChevronDown } from "lucide-vue-next";
import { ChevronUp } from "lucide-vue-next";
import { ArrowDownUp } from "lucide-vue-next";

interface DataTableColumnHeaderProps {
  column: Column<Student, any>;
  title: string;
}

defineProps<DataTableColumnHeaderProps>();
</script>

<script lang="ts">
export default {
  inheritAttrs: false,
};
</script>

<template>
  <div
    v-if="column.getCanSort()"
    :class="cn('text-center', $attrs.class ?? '')"
  >
    <DropdownMenu>
      <DropdownMenuTrigger as-child>
        <Button
          variant="ghost"
          size="sm"
          class="ml-2 h-8 data-[state=open]:bg-accent text-xs"
        >
          <span>{{ title }}</span>
          <ChevronDown
            v-if="column.getIsSorted() === 'desc'"
            class="ml-2 h-4 w-4"
          />
          <ChevronUp
            v-else-if="column.getIsSorted() === 'asc'"
            class="ml-2 h-2 w-2"
          />
          <ArrowDownUp v-else class="ml-2 h-2.5 w-2.5" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="center">
        <DropdownMenuItem @click="column.toggleSorting(false)">
          <ChevronUp class="mr-2 h-3.5 w-3.5 text-muted-foreground/70" />
          Asc
        </DropdownMenuItem>
        <DropdownMenuItem @click="column.toggleSorting(true)">
          <ChevronDown class="mr-2 h-3.5 w-3.5 text-muted-foreground/70" />
          Desc
        </DropdownMenuItem>
        <DropdownMenuSeparator />
      </DropdownMenuContent>
    </DropdownMenu>
  </div>

  <div v-else :class="$attrs.class">
    {{ title }}
  </div>
</template>
