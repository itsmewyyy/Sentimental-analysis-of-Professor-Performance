<script setup lang="ts">
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import MISNavbar from "@/components/navigation/NavBarMIS.vue";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import Toaster from "@/components/ui/toast/Toaster.vue";
import adminList from "@/components/databaseManagement/admins/adminList.vue";
import professorList from "@/components/databaseManagement/professors/professorList.vue";
import collegeList from "@/components/databaseManagement/colleges/collegeList.vue";
import programList from "@/components/databaseManagement/programs/programList.vue";
import sectionList from "@/components/databaseManagement/sections/sectionList.vue";
import subjectList from "@/components/databaseManagement/subjects/subjectList.vue";
import categoryList from "@/components/databaseManagement/categories/categoryList.vue";
import NumQuestionList from "@/components/databaseManagement/numericalQuestions/NumQuestionList.vue";
import feedbackquestionlist from "@/components/databaseManagement/feedbackquestions/feedbackquestionlist.vue";
import { useAuthStore } from "@/store/adminStore";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
const authStore = useAuthStore();
authStore.restoreSession();
</script>

<template>
  <Toaster />
  <MISNavbar></MISNavbar>
  <ScrollArea class="h-svh w-full">
    <section class="p-20 pt-32">
      <div
        class="w-full border border-black/25 rounded-md space-y-8 pb-4 px-9 pt-9"
      >
        <div class="w-full border-b border-black/15 pb-6">
          <h1 class="font-bold text-3xl">Database Management</h1>
          <p class="font-medium text-base text-darks-200/60">
            Displayed below are numerous databases, organized with tabs for easy
            navigation.
          </p>
        </div>

        <Tabs default-value="1" class="w-full pr-1">
          <TabsList class="grid w-full grid-cols-3 w-5/12 bg-plpgreen-100/40">
            <TabsTrigger value="1"> Admins and Professors </TabsTrigger>
            <TabsTrigger value="2">
              Colleges, Programs, Sections, and Subjects
            </TabsTrigger>
            <TabsTrigger value="3"> Questions </TabsTrigger>
          </TabsList>
          <!---Group 1-->
          <TabsContent value="1" class="w-full">
            <div class="w-full">
              <Tabs default-value="1" class="w-full -space-y-1">
                <TabsList
                  class="grid w-full grid-cols-2 w-5/12 bg-plpyellow-100/30"
                >
                  <TabsTrigger value="1"> Admins </TabsTrigger>
                  <TabsTrigger value="2"> Professors </TabsTrigger>
                </TabsList>
                <TabsContent value="1" class="w-full">
                  <adminList></adminList>
                </TabsContent>
                <TabsContent value="2">
                  <professorList></professorList
                ></TabsContent>
              </Tabs>
            </div>
          </TabsContent>
          <!---Group 2-->
          <TabsContent value="2">
            <div class="w-full">
              <Tabs default-value="1" class="w-full -space-y-1">
                <TabsList
                  class="grid w-full grid-cols-4 w-5/12 bg-plpyellow-100/30"
                >
                  <TabsTrigger value="1"> Colleges </TabsTrigger>
                  <TabsTrigger value="2"> Progams </TabsTrigger>
                  <TabsTrigger value="3"> Sections </TabsTrigger>
                  <TabsTrigger value="4"> Subjects </TabsTrigger>
                </TabsList>
                <TabsContent value="1" class="w-full">
                  <collegeList></collegeList>
                </TabsContent>
                <TabsContent value="2">
                  <programList></programList>
                </TabsContent>
                <TabsContent value="3"
                  ><sectionList></sectionList>
                </TabsContent>
                <TabsContent value="4"
                  ><subjectList></subjectList>
                </TabsContent>
              </Tabs></div
          ></TabsContent>
          <!---Group 3-->
          <TabsContent value="3">
            <div class="w-full">
              <Tabs default-value="1" class="w-full -space-y-1">
                <TabsList
                  class="grid w-full grid-cols-3 w-5/12 bg-plpyellow-100/30"
                >
                  <TabsTrigger value="1"> Categories </TabsTrigger>
                  <TabsTrigger value="2"> Numerical Questions </TabsTrigger>
                  <TabsTrigger value="3"> Feedback Questions </TabsTrigger>
                </TabsList>
                <TabsContent value="1" class="w-full">
                  <categoryList></categoryList>
                </TabsContent>
                <TabsContent value="2">
                  <NumQuestionList></NumQuestionList>
                </TabsContent>
                <TabsContent value="3">
                  <feedbackquestionlist></feedbackquestionlist>
                </TabsContent>
              </Tabs></div
          ></TabsContent>
        </Tabs>
      </div>
    </section>
  </ScrollArea>
</template>
