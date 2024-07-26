<template>
  <section class="w-full h-screen flex items-center justify-center p-10 font-raleway">
       <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <div class="flex rounded-2xl shadow-lg max-w-5xl w-full">
      <div class="w-3/5 p-10 flex flex-col items-start justify-center bg-yellow-50 rounded-l-2xl">
        <h1 class="mb-10 tracking-relaxed font-semibold text-green-700 lg:text-4xl leading-snug">
          Welcome to Student Evaluation of Teaching
        </h1>
        <p class="mb-0 text-lg font-light text-gray-500 tracking-tight text-left rtl:text-right">
          Get involved in shaping the future of education by registering today. Your feedback on teachers will play a key role in improving the quality of instruction and fostering a better learning environment.
        </p>
      </div>
      <div class="w-2/5 p-10 flex items-center justify-center">
        <div class="w-full max-w-sm p-10">
          <h4 class="text-2xl font-medium text-black mb-4">Sign in to our platform</h4>
          <p class="text-sm text-gray-500 mb-8">Create your account Now</p>
          <form class="w-full mx-auto">
            <div class="relative z-0 w-full mb-8 group">
              <input type="email" name="email" id="floating_email" class="block py-3 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-black peer" placeholder=" " required />
              <label for="floating_email" class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-4 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-green-800 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Student Number</label>
            </div>
            <div class="relative z-0 w-full mb-8 group">
              <input type="password" name="password" id="floating_password" class="block py-3 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-black peer" placeholder=" " required />
              <label for="floating_password" class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-4 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-green-800 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Password</label>
            </div>
            <div class="relative z-0 w-full mb-20 group">
              <input type="password" name="password_confirmation" id="floating_repeat_password" class="block py-3 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-black peer" placeholder=" " required />
              <label for="floating_repeat_password" class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-4 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-green-800 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Confirm password</label>
            </div>
            <button type="submit" class="w-full px-6 py-3 text-sm font-medium text-center text-white bg-green-700 rounded-lg hover:bg-green-600 focus:ring-4 focus:outline-none focus:ring-black">Register</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
