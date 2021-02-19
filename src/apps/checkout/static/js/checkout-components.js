const button = {
  delimiters: ["[[", "]]"],
  methods: {},
  template: `
<button v-:click="">

</button>
    `,
};

const formSection = {
  delimiters: ["[[", "]]"],
  props: {
    header: String,
    subHeader: String,
    active: Boolean,
  },

  template: `
<div v-if="active">
    <h2 class="text-xl font-semibold text-gray-900 whitespace-nowrap">
    [[header]]
    </h2>
    <h3 class="font-thin text-gray-400">
    [[subHeader]]
    </h3>

    <div class="grid gap-6 mt-6 lg:grid-cols-2" id="">
    <slot></slot>
    </div>
</div>
`,
};

const stageSection = {
  delimiters: ["[[", "]]"],
  props: {
    stage: String,
    active: Boolean,
  },

  template: `
<div class="flex flex-col items-center justify-center space-y-3 capitalize">
    <div v-bind:class="{'bg-green-400': active}" class="w-8 h-8 md:w-12 md:h-12 bg-gray-200 rounded-full"></div>
    <p> [[stage]] </p>
</div>
`,
};

const productBenefit = {
  delimiters: ["[[", "]]"],
  props: {
    benefit: String,
  },
  template: `
    <div class="flex items-center justify-start space-x-6">
      <div class="w-6 h-6 text-green-400">
            <svg class="h-full" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" ></path>
            </svg>
      </div>

      <p class="text-lg font-thin">[[benefit]]</p>

    </div>
`,
};

const app = new Vue({
  el: "#app",
  data: {},
  components: { stageSection, formSection, productBenefit },
});
