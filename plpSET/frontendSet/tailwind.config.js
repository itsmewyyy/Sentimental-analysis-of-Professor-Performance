const animate = require("tailwindcss-animate");
const flowbite = require("flowbite/plugin");

module.exports = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{js,jsx,vue}",
    "./components/**/*.{js,jsx,vue}",
    "./app/**/*.{js,jsx,vue}",
    "./src/**/*.{js,jsx,vue}",
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      fontFamily: {
        roboto: ["Roboto", "sans-serif"],
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
        reds: {
          200: "#C33232",
          800: "#B40D0D",
        },
      },
      keyframes: {
        "accordion-down": {
          from: { height: 0 },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: 0 },
        },
        "collapsible-down": {
          from: { height: 0 },
          to: { height: "var(--radix-collapsible-content-height)" },
        },
        "collapsible-up": {
          from: { height: "var(--radix-collapsible-content-height)" },
          to: { height: 0 },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
        "collapsible-down": "collapsible-down 0.2s ease-in-out",
        "collapsible-up": "collapsible-up 0.2s ease-in-out",
      },
    },
  },
  plugins: [animate, flowbite],
};
