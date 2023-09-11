<template>
  <div class="content">
    прив
<!--    <Header :header="this.header" @popUpCall="popUpCall()"/>-->

<!--    <Main :main="this.main" @popUpCall="popUpCall()"/>-->

<!--    <About :about="this.about"/>-->

<!--    <Production :production="this.production"/>-->

<!--    <Services :services="this.services"/>-->

<!--    <Projects :projects="this.projects"/>-->

<!--    <Request requestNum="1"/>-->

<!--    <Stages :stages="this.stages" :stagesArr="this.stagesArr"/>-->

<!--    <Team :team="this.team" :staffArr="this.staffArr"/>-->

<!--    <Request requestNum="2"/>-->

<!--    <Questions :questions="this.questions" :questionsArr="this.questionsArr"/>-->

<!--    <Reviews :reviews="this.reviews" :reviewTextArr="this.reviewTextArr" :reviewVideoArr="this.reviewVideoArr"/>-->

<!--    <Request requestNum="3"/>-->

<!--    <Contacts :contacts="this.contacts"/>-->

<!--    <Footer :header="this.header" :meta="true" @popUpCall="popUpCall()"/>-->

<!--    <VideoPlayer :visible="videoVisible" :videoId="videoId" @close="hideVideo" />-->

<!--    <PopUp :visible="popUpVisible" @close="hidePopUp" />-->

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

      popUpVisible: false,
    }
  },

  methods: {
    async getPageData(){
      await axios
          .get('api/v1/main_page/')
          .then( response => {
            let receivedData = response.data

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

    popUpCall() {
      this.popUpVisible = true;
      document.body.style.overflow = "hidden";
    },
    hidePopUp() {
      this.popUpVisible = false;
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