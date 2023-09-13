<template>
  <div class="main-view">

    <Header :header="this.header_block" @popUpCall="popUpCall('request')"/>

    <Main :main="this.main_block" @popUpCall="popUpCall('request')"/>

    <Popular />

    <About :about="this.about_block"/>

    <Why :why="this.why_block"/>

    <Request :request="this.request_block"/>

    <Stages :stages="this.stages_block"/>

    <Delivery :delivery="this.delivery_block"/>

    <Reviews />

    <Questions  /><!--:questionsArr="this.questionsArr"-->

    <AddQuestions @popUpCall="popUpCall('question')"/>

    <Contacts :contacts="this.contacts_block"/>

    <Footer :footer="this.header_block" @popUpCall="popUpCall('request')"/>

<!--    <VideoPlayer :visible="videoVisible" :videoId="videoId" @close="hideVideo" />-->

    <RequestPopup :visible="requestPopUpVisible" @close="hidePopUp('request')" />

    <QuestionPopup :visible="questionPopUpVisible" @close="hidePopUp('question')"/>

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
    QuestionPopup
  },

  data(){
    return {
      header_block: {},
      main_block: {},
      // popular_block
      about_block: {},
      why_block: {},
      request_block: {},
      stages_block: {},
      delivery_block: {},
      // reviews_block
      // questions_block: {},
      contacts_block: {},
      footer_block: {},

      requestPopUpVisible: false,
      questionPopUpVisible: false,
    }
  },

  methods: {
    async getPageData(){
      await axios
          .get('api/v1/main_page/')
          .then( response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.main_block = receivedData.main_block
            this.about_block = receivedData.about_block
            this.why_block = receivedData.why_block
            this.request_block = receivedData.request_block
            this.stages_block = receivedData.stages_block
            this.delivery_block = receivedData.delivery_block
            this.contacts_block = receivedData.contacts_block
            this.footer_block = receivedData.footer_block

            // receivedData.forEach(block => {
            //   if (block.type === 'HeaderBlock') {
            //     this.header = block.data
            //   } else if (block.type === 'MainBlock') {
            //     this.main = block.data
            //   } else if (block.type === 'AboutBlock') {
            //     this.about = block.data
            //   } else if (block.type === 'ProductionBlock') {
            //     this.production = block.data
            //   } else if (block.type === 'ServicesBlock') {
            //     this.services = block.data
            //   } else if (block.type === 'ProjectsBlock') {
            //     this.projects = block.data
            //   } else if (block.type === 'StagesBlock') {
            //     this.stages = block.data
            //   } else if (block.type === 'TeamBlock') {
            //     this.team = block.data
            //   } else if (block.type === 'QuestionsBlock') {
            //     this.questions = block.data
            //   } else if (block.type === 'ReviewsBlock') {
            //     this.reviews = block.data
            //   } else if (block.type === 'ContactsBlock') {
            //     this.contacts = block.data
            //   } else if (block.type === 'FooterBlock') {
            //     this.footer = block.data
            //   }
            // });

            console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData(){
      await axios
          .get('api/v1/core_objects/')
          .then( response => {
            let receivedData = response.data
            receivedData.forEach( block => {
              if (block.type === 'Stages') {
                this.stagesArr.push(block.data)
              } else if (block.type === 'Staff') {
                this.staffArr.push(block.data)
              } else if (block.type === 'Questions') {
                this.questionsArr.push(block.data)
              } else if (block.type === 'ReviewText') {
                this.reviewTextArr.push(block.data)
              } else if (block.type === 'ReviewVideo') {
                this.reviewVideoArr.push(block.data)
              }
            });

            // console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    popUpCall(target) {
      if (target === 'request'){
        this.requestPopUpVisible = true;
      } else {
        this.questionPopUpVisible = true;
      }
      document.body.style.overflow = "hidden";
    },
    hidePopUp(target) {
      if (target === 'request'){
        this.requestPopUpVisible = false;
      } else {
        this.questionPopUpVisible = false;
      }
      document.body.style.overflow = "";
    },

  },

  beforeMount() {
    this.getPageData()
    // this.getObjectsData()
  },

}
</script>

<style scoped>

</style>