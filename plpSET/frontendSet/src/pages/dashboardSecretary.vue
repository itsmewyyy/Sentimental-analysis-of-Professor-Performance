<script setup lang="ts">
import { ref } from "vue";
import { Plus, Trash } from "lucide-vue-next";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import subjectTagging from "@/components/subject-sectionTagging/subjectTagging.vue";
import sectionTagging from "@/components/subject-sectionTagging/sectionTagging.vue";
import secretaryNavbar from "@/components/navigation/secretaryNavbar.vue";
import { ChevronDown } from "lucide-vue-next";

const subjectsectionTags = ref<Array<number>>([]);

const addSubjectSectionTag = () => {
  subjectsectionTags.value.push(subjectsectionTags.value.length + 1);
};

const removeSubjectSectionTag = (index: number) => {
  subjectsectionTags.value.splice(index, 1);
};
</script>

<template>
  <secretaryNavbar></secretaryNavbar>
  <section class="p-20 pt-32 rounded space-y-14 font-raleway">
    <div class="flex items-center space-x-2">
      <Avatar class="w-16 h-16">
        <AvatarImage
          src="https://i1.sndcdn.com/artworks-NuIfnZ3ZMRhLnlEz-QHsZQA-t500x500.jpg"
        />
        <AvatarFallback>PLP</AvatarFallback>
      </Avatar>
      <div class="w-4/6">
        <DropdownMenu>
          <DropdownMenuTrigger
            ><p
              class="font-bold text-3xl flex items-end space-x-12 hover:text-darks-700/80"
            >
              Noreen Perez<ChevronDown class="w-8 h-8" /></p
          ></DropdownMenuTrigger>
          <DropdownMenuContent class="w-[240px]">
            <DropdownMenuLabel>Professors</DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuItem>Ronnie Chu</DropdownMenuItem>
            <DropdownMenuItem>Andres Bonifacio</DropdownMenuItem>
            <DropdownMenuItem
              >Jose Protacio Rizal Mercado Y Alonso Realonda</DropdownMenuItem
            >
          </DropdownMenuContent>
        </DropdownMenu>

        <p class="text-base text-darks-400/60 font-medium">
          College of Computer Studies
        </p>
      </div>
    </div>
    <div>
      <div class="text-xs pb-2 text-darks-200/70 font-medium pl-2">
        Assign subjects and sections to this professor for the current semester.
      </div>
      <div class="border border-black/25 rounded-md">
        <div
          class="flex items-center justify-between border-b border-black/15 text-sm h-14 p-4 pl-5 font-medium text-darks-200/80 hover:bg-darks-50/80 p-2 w-full rounded-t-md"
        >
          <p class="w-6/12">Subject</p>
          <p class="w-6/12 mr-14">Section</p>
        </div>
        <div>
          <div
            v-for="(tag, index) in subjectsectionTags"
            :key="tag"
            class="flex items center pr-12 border-b border-black/15 hover:bg-darks-50/80 space-x-8"
          >
            <div class="flex items-center space-x-4 p-2 w-full">
              <subjectTagging /> <sectionTagging />
            </div>

            <button
              @click="removeSubjectSectionTag(index)"
              class="text-red-500 hover:text-red-700"
            >
              <Trash class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
      <button
        @click="addSubjectSectionTag"
        class="flex items-center h-14 text-sm w-full font-medium text-darks-100 hover:bg-darks-50/80 space-x-1"
      >
        <Plus class="w-5 h-5" />
        <p>New</p>
      </button>
    </div>
  </section>
</template>
