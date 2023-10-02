<template>
  <div class="questions-component">
    <div class="questions-max">
      <h2 class="title">
        Частые вопросы
      </h2>

      <div class="content">
        <div v-for="question in shownQuestions" :key="question.id" class="question-card"
             @click="toggleAnswer(question.id)">
          <div class="question-content">
            <p>{{ question.question }}</p>
            <div class="icon"
                 :style="{ transform: openQuestions.includes(question.id) ? 'rotate(45deg)' : 'rotate(0deg)' }">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M12 2V22M2 12H22" stroke="#484848" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </div>
          </div>
          <div class="answer" :class="{ 'answer-visible': openQuestions.includes(question.id)}"
               v-html="question.answer">
          </div>
        </div>
        <div class="button">
          <div class="button-text" @click="toggleAllQuestions">
            {{ showAll ? 'Скрыть вопросы' : 'Показать все вопросы' }}
          </div>
          <div class="button-icon" :style="{ transform: showAll ? 'rotate(180deg)' : 'rotate(0deg)' }">
            <svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 17 17" fill="none">
              <path d="M4.5 6.5L8.5 10.5L12.5 6.5" stroke="#484848" stroke-width="1.5" stroke-linecap="round"
                    stroke-linejoin="round"/>
            </svg>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Payment from "../deliveryPage/Payment.vue";

export default {
  name: "Questions",
  components: {Payment},
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
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.questions-max {
  text-align: center;
  max-width: 74rem;
  width: 100%;
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
  border-bottom: 1px solid #E5E5E5;
  cursor: pointer;
  display: flex;
  width: 100%;
  flex-direction: column;
  transition: all 0.3s ease-in-out;

}

.question-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: normal;
  text-align: left;
}

.question-content p {
  cursor: pointer;
}

.icon, .button-icon {
  transition: transform 0.3s ease, background-color 0.2s ease-in-out;
  display: flex;
  cursor: pointer;
  padding: 8px;
  border-radius: 50%;
}

.question-card:hover .icon {
  background-color: #212121;;

}

.icon path {
  transition: stroke 0.2s ease-in-out;
}

.question-card:hover path {
  stroke: white;
}

.answer-base {
  margin-top: 2rem;
  color: #484848;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
  text-align: left;
}

.answer {
  margin-top: 0;
  color: #484848;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
  text-align: left;
  max-height: 0;

  opacity: 0;
  transition: all 0.3s ease-in-out;

}


:deep(.answer p) {
  visibility: hidden;
  transition: all 0.3s ease-in-out;
}


.answer-visible {
  margin-top: 2rem;
  max-height: 20rem;
  opacity: 1;
}

:deep(.answer-visible p) {
  visibility: visible;
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

@media screen and (max-width: 1200px) {
  .questions-component {
    margin-top: 12.5rem;
  }

  .question-content {
    font-size: 1.125rem;
  }

  .answer {
    font-size: 1rem;
  }

}

@media screen and (max-width: 990px) {
  .questions-component {
    margin-top: 7.5rem;
  }

  .content {
    margin-top: 2.6rem;
  }

  .answer {
    font-size: 0.9375rem;
  }

  .button-text {
    font-size: 1rem;
  }
}

@media screen and (max-width: 640px) {
  .questions-component {
    margin-top: 6.25rem;
  }

  .content {
    margin-top: 2rem;
  }

  .question-content {
    font-size: 1rem;
  }

  .answer {
    font-size: 0.875rem;;
  }

  .button-text {
    font-size: 0.9375rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>