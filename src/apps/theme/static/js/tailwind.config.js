// This is a minimal config.
// If you need the full config, get it from here:
// https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js

module.exports = {
  purge: ["../../../**/templates/**/*.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        inter: "Inter",
        roboto: "Roboto",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    // require("@tailwindcss/custom-forms"),
    require("@tailwindcss/forms"),
  ],
};
