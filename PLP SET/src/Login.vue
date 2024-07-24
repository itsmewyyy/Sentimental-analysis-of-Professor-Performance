<template>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <div class="min-h-screen flex items-center justify-center font-raleway">
        <section class="bg-yellow-50 rounded-3xl px-5">
            <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
                <div class="flex flex-col justify-center">
                    <h1 class="mb-4 text-md font-bold tracking-tight leading-none text-green-700 md:text-5xl lg:text-4xl">
                        Help Us Improve Education at Pamantasan ng Lungsod ng Pasig!
                    </h1>
                    <p class="mb-6 text-lg font-normal text-gray-500 lg:text-xl">
                        Your feedback is invaluable! Participate in the Student Evaluation of Teachers (SET) 
                        and help us enhance the quality of education at Pamantasan ng Lungsod ng Pasig. 
                        Share your thoughts and experiences to contribute to the continuous improvement of our academic environment.
                    </p>
                </div>
                <div>
                    <div class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl">
                        <h2 class="text-2xl font-bold text-yellow-300">
                            Student Login
                        </h2>
                        <form action="{{ route('login.submit') }}" method="POST" class="mt-8 space-y-6">
                            <div>
                                <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Student Number</label>
                                <input type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-purple-600 focus:border-purple-500 block w-full p-2.5" placeholder="Enter Student Number" required>
                            </div>
                            <div>
                                <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Your password</label>
                                <input type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-purple-600 focus:border-purple-500 block w-full p-2.5" required>
                            </div>
                            <div class="flex justify-between items-center text-sm font-medium text-gray-900">
                                <div>

                                </div> 
                                    <a href="#" class="text-blue-600 hover:underline dark:text-blue-500">Forgot Password?</a>
                            </div>
                            
                            <button type="submit" class="w-full px-5 py-3 text-base font-medium text-center text-white bg-green-700 rounded-lg hover:bg-green-600 focus:ring-4 focus:ring-blue-300 sm:w-auto">Login to your account</button>
                            <div class="text-sm font-medium text-gray-900">
                                Create your student account <a href class="text-blue-600 hover:underline dark:text-blue-500">here</a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
