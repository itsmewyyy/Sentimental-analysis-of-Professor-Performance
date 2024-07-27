module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        raleway: ["Raleway", "sans-serif"],
      },
      colors: {
        darks: {
          50: "#F8F8F8",
          100: "#B4B4B4",
          200: "#5C5C5C",
          300: "#595959",
          400: "#474747",
          500: "#464646",
          600: "#3F3F3F",
          700: "#3E3E3E",
          800: "#252525",
          900: "#000000",
        },

        plpyellow: {
          100: "#EBE186",
          200: "#ECCC35",
        },

        plpgreen: {
          100: "#C9D8C2",
          200: "#5F965E",
          300: "#5C925C",
          400: "#5E8C5E",
        },
      },
    },
  },

  plugins: [require("flowbite/plugin")],
};
