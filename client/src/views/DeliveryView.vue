<template>
  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <div class="delivery-view">
    <Header
        :header="this.header_block"
        @popUpCall="popUpCall()"
    />

    <Delivery
        :delivery="this.delivery_block"
    />

    <Payment
        :payment="this.payment_block"
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
        @close="hidePopUp()"
    />

  </div>
</template>

<script>
import Header from "../components/base/Header.vue";
import Delivery from "../components/deliveryPage/Delivery.vue";
import Payment from "../components/deliveryPage/Payment.vue";
import Footer from "../components/base/Footer.vue";

import RequestPopup from "../components/base/RequestPopup.vue";
import axios from "axios";
import {useMeta} from "vue-meta";


export default {
  name: "DeliveryView",
  inject: ['backendURL'],
  components: {
    Header,
    Delivery,
    Payment,
    Footer,

    RequestPopup,
  },

  data() {
    return {
      header_block: {},
      delivery_block: {},
      payment_block: {},

      requestPopUpVisible: false,
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero()
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/delivery_page/`)
          .then(response => {
            let receivedData = response.data
            window.ym(95108306, 'hit', 'https://kamamebel.com/delivery')

            this.header_block = receivedData.header_block
            this.delivery_block = receivedData.delivery_block
            this.payment_block = receivedData.payment_block

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
    hidePopUp() {
      this.requestPopUpVisible = false;
      document.body.style.overflow = "";
    },

    reviewPopup(review) {
      this.popup_review = review
      this.reviewPopUpVisible = true;
      document.body.style.overflow = "hidden";
    },
    scrollToZero() {
      document.documentElement.scrollTop = 0;
    }
  },
  setup() {
    const title = 'Доставка и оплата | Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома';
    const description = 'Доставка и оплата в компании Кама. Купите мягкие диваны в Казани от Кама. Высокое качество, доступные цены, быстрая доставка и сборка. Сделайте правильный выбор!';

    useMeta({
      title: title,
      description: description,
      og: {
        title: title,
        type: 'website',
        url: 'https://kamamebel.com/delivery',
        description: description,
        site_name: 'Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома',
        locale: 'ru_RU',
        image: 'https://kamamebel.com/images/meta-img.png',
        'image:alt': 'Изображение главной страницы сайта Кама. Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома.'
      },
      twitter: {
        card: 'summary',
        site: 'https://kamamebel.com/delivery',
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