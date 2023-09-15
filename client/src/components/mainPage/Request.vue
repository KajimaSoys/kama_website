<template>
  <div class="request-component">
    <div class="content">
      <div class="icon-block">
        <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
          <path d="M18 10V18L22.5 21M18 33C9.71573 33 3 26.2843 3 18C3 9.71573 9.71573 3 18 3C26.2843 3 33 9.71573 33 18C33 26.2843 26.2843 33 18 33Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <h2>
        {{ this.request.title }}
      </h2>
      <div class="description">
        {{ this.request.description }}
      </div>

      <div class="button" @click="this.$emit('popUpCall')">
        <span>Оставить заявку</span>
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

    <img :src="`${this.backendURL}${this.request.image}`" alt="" class="image"/>

<!--    <div class="background">-->

<!--    </div>-->

  </div>
</template>

<script>
export default {
  name: "Request",
  inject: ['backendURL'],
  props: [
      'request'
  ],
  emits: [
      'popUpCall'
  ],
  methods: {

  }
}
</script>

<style scoped>
.request-component {
  margin-top: 18.6rem;
  position: relative;
  height: 41.0625rem;
  background-color: #2A2B2D;
  z-index: 0;
}

.background {
  position: absolute;
  height: 41.0625rem;
  background: #2A2B2D;
}

.content {
  padding-top: 5rem;
  margin-left: 23rem;
  margin-right: 23rem;
}

.icon-block {
  background: #434447;
  width: 3.75rem;
  height: 3.75rem;
  position: relative;
  margin-bottom: 2rem;
}

.icon {
  position: absolute;
  left: 0.8375rem;
  top: 0.8375rem;
}

h2 {
  color: #FFF;
  margin-bottom: 2rem;
  width: 60%;
}

.description {
  color: #FFF;
  font-size: 1.125rem;
  width: 35%;
}


.button {
  margin-top: 4rem;
  background: #FFF;
  padding: 0.2rem 2rem;
  display: flex;
  width: 14.1875rem;
  height: 4.375rem;
  justify-content: space-between;
  align-items: center;
  position: relative;
  cursor: pointer;
  transition: background-color .2s ease-in-out;
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

.button:hover {
  background: #212121;
}

.button:hover span {
  color: #fff;
}

.button:hover .arrow-right path {
  stroke: #fff;
}

.image {
  position: absolute;
  width: 28.18175rem;
  height: 39.91675rem;
  transform: rotate(-4deg);
  right: 23rem;
  bottom: -13rem;
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