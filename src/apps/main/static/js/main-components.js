Vue.component("quote", {
  delimiters: ["[[", "]]"],
  props: {
    name: String,
    img: String,
  },

  template: `
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-4">
            <div>
              <p
                class="mt-4 text-base font-bold uppercase tracking-wider text-gray-800 font-inter"
              >
              [[name]]
              </p>
              <p class="text-sm text-gray-500 font-inter">Freelance Painter</p>
            </div>
            <img
              class="w-12 h-12 mt-4"
              v-bind:src="[[img]]"
              alt="Our professionally crafted profession sections"
            />
          </div>

          <img
            class="h-8 mt-4 opacity-50"
            src="../static/imgs/facebook.png"
            alt="Our professionally crafted profession sections"
          />
        </div>
`,
});
const testimonialCard = {
  delimiters: ["[[", "]]"],
  props: {
    name: String,
    quote1: String,
    quote2: String,
    img: String,
  },
  template: `
    <div
      class="relative max-w-lg flex items-center p-8 mt-12 text-base bg-white border-gray-200 rounded-md shadow-lg font-proxima"
    >
      <div class="flex flex-col justify-around text-gray-700 font-proxima">
        <div class="italic">
          <p>
          [[quote1]]
          </p>
          <p
            class="absolute top-0 left-0 leading-none text-gray-900 opacity-25 text-9xl"
          >
            "
          </p>
        </div>
        <p class="mt-4 italic">
        [[ quote2 ]]
        </p>

        <quote v-bind:name="name" v-bind:img="img"> </quote>

      </div>
    </div>
`,
};

const app = new Vue({
  el: "#app",
  data: {},
  components: { testimonialCard },
});
