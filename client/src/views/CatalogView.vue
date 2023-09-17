<template>
  <div class="catalog-view">
    <Header
        :header="this.header_block"
        @popUpCall="popUpCall()"
    />

    <h1 class="title">Каталог</h1>

    <Filters
        :filters="this.filters"
    />

    <Catalog
        :sofas="this.sofas"
        :filters="this.filters"
    />

    <Footer
        :footer="this.header_block"
        @popUpCall="popUpCall()"
    />

    <RequestPopup
        :visible="requestPopUpVisible"
        @close="hidePopUp()"
    />

  </div>
</template>

<script>
import axios from "axios";

import Header from "../components/base/Header.vue";
import Filters from "../components/catalogPage/Filters.vue";
import Catalog from "../components/catalogPage/Catalog.vue";
import Footer from "../components/base/Footer.vue";
import RequestPopup from "../components/base/RequestPopup.vue";


export default {
  name: "CatalogView",
  inject: ['backendURL'],
  components: {
    Header,
    Filters,
    Catalog,
    Footer,
    RequestPopup
  },
  data() {
    return {
      header_block: {},

      sofas: [],
      filters: {
        sofaForms: {},
        sofaTypes: {},
        foldingMechanisms: {},
        currentSofaForms: 'all',
        currentSofaTypes: 'all',
        currentFoldingMechanisms: 'all',
      },

      requestPopUpVisible: false,

    }
  },

  beforeMount() {
      this.getPageData()
      this.getObjectsData()
  },
  methods: {
    async getPageData(){
      await axios
          .get('api/v1/get_layout/')
          .then( response => {
            this.header_block = response.data.header_block
            console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData(){
      await axios
          .get('api/v1/sofas/')
          .then( response => {
            this.sofas = response.data
            console.log(response.data)

            this.filters.sofaForms = [...new Set(this.sofas.map(sofa => sofa.sofa_form))];
            this.filters.sofaTypes = [...new Set(this.sofas.map(sofa => sofa.sofa_type))];
            this.filters.foldingMechanisms = [...new Set(this.sofas.map(sofa => sofa.folding_mechanism))];


            console.log(this.filters);
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    popUpCall() {
      this.requestPopUpVisible = true;
      document.body.style.overflow = "hidden";
    },
    hidePopUp() {
      this.requestPopUpVisible = false;
      document.body.style.overflow = "";
    },
  },
}
</script>

<style scoped>
h1.title {
  text-align: center;
  margin-top: 6.25rem;
}


</style>