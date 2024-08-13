/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.html',
    './static/js/**/*.js',
    './node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('preline/plugin'),
  ],
}
