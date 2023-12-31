<template>
  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <div class="main-view">

    <Header
        :header="this.header_block"
        @popUpCall="popUpCall('request')"
    />

    <Main
        :main="this.main_block"
        @popUpCall="popUpCall('request')"
    />

    <Popular
        :popular_models="this.popular_models"
    />

    <About
        :about="this.about_block"
        id="about_block"
    />

    <Why
        :why="this.why_block"
    />

    <Request
        :request="this.request_block"
        @popUpCall="popUpCall('request')"
    />

    <Stages
        :stages="this.stages_block"
    />

    <Delivery
        :delivery="this.delivery_block"
    />

    <Reviews
        :reviews="this.reviews"
        @popUpCall="reviewPopup"
    />

    <Questions
        :questions="this.questions"
    /><!--:questionsArr="this.questionsArr"-->

    <AddQuestions
        @popUpCall="popUpCall('question')"
    />

    <Contacts
        :contacts="this.contacts_block"
        id="contacts_block"
    />

    <Footer
        :footer="this.header_block"
        @popUpCall="popUpCall('request')"
    />

    <RequestPopup
        :visible="requestPopUpVisible"
        @close="hidePopUp('request')"
    />

    <QuestionPopup
        :visible="questionPopUpVisible"
        @close="hidePopUp('question')"
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
import Main from "../components/mainPage/Main.vue";
import Popular from "../components/mainPage/Popular.vue";
import About from "../components/mainPage/About.vue";
import Why from "../components/mainPage/Why.vue";
import Request from "../components/mainPage/Request.vue";
import Stages from "../components/mainPage/Stages.vue";
import Delivery from "../components/mainPage/Delivery.vue";
import Reviews from "../components/base/Reviews.vue";
import Questions from "../components/mainPage/Questions.vue";
import AddQuestions from "../components/mainPage/AddQuestions.vue";
import Contacts from "../components/mainPage/Contacts.vue";
import Footer from "../components/base/Footer.vue";
import RequestPopup from "../components/base/RequestPopup.vue";
import QuestionPopup from "../components/base/QuestionPopup.vue";
import ReviewPopup from "../components/base/ReviewPopup.vue";
import {useMeta} from "vue-meta";

export default {
  name: "MainView",
  inject: ['backendURL'],
  components: {
    Header,
    Main,
    Popular,
    About,
    Why,
    Request,
    Stages,
    Delivery,
    Reviews,
    Questions,
    AddQuestions,
    Contacts,
    Footer,
    RequestPopup,
    QuestionPopup,
    ReviewPopup,
  },
  data() {
    return {
      header_block: {},
      main_block: {},
      about_block: {},
      why_block: {},
      request_block: {},
      stages_block: {},
      delivery_block: {},
      contacts_block: {},

      popular_models: {},
      reviews: {},
      questions: [],

      popup_review: {},

      requestPopUpVisible: false,
      questionPopUpVisible: false,
      reviewPopUpVisible: false,
    }
  },
  created() {
    this.getPageData()
    this.getObjectsData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();
  },

  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/main_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.main_block = receivedData.main_block
            this.about_block = receivedData.about_block
            this.why_block = receivedData.why_block
            this.request_block = receivedData.request_block
            this.stages_block = receivedData.stages_block
            this.delivery_block = receivedData.delivery_block
            this.contacts_block = receivedData.contacts_block
            window.ym(95108306, 'hit', 'https://kamamebel.com/');

            // console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData() {
      await axios
          .get(`${this.backendURL}/api/v1/service/`)
          .then(response => {
            let receivedData = response.data

            this.popular_models = receivedData.popular_models
            this.reviews = receivedData.reviews
            this.questions = receivedData.questions

            // console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },

    popUpCall(target) {
      if (target === 'request') {
        this.requestPopUpVisible = true;
      } else if (target === 'question') {
        this.questionPopUpVisible = true;
      }
      document.body.style.overflow = "hidden";
    },

    hidePopUp(target) {
      if (target === 'request') {
        this.requestPopUpVisible = false;
      } else if (target === 'question') {
        this.questionPopUpVisible = false;
      } else if (target === 'review') {
        this.reviewPopUpVisible = false;
      }
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
    const title = 'Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома';
    const description = 'Купите мягкие диваны в Казани от Кама. Высокое качество, доступные цены, быстрая доставка и сборка. Сделайте правильный выбор!';

    useMeta({
      title: title,
      description: description,
      og: {
        title: title,
        type: 'website',
        url: 'https://kamamebel.com',
        description: description,
        site_name: 'Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома',
        locale: 'ru_RU',
        image: 'https://kamamebel.com/images/meta-img.png',
        'image:alt': 'Изображение главной страницы сайта Кама. Диваны в Казани от Кама - Лучшие мягкие диваны для вашего дома.'
      },
      twitter: {
        card: 'summary',
        site: 'https://kamamebel.com',
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

</style>