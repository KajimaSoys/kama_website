<template>
  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Header
      :header="this.header_block"
      @popUpCall="popUpCall()"
  />

  <div class="not-found-view">
    <div class="not-found-max">
      <h1>Страница не найдена</h1>
    </div>

  </div>

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
      @close="hidePopUp"
  />

</template>

<script>
import Header from "../components/base/Header.vue";
import Footer from "../components/base/Footer.vue";

import RequestPopup from "../components/base/RequestPopup.vue";
import axios from "axios";
import {useMeta} from "vue-meta";

export default {
  name: "NotFoundView",
  inject: ['backendURL'],
  components: {
    Header,
    Footer,

    RequestPopup,
  },
  data() {
    return {
      header_block: {},
      contacts: {},
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
          .get(`${this.backendURL}/api/v1/get_layout/`)
          .then(response => {
            this.header_block = response.data.header_block
            this.contacts = response.data.contacts_block
            console.log(response.data)
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

    scrollToZero() {
      document.documentElement.scrollTop = 0;
    }
  },
  setup() {
    const title = 'Страница не найдена! | Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома';
    const description = 'Купите мягкие диваны в Казани от Кама. Высокое качество, доступные цены, быстрая доставка и сборка. Сделайте правильный выбор!';

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
.not-found-view {
  margin-top: 6.25rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
  height: 10rem;
}

.not-found-max {
  max-width: 74rem;
  width: 100%;
}

h1 {
  text-align: center;
  padding-bottom: 2rem;
  font-family: OnestMedium, Inter, sans-serif;
  font-size: 2.5rem;
}

.union {
  bottom: -5rem;
  z-index: -1;
  position: relative;
  height: 26rem;
}


@media screen and (max-width: 1200px) {
  .not-found-view {
    margin-top: 4rem;
  }

  h1 {
    font-size: 2.125rem;
  }

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

@media screen and (max-width: 640px) {
  .not-found-view {
    margin-top: 2rem;
  }

  h1 {
    font-size: 1.5rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>
