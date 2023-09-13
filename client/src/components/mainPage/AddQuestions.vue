<template>
  <div class="add-questions-component">
    <h2 class="title">
      Остались вопросы?
    </h2>
    <div class="description">
      Мы свяжемся с вами в течение 10 минут и поможем разобраться
    </div>
    <div class="button">
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
</template>

<script>
export default {
  name: "AddQuestions",
  inject: ['backendURL'],
  props: [
  ],
  emits: [
  ],
  methods: {

  }
}
</script>

<style scoped>
.add-questions-component {
  margin-top: 12.5rem;
  height: 29.75rem;
  background: #2A2B2D;
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
  margin-left: 40%;
  margin-right: 40%;
  //width: 22.5rem;
}

.button {
  margin-top: 4rem;
  background: #FFF;
  padding: 0.2rem 2rem;
  display: flex;
  width: 20.1875rem;
  height: 4.375rem;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-left: auto;
  margin-right: auto;
}

.button span {
  color: #212121;
  text-align: left;
  font-size: 1.125rem;
  position: relative;
  font-weight: 500;
}

.arrow-right {
  flex-shrink: 0;
  position: relative;
  overflow: visible;
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