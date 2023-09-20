<template>
  <div class="request-component">
    <div class="request-max">
      <div class="content">
        <div class="icon-block">
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
            <path
                d="M18 10V18L22.5 21M18 33C9.71573 33 3 26.2843 3 18C3 9.71573 9.71573 3 18 3C26.2843 3 33 9.71573 33 18C33 26.2843 26.2843 33 18 33Z"
                stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
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
    </div>


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
  methods: {}
}
</script>

<style scoped>
.request-component {
  margin-top: 12.5rem;
  position: relative;
  height: 41.0625rem;
  background-color: #2A2B2D;
  z-index: 0;
  display: flex;
  justify-content: center;
}

.request-max {
  max-width: 74rem;
  width: 100%;
  padding: 0 1rem 0 1rem;
  display: flex;
  flex-direction: row;
}

.background {
  position: absolute;
  height: 41.0625rem;
  background: #2A2B2D;
}

.content {
  padding-top: 5rem;
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
  width: 100%;
}

.description {
  color: #FFF;
  font-size: 1.125rem;
  width: 60%;
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
  position: relative;
  width: 28.18175rem;
  height: 39.91675rem;
  transform: rotate(-4deg);
  bottom: -16rem;

}

@media screen and (max-width: 1200px) {
  .request-component {
    margin-top: 9.5rem;
  }

  h2 {
    width: 80%;
  }

  .description {
    font-size: 1rem;
  }

  .image {
    bottom: -9rem;
    right: 2rem;
  }
}

@media screen and (max-width: 990px) {
  .request-component {
    margin-top: 7.5rem;
  }

  .request-max {
    flex-direction: column;
    align-items: center;
  }

  .content {
    padding-top: 5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  h2 {
    width: 100%;
    text-align: center;
  }

  .description {
    width: 70%;
    text-align: center;
  }

  .button {
    height: 3.5rem;
  }

  .image {
    width: 20rem;
    height: 28rem;
    bottom: -5rem;
    right: auto;
  }
}

@media screen and (max-width: 640px) {
  .request-component {
    margin-top: 6.25rem;
  }

  h2 {
    margin-bottom: 1rem;
  }

  .description {
    font-size: 0.875rem;
    width: 90%;
  }

  .image {
    width: 16.5rem;
    bottom: -4rem;
  }
}

@media screen and (max-width: 360px) {
  .button {
    width: 75%;
  }
}
</style>