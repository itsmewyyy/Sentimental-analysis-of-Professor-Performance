<template>
  <UseTemplate>
    <div class="flex w-full h-full">
      <!-- Sidebar for Export Options -->
      <div
        class="w-1/5 min-w-[250px] h-full bg-gray-100 rounded-l-md grid grid-rows-5 pt-8 pl-6 pr-4 gap-6"
      >
        <div class="text-2xl font-bold row-start-1 pl-9">Export Reports</div>

        <div class="row-start-2 space-y-4">
          <Select v-model="rating">
            <SelectTrigger>
              <SelectValue placeholder="Select Ratings" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Reports</SelectLabel>
                <SelectItem value="numerical">Numerical Ratings</SelectItem>
                <SelectItem value="feedback">Feedback Ratings</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <!-- Conditional Question Select -->
          <div v-if="rating === 'feedback'">
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Select Question" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Question</SelectLabel>
                  <SelectItem value="1">1</SelectItem>
                  <SelectItem value="2">2</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
        </div>

        <!-- College and Professor Selection -->
        <div class="row-start-3">
          <Select>
            <SelectTrigger>
              <SelectValue placeholder="Select Professor" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Professors</SelectLabel>
                <SelectItem value="prof1">Prof. 1</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>

        <!-- Action Buttons -->
        <div class="row-start-4 space-x-2 pt-8">
          <Button variant="outline" class="px-8">Generate</Button>
          <Button class="bg-plpgreen-200 px-9">Export</Button>
        </div>
      </div>

      <!-- Content Area -->
      <div class="flex-grow bg-plpgreen-100/50 p-8 rounded-r-md">
        <ScrollArea class="max-h-[75vh] rounded-md bg-plpgreen-100/50">
          <div class="w-full bg-white rounded-md shadow-md p-4">
            Content preview goes here...
          </div>
        </ScrollArea>
      </div>
    </div>
  </UseTemplate>

  <!-- Desktop Dialog for Editing Profile -->
  <Dialog v-if="isDesktop" v-model="isOpen">
    <DialogTrigger as-child>
      <Button variant="outline">Edit Profile</Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[1440px] h-5/6 p-0">
      <GridForm />
    </DialogContent>
  </Dialog>

  <!-- Mobile Drawer for Editing Profile -->
  <Drawer v-else v-model="isOpen">
    <DrawerTrigger as-child>
      <Button variant="outline">Edit Profile</Button>
    </DrawerTrigger>
    <DrawerContent>
      <DrawerHeader class="text-left">
        <DrawerTitle>Edit Profile</DrawerTitle>
        <DrawerDescription>
          Make changes to your profile here. Click save when you're done.
        </DrawerDescription>
      </DrawerHeader>
      <GridForm />
      <DrawerFooter class="pt-2">
        <DrawerClose as-child>
          <Button variant="outline">Cancel</Button>
        </DrawerClose>
      </DrawerFooter>
    </DrawerContent>
  </Drawer>
</template>

<script lang="ts" setup>
import { Button } from "@/components/ui/button";
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
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { ref } from "vue";
import { ScrollArea } from "../ui/scroll-area";

// Reusable form section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const rating = ref("");
</script>

<style scoped>
/* Set sidebar's min-width to keep it consistent */
.sidebar {
  min-width: 250px;
}
</style>
