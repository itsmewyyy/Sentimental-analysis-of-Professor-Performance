<script setup>
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle, SquarePlus } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Toaster } from "@/components/ui/toast";
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
import { ref } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";

// Reuse `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();
</script>

<template>
  <div>
    <!-- Reusable Form Template -->
    <UseTemplate>
      <form class="grid items-start gap-4 px-4">
        <div class="grid gap-2">
          <Label html-for="email" class="text-xs">Admin ID</Label>
          <Input id="Admin Id" type="" default-value="shadcn@example.com" />
        </div>
        <div class="grid gap-2">
          <Label html-for="username" class="text-xs">UserName</Label>
          <Input id="username" default-value="@shadcn" />
        </div>
        <div class="grid gap-2">
          <Label html-for="email" class="text-xs">Password</Label>
          <Input
            id="email"
            type="password"
            default-value="shadcn@example.com"
          />
        </div>
        <div class="grid gap-2">
          <Label html-for="email" class="text-xs">Confirm Password</Label>
          <Input
            id="email"
            type="password"
            default-value="shadcn@example.com"
          />
        </div>
        <div class="grid gap-2">
          <Label for="college" class="text-xs">Department</Label>
          <Select class="sm:w-[300px]">
            <SelectTrigger class="sm:w-full">
              <SelectValue placeholder="Select Department" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="CON" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="pink" fill="pink" /> College of
                    Nursing (CON)
                  </span>
                </SelectItem>
                <SelectItem value="COE" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="orange" fill="orange" /> College of
                    Engineering (COE)
                  </span>
                </SelectItem>
                <SelectItem value="CBA" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="yellow" fill="yellow" /> College of
                    Business Administration (CBA)
                  </span>
                </SelectItem>
                <SelectItem value="COED" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="blue" fill="blue" /> College of
                    Education (COED)
                  </span>
                </SelectItem>
                <SelectItem value="CAS" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="violet" fill="violet" /> College of
                    Arts and Sciences (CAS)
                  </span>
                </SelectItem>
                <SelectItem value="CCS" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="grey" fill="grey" /> College of
                    Computer Studies (CCS)
                  </span>
                </SelectItem>
                <SelectItem value="CIHM" class="flex items-center gap-2">
                  <span class="flex items-center gap-2">
                    <Circle size="14" color="red" fill="red" /> College of
                    International Hospitality Management (CIHM)
                  </span>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <Label for="college" class="text-xs">Select Position</Label>
        <div class="grid gap-2">
          <RadioGroup default-value="comfortable" class="flex space-x-4">
            <div class="flex items-center">
              <RadioGroupItem id="r1" value="default" />
              <Label for="r1" class="ml-2">Dean</Label>
            </div>
            <div class="flex items-center">
              <RadioGroupItem id="r2" value="comfortable" />
              <Label for="r2" class="ml-2">Secretary</Label>
            </div>
          </RadioGroup>
        </div>

        <Button type="submit" class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
          >Confirm</Button
        >
      </form>
    </UseTemplate>

    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger>
          <Button class="" @click="isOpen = true"> Admin </Button>
        </TooltipTrigger>
        <TooltipContent>
          <p>Add Admin to Library</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[505px]">
        <DialogHeader>
          <DialogTitle>New Admin</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new admin
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <Drawer v-else v-model:open="isOpen">
      <DrawerTrigger as-child> </DrawerTrigger>
      <DrawerContent>
        <DrawerHeader class="text-left">
          <DrawerTitle>New Admin</DrawerTitle>
          <DrawerDescription>
            Make changes to your profile here. Click save when you're done.
          </DrawerDescription>
        </DrawerHeader>
        <GridForm />
        <DrawerFooter class="pt-2">
          <DrawerClose as-child>
            <Button variant="outline"> Cancel </Button>
          </DrawerClose>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  </div>
</template>
