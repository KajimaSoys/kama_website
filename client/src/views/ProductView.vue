<template>
  <div class="product-view">
    <Header
        :header="this.header_block"
        @popUpCall="popUpCall()"
    />

    <ImageSlider
        :images="this.sofa.images"
    />

    <Description
        :description="this.sofa"
        :contacts="this.contacts"
    />

    <OtherVariants
        v-if="this.sofa.other_variants && this.sofa.other_variants.length > 0"
        :otherVariants="this.sofa.other_variants"
    />

    <OwnConfiguration
      :contacts="this.contacts"
    />

    <Reviews
        v-if="this.sofa.reviews && this.sofa.reviews.length > 0"
        :reviews="this.sofa.reviews"
        @popUpCall="reviewPopup"
    />

    <Footer
        :footer="this.header_block"
        @popUpCall="popUpCall()"
    />

    <RequestPopup
        :visible="requestPopUpVisible"
        @close="hidePopUp('request')"
    />

    <ReviewPopup
        :visible="reviewPopUpVisible"
        :popup_review="this.popup_review"
        @close="hidePopUp('review')"
    />

  </div>
</template>

<script>
import axios from "axios";

import Header from "../components/base/Header.vue";
import ImageSlider from "../components/productPage/ImageSlider.vue";
import Description from "../components/productPage/Description.vue";
import OtherVariants from "../components/productPage/OtherVariants.vue";
import OwnConfiguration from "../components/productPage/OwnConfiguration.vue";
import Reviews from "../components/base/Reviews.vue";
import Footer from "../components/base/Footer.vue";

import RequestPopup from "../components/base/RequestPopup.vue";
import ReviewPopup from "../components/base/ReviewPopup.vue";


export default {
  name: "ProductView",
  components: {
    Header,
    ImageSlider,
    Description,
    OtherVariants,
    OwnConfiguration,
    Reviews,
    Footer,

    RequestPopup,
    ReviewPopup
  },
  data() {
    return {
      header_block: {},
      contacts: {},

      sofa: {},

      popup_review: {},

      requestPopUpVisible: false,
      reviewPopUpVisible: false,
    }
  },

  created() {
      this.getPageData()
      this.getObjectsData()
  },
  methods: {
    async getPageData(){
      await axios
          .get('api/v1/get_layout/')
          .then( response => {
            this.header_block = response.data.header_block
            this.contacts = response.data.contacts_block
            console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData(){
      await axios
          .get(`api/v1/sofas/${this.$route.params.id}/`)
          .then( response => {
            this.sofa = response.data
            console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    popUpCall() {
      this.requestPopUpVisible = true;
      document.body.style.overflow = "hidden";
    },
    reviewPopup(review){
      this.popup_review = review
      this.reviewPopUpVisible = true;
      document.body.style.overflow = "hidden";
    },
    hidePopUp(target) {
      if (target === 'request'){
        this.requestPopUpVisible = false;
      } else if (target === 'review') {
        this.reviewPopUpVisible = false;
      }
      document.body.style.overflow = "";
    },
  },
}
</script>

<style scoped>

</style>