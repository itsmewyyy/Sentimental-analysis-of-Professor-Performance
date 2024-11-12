<template>
  <Toaster></Toaster>
  <NavBarDean></NavBarDean>
  <ScrollArea class="h-svh w-full">
    <div class="max-w-3xl mx-auto p-4 space-y-4">
      <h1 class="text-xl font-semibold mt-4 text-gray-900">Dean Profile</h1>

      <Card>
        <CardContent class="p-6">
          <div class="flex justify-between items-start">
            <div class="flex gap-4 items-center">
              <Avatar class="h-16 w-16">
                <AvatarImage
                  src="https://scontent.fcrk3-2.fna.fbcdn.net/v/t39.30808-1/464624148_1812122635988644_8047543269600036803_n.jpg?stp=dst-jpg_s160x160&_nc_cat=103&ccb=1-7&_nc_sid=6738e8&_nc_ohc=0C3RvHUHEjcQ7kNvgF_do2n&_nc_zt=24&_nc_ht=scontent.fcrk3-2.fna&_nc_gid=AH7tbo_NHnbk6TXxaOG0bRA&oh=00_AYAN1CwDuYbpljVoCcywiXOgEh6Jb89ShPvrhRMoOFwmPA&oe=67281993"
                  alt=""
                />
                <AvatarFallback>JA</AvatarFallback>
              </Avatar>
              <div>
                <h2 class="text-lg font-semibold">
                  {{ deanProfile.account.admin_username }}
                </h2>
                <p class="text-gray-500 italic text-xs">
                  {{ deanProfile.account.college }}
                </p>
              </div>
            </div>
            <Button variant="ghost" size="sm" class="text-blue-600">
              <Pencil class="h-4 w-4 mr-1" />
              Edit
            </Button>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader class="flex flex-row items-center justify-between">
          <CardTitle>Change Password</CardTitle>
          <Dialog>
            <DialogTrigger as-child>
              <Button variant="ghost" size="sm" class="text-blue-600">
                <Pencil class="h-4 w-4 mr-1" />
                Edit
              </Button>
            </DialogTrigger>
            <DialogContent class="w-full p-4 sm:p-6 sm:max-w-md">
              <DialogHeader>
                <DialogTitle>Change Password</DialogTitle>
                <DialogDescription
                  >Remember your new password</DialogDescription
                >
              </DialogHeader>
              <form @submit.prevent="updatePassword">
                <div class="flex items-center space-x-2">
                  <div class="grid gap-2">
                    <Label html-for="password" class="text-xs">Password</Label>
                    <Input id="password" type="password" v-model="password" />
                  </div>
                  <div class="grid gap-2">
                    <Label html-for="cpassword" class="text-xs"
                      >Confirm Password</Label
                    >
                    <Input
                      id="cpassword"
                      type="password"
                      v-model="confirmPassword"
                    />
                  </div>
                </div>
                <DialogFooter class="sm:justify-start">
                  <Button
                    type="submit"
                    class="bg-transparent hover:bg-plpgreen-400"
                    >Save Password</Button
                  >
                </DialogFooter>
              </form>
            </DialogContent>
          </Dialog>
        </CardHeader>
        <CardContent class="grid gap-4">
          <div class="grid sm:grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-gray-500">Password</p>
              <p class="text-gray-900">******</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  </ScrollArea>
</template>

<script setup>
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogClose,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-vue-next";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAuthStore } from "@/store/adminStore";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
import NavBarDean from "@/components/navigation/NavBarDean.vue";
import axios from "axios";
import { ref, onMounted } from "vue";
import Toaster from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast";

const authStore = useAuthStore();
authStore.restoreSession();
const { toast } = useToast();
const deanProfile = ref(null);

const password = ref("");
const confirmPassword = ref("");

async function updatePassword() {
  if (password.value !== confirmPassword.value) {
    toast({
      variant: "destructive",
      title: "Error updating password",
      description: "Passwords do not match",
    });
    return;
  }
  try {
    const adminId = localStorage.getItem("admin_id")?.toUpperCase();
    await axios.put(
      `https://sentiment-professor-feedback-1.onrender.com/api/admininfocrud/${adminId}`,
      {
        password: password.value,
        confirm_password: confirmPassword.value,
      }
    );
    toast({
      title: "Success",
      description: "Password updated succesfully",
    });
  } catch (error) {
    toast({
      variant: "destructive",
      title: "Error updating password",
      description: error.error,
    });
  }
}

onMounted(async () => {
  const adminUsername = localStorage.getItem("admin_id");
  if (adminUsername) {
    try {
      const response = await axios.get(
        `https://sentiment-professor-feedback-1.onrender.com/api/dean-profile?admin_username=${adminUsername}`
      );
      console.log(response.data);
      deanProfile.value = response.data;
    } catch (error) {
      console.error("Error fetching dean profile:", error);
    }
  } else {
    console.error("Admin ID not found in localStorage.");
  }
});
</script>
