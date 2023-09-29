<template>
  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>


  <div class="reviews-view">
    <Header
        :header="this.header_block"
        @popUpCall="popUpCall()"
    />

    <Reviews
        v-if="this.reviews && this.reviews.length > 0"
        :reviews="this.reviews"
        @popUpCall="reviewPopup"
    />

    <div class="union">
      <svg xmlns="http://www.w3.org/2000/svg" width="1716" height="656" viewBox="0 0 1716 656" fill="none">
        <path
            d="M1147.71 186.541C1197.49 54.9356 1331.2 -19.4501 1473.83 4.86829C1615.71 29.1867 1715.26 142.911 1716 281.669V656H1496.86V282.384C1496.86 228.741 1454.51 215.866 1435.94 213.005C1418.11 209.429 1373.54 207.998 1354.23 258.066L1206.37 656H973.279L1147.71 186.541Z"
            fill="white"/>
        <path
            d="M475.371 80.5768C617.257 104.18 716.8 218.62 716.8 357.378V656H498.4V357.378C498.4 304.449 456.057 290.859 437.486 287.998C419.657 285.137 375.086 283.707 355.772 333.774L200.598 656H-33.0283L150 260.819C199.029 130.644 332.743 56.2584 475.371 80.5768Z"
            fill="white"/>
      </svg>
    </div>

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
import Reviews from "../components/reviewsPage/Reviews.vue";
import Footer from "../components/base/Footer.vue";

import RequestPopup from "../components/base/RequestPopup.vue";
import ReviewPopup from "../components/base/ReviewPopup.vue";
import {useMeta} from "vue-meta";

export default {
  name: "ReviewsView",
  inject: ['backendURL'],
  components: {
    Header,
    Reviews,
    Footer,

    RequestPopup,
    ReviewPopup,
  },
  data() {
    return {
      header_block: {},
      reviews: {},

      popup_review: {},

      requestPopUpVisible: false,
      reviewPopUpVisible: false,
    }
  },
  created() {
    this.getPageData()
    this.getObjectsData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero()
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/get_layout/`)
          .then(response => {
            this.header_block = response.data.header_block
            // console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData() {
      await axios
          .get(`${this.backendURL}/api/v1/reviews/`)
          .then(response => {
            this.reviews = response.data.reviews
            // console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },

    popUpCall() {
      this.requestPopUpVisible = true;
      document.body.style.overflow = "hidden";
    },

    reviewPopup(review) {
      this.popup_review = review
      this.reviewPopUpVisible = true;
      document.body.style.overflow = "hidden";
    },

    hidePopUp(target) {
      if (target === 'request') {
        this.requestPopUpVisible = false;
      } else if (target === 'review') {
        this.reviewPopUpVisible = false;
      }
      document.body.style.overflow = "";
    },

    scrollToZero() {
      document.documentElement.scrollTop = 0;
    }
  },
  setup() {
    const title = 'Отзывы | Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома';
    const description = 'Отзывы клиентов компании Кама. Купите мягкие диваны в Казани от Кама. Высокое качество, доступные цены, быстрая доставка и сборка. Сделайте правильный выбор!';

    useMeta({
      title: title,
      description: description,
      og: {
        title: title,
        type: 'website',
        url: 'https://kamamebel.com/',
        description: description,
        site_name: 'Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома',
        locale: 'ru_RU',
        image: 'https://kamamebel.com/images/meta-img.png',
        'image:alt': 'Изображение главной страницы сайта Кама. Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома.'
      },
      twitter: {
        card: 'summary',
        site: 'https://kamamebel.com/',
        title: title,
        description: description,
        image: 'https://kamamebel.com/images/meta-img.png',
        'image:alt': 'Изображение главной страницы сайта Кама. Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома.'
      },
    })
  }
}
</script>

<style scoped>
.union {
  bottom: -5rem;
  z-index: -1;
  position: relative;
  height: 26rem;
}

@media screen and (max-width: 1200px) {
  .union {
    bottom: 2rem;
    height: 20rem;
  }

  .union svg {
    width: 100%;
  }
}

@media screen and (max-width: 990px) {
  .union {
    bottom: 5rem;
    height: 17rem;
  }
}
</style>