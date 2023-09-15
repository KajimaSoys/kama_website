<template>
  <div class="questions-component">
    <h2 class="title">
      Частые вопросы
    </h2>

    <div class="content">
      <div v-for="question in shownQuestions" :key="question.id" class="question-card" @click="toggleAnswer(question.id)">
        <div class="question-content">
          <p>{{ question.question }}</p>
          <div class="icon" :style="{ transform: openQuestions.includes(question.id) ? 'rotate(45deg)' : 'rotate(0deg)' }">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M12 2V22M2 12H22" stroke="#484848" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </div>
        </div>
        <div v-if="openQuestions.includes(question.id)" class="answer">
          <div v-html="question.answer"></div>
        </div>
      </div>
      <div class="button">
        <div class="button-text" @click="toggleAllQuestions">
          {{ showAll ? 'Скрыть вопросы' : 'Показать все вопросы' }}
        </div>
        <div class="button-icon" :style="{ transform: showAll ? 'rotate(180deg)' : 'rotate(0deg)' }">
          <svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 17 17" fill="none">
            <path d="M4.5 6.5L8.5 10.5L12.5 6.5" stroke="#484848" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Questions",
  inject: ['backendURL'],
  props: {
    questions: Array,
  },
  data() {
    return {
      openQuestions: [],
      showAll: false,
    };
  },
  computed: {
    shownQuestions() {
      return this.showAll ? this.questions : this.questions.slice(0, 4);
    },
  },
  methods: {
    toggleAnswer(id) {
      const index = this.openQuestions.indexOf(id);
      if (index === -1) {
        this.openQuestions.push(id);
      } else {
        this.openQuestions.splice(index, 1);
      }
    },
    toggleAllQuestions() {
      this.showAll = !this.showAll;
    },
  },
}
</script>

<style scoped>
.questions-component {
  margin-top: 12.5rem;
  margin-left: 23rem;
  margin-right: 23rem;
}

.title {
  text-align: center;
}

.content {
  margin-top: 4rem;
  border-top: 1px solid #E5E5E5;;
}

.question-card {
  padding: 2rem 0;
  border-bottom: 1px solid #E5E5E5;;
}

.question-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: normal;
}

.question-content p {
  cursor: pointer;
}

.icon, .button-icon {
  transition: transform 0.3s ease;
  display: flex;
  cursor: pointer;
}

.answer {
  margin-top: 2rem;
  color: #484848;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
}

.button {
  margin-top: 4rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  gap: 0.5rem;
}

.button-text {
  color: #212121;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}

@media screen and (max-width: 1200px){

}

@media screen and (max-width: 990px) {

}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 360px) {

}
</style>