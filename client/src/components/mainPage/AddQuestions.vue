<template>
  <div class="add-questions-component">
    <div class="add-questions-max">
      <h2 class="title">
        Остались вопросы?
      </h2>
      <div class="description">
        Мы свяжемся с вами в течение 10 минут и поможем разобраться
      </div>
      <div class="button" @click="this.$emit('popUpCall')">
        <span>Задать вопрос</span>
        <svg
            class="arrow-right"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
        >
          <path
              d="M3 11.9999H21M21 11.9999L14 5M21 11.9999L14 18.9999"
              stroke="#212121"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
          />
        </svg>
      </div>

    </div>
  </div>
</template>

<script>
import Description from "../productPage/Description.vue";

export default {
  name: "AddQuestions",
  components: {Description},
  inject: ['backendURL'],
  props: [],
  emits: [
    'popUpCall'
  ],
  methods: {}
}
</script>

<style scoped>
.add-questions-component {
  margin-top: 12.5rem;
  height: 29.75rem;
  background: #2A2B2D;
  display: flex;
  justify-content: center;
}

.add-questions-max {
  max-width: 74rem;
  width: 100%;
  padding: 0 1rem 0 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;

}

.title {
  color: #fff;
  text-align: center;
  padding-top: 6.25rem;
}

.description {
  margin-top: 1rem;
  color: #fff;
  text-align: center;
  font-size: 1.125rem;
  width: 35%;

}

.button {
  margin-top: 4rem;
  background: #FFF;
  padding: 1rem 2rem;
  display: flex;
  width: 20.1875rem;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-left: auto;
  margin-right: auto;
  cursor: pointer;
  transition: background-color 0.5s ease;
}

.button:hover {
  background: #21212100;
}

.button:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100%;
  background: #212121;
  z-index: 0;
  clip-path: inset(-1% 100% -1% 0);
  transition: clip-path 0.5s ease;
}

.button:hover:before {
  clip-path: inset(-10% 0 0 -10%);
}

.button span {
  color: #212121;
  text-align: left;
  font-size: 1.125rem;
  position: relative;
  font-weight: 500;
  transition: color .2s ease-in-out;
}

.arrow-right {
  flex-shrink: 0;
  position: relative;
  overflow: visible;
}

.arrow-right path {
  transition: all .2s ease-in-out;
}

.button:hover span {
  color: #fff;
}

.button:hover .arrow-right path {
  stroke: #fff;
}

@media screen and (max-width: 1200px) {
  .add-questions-component {
    margin-top: 9.5rem;
  }

  .description {
    font-size: 1rem;
  }
}

@media screen and (max-width: 990px) {
  .add-questions-component {
    height: 26.75rem;
    margin-top: 7.5rem;
  }

  .description {
    width: 50%;
  }

  .button {
    padding: 1rem 1.5rem;
    margin-top: 2.5rem;
  }
}

@media screen and (max-width: 640px) {
  .add-questions-component {
    height: 24.75rem;
    margin-top: 6.25rem;
  }

  .description {
    font-size: 0.875rem;
    width: 80%;
    line-height: 1.5rem;
  }

  .button span {
    font-size: 1rem;
  }

  .button {
    width: 14.1875rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>