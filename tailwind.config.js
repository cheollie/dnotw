/** @type {import('tailwindcss').Config} */

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        "bookmark-purple": "#2E43BA",//"#5267DF",
        "bookmark-red": "#11D8BB",//"#FA5959",
        "bookmark-blue": "#2B9EDD",//"#242A45",
        "bookmark-grey": "#9194A2",
        "bookmark-white": "#060721",//"#f7f7f7",
      },
    },
    fontFamily: {
      Poppins: ["Poppins, sans-serif"],
    },
    container: {
      center: true,
      padding: "1rem",
      screens: {
        lg: "1124px",
        xl: "1124px",
        "2xl": "1124px",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
