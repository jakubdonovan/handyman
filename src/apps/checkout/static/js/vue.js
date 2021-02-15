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
    <div v-bind:class="{'bg-green-400': active}" class="w-12 h-12 bg-gray-200 rounded-full"></div>
    <p> [[stage]] </p>
</div>
`,
};

const app = new Vue({
  el: "#app",
  data: {
    msg: "test",
    state: 0,
  },
  components: { stageSection, formSection },
});
