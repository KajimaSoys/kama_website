<template>
  <div class="main-component">
    <svg class="union" xmlns="http://www.w3.org/2000/svg" width="1584" height="635" viewBox="0 0 1584 635" fill="none">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M200 0H1419C1510.13 0 1584 73.873 1584 165H200C180.67 165 165 180.67 165 200C165 219.33 180.67 235 200 235H1384C1494.46 235 1584 324.543 1584 435C1584 545.457 1494.46 635 1384 635H0C0 543.873 73.873 470 165 470H1384C1403.33 470 1419 454.33 1419 435C1419 415.67 1403.33 400 1384 400H200C89.5431 400 0 310.457 0 200C0 89.543 89.5431 0 200 0Z" fill="white"/>
    </svg>

    <div class="parent">
      <h1 class="title">{{ this.main.title }}</h1>
      <div class="description">{{ this.main.description }}</div>
      <div class="button-container">
        <router-link class="button" :to="{ name: 'catalog' }">
          <span>Перейти в каталог</span>
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
              stroke="white"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </router-link>
      </div>

      <img :src="`${this.backendURL}${this.main.image}`" alt="" class="image"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "Main",
  inject: ['backendURL'],
  props: [
      "main"
  ],
  emits: [
  ],
  methods: {

  }
}
</script>

<style scoped>
.main-component {
  margin: 3.5rem 10.5rem 0;
  height: 40rem;
  position: relative;
}

.union {
  position: absolute;
  z-index: 0;
}

.parent {
  display: grid;
  position: relative;
  grid-template-columns: 1fr;
  grid-template-rows: 0.95fr 1fr 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  margin: 0 12rem 0;
  padding-top: 2.3rem;
}

.title { grid-area: 1 / 1 / 2 / 3; }
.description {
  grid-area: 2 / 1 / 3 / 2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 23.375rem;
}

.button-container {
  display: flex;
  align-items: flex-end;
}

.button {
  grid-area: 3 / 1 / 4 / 2;
  background: #212121;
  padding: 0.2rem 2rem;
  display: flex;
  width: 18.1875rem;
  height: 4.375rem;

  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;

  position: relative;
  top: -1.5rem;

  text-decoration: none;
}

.button:hover {
}

.button:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100%;
  background: #F8F8F8;
  z-index: 0;
  clip-path: inset(-1% 100% -1% 0);
  transition: clip-path 0.5s ease;
}

.button:hover:before {
  clip-path: inset(-10% 0 0 -10%);
}

.button span {
  color: #ffffff;
  text-align: left;
  font-size: 1.125rem;
  position: relative;
  background: linear-gradient(to right, #212121, #212121 50%, #ffffff 50%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-size: 200% 100%;
  background-position: 100%;
  transition: background-position .18s ease-in-out;
}

.arrow-right {
  flex-shrink: 0;
  position: relative;
  overflow: visible;
}

.button:hover span {
    background-position: 0 100%;
}

.button path {
  transition: stroke 0.4s ease;
}

.button:hover path {
  stroke: #212121;
}

.image {
  grid-area: 2 / 2 / 4 / 3;
  position: relative;
  top: -1.5rem;
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