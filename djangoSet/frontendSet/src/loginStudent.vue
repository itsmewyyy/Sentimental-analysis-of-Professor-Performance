<!-- Student Login -->
<template>
  <div class="min-h-screen flex items-center justify-center font-raleway">
    <section class="bg-plpyellow-100/20 rounded-3xl px-5">
      <div
        class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16"
      >
        <div class="flex flex-col justify-center">
          <h1
            class="mb-4 text-md font-black tracking-tight leading-none text-plpgreen-200 md:text-5xl lg:text-4xl"
          >
            Help Us Improve Education at Pamantasan ng Lungsod ng Pasig!
          </h1>
          <p class="mb-6 text-lg font-normal text-darks-900/50 lg:text-xl">
            Your feedback is invaluable! Participate in the Student Evaluation
            of Teachers (SET) and help us enhance the quality of education at
            Pamantasan ng Lungsod ng Pasig. Share your thoughts and experiences
            to contribute to the continuous improvement of our academic
            environment.
          </p>
        </div>
        <div>
          <div
            class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl"
          >
            <h2 class="text-2xl font-bold text-plpyellow-200">Student Login</h2>
            <form action="" method="POST" class="mt-8 space-y-6">
              <div class="space-y-2">
                <div class="space-y-6">
                  <div>
                    <label
                      for="email"
                      class="block mb-2 text-sm font-medium text-gray-900"
                      >Student Number</label
                    >
                    <input
                      type="text"
                      name="email"
                      id="email"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-purple-600 focus:border-purple-500 block w-full p-2.5"
                      placeholder="Enter Student Number"
                      required
                    />
                  </div>
                  <div>
                    <label
                      for="password"
                      class="block mb-2 text-sm font-medium text-gray-900"
                      >Your password</label
                    >
                    <input
                      type="password"
                      name="password"
                      id="password"
                      placeholder="••••••••"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-purple-600 focus:border-purple-500 block w-full p-2.5"
                      required
                    />
                  </div>
                </div>
                <div
                  class="flex justify-between items-center text-sm font-medium text-gray-900"
                >
                  <div></div>
                  <a
                    href="#"
                    class="text-blue-600 hover:underline dark:text-blue-500 text-xs"
                    >Forgot Password?</a
                  >
                </div>
              </div>
              <div class="space-y-2">
                <button
                  type="submit"
                  class="w-full px-5 py-3 text-sm font-medium text-center text-white bg-plpgreen-200 rounded-lg hover:bg-plpgreen-400 sm:w-auto focus:ring-2 focus:ring-plpgreen-100"
                >
                  Login to your account
                </button>
                <div class="text-xs font-medium text-gray-900">
                  Create your student account
                  <a
                    href=""
                    class="text-blue-600 hover:underline dark:text-blue-500"
                    >here</a
                  >
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
