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
import MISNavbar from "@/components/navigation/MISNavbar.vue";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import adminList from "@/components/databaseManagement/admins/adminList.vue";
import professorList from "@/components/databaseManagement/professors/professorList.vue";
</script>

<template>
  <MISNavbar></MISNavbar>
  <section class="p-20 pt-32 min-h-full">
    <div
      class="w-full border border-black/15 rounded-md space-y-8 pb-4 px-9 pt-9"
    >
      <div class="w-full border-b border-black/15 pb-6">
        <h1 class="font-bold text-3xl">Database Management</h1>
        <p class="font-medium text-base text-darks-200/60">
          Displayed below are numerous databases, organized with tabs for easy
          navigation.
        </p>
      </div>

      <Tabs default-value="1" class="w-full pr-1">
        <TabsList class="grid w-full grid-cols-3 w-5/12">
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
              <TabsList class="grid w-full grid-cols-2 w-5/12">
                <TabsTrigger value="1"> Admins </TabsTrigger>
                <TabsTrigger value="2"> Professors </TabsTrigger>
              </TabsList>
              <TabsContent value="1" class="w-full">
                <div class="w-full flex-col">
                  <adminList></adminList>
                </div>
              </TabsContent>
              <TabsContent value="2">
                <div class="w-full"><professorList></professorList></div
              ></TabsContent>
            </Tabs>
          </div>
        </TabsContent>
        <!---Group 2-->
        <TabsContent value="2">
          <div class="w-full">
            <Tabs default-value="1" class="w-full -space-y-1">
              <TabsList class="grid w-full grid-cols-4 w-5/12">
                <TabsTrigger value="1"> Colleges </TabsTrigger>
                <TabsTrigger value="2"> Progams </TabsTrigger>
                <TabsTrigger value="3"> Sections </TabsTrigger>
                <TabsTrigger value="4"> Subjects </TabsTrigger>
              </TabsList>
              <TabsContent value="1" class="w-full">
                <div class="w-full">1</div>
              </TabsContent>
              <TabsContent value="2"> <div class="w-full">22</div></TabsContent>
              <TabsContent value="3"
                >33
                <div class="w-full"></div
              ></TabsContent>
              <TabsContent value="4"
                >44
                <div class="w-full"></div
              ></TabsContent>
            </Tabs></div
        ></TabsContent>
        <!---Group 3-->
        <TabsContent value="3">
          <div class="w-full">
            <Tabs default-value="1" class="w-full -space-y-1">
              <TabsList class="grid w-full grid-cols-3 w-5/12">
                <TabsTrigger value="1"> Categories </TabsTrigger>
                <TabsTrigger value="2"> Numerical Questions </TabsTrigger>
                <TabsTrigger value="3"> Feedback Questions </TabsTrigger>
              </TabsList>
              <TabsContent value="1" class="w-full">
                <div class="w-full">111</div>
              </TabsContent>
              <TabsContent value="2"> <div class="w-full">2</div></TabsContent>
              <TabsContent value="3">
                3
                <div class="w-full"></div
              ></TabsContent>
            </Tabs></div
        ></TabsContent>
      </Tabs>
    </div>
  </section>
</template>
