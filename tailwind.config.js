/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ['./homepage/templates/*.{html,htmldjango,js}',
            './databases/templates/authenticate/*.{html,js,htmldjango}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
