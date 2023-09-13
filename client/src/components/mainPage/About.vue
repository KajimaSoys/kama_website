<template>
  <div class="about-component">
    <svg class="union" xmlns="http://www.w3.org/2000/svg" width="1841" height="731" viewBox="0 0 1841 731" fill="none">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M89 0H1604C1790.12 0 1941 163.64 1941 365.5C1941 567.36 1790.12 731 1604 731H200C89.543 731 0 641.457 0 531V453H1604C1639.35 453 1668 424.346 1668 389C1668 353.654 1639.35 325 1604 325H389C223.315 325 89 190.685 89 25V0Z" fill="white"/>
    </svg>

    <div class="content">

      <div class="row-first">
        <img :src="`${this.backendURL}${this.about.image_first}`" alt="" class="image"/>
        <h2>{{ this.about.title }}</h2>
      </div>

      <div class="row-second">
        <div class="first-image-container">
          <img :src="`${this.backendURL}${this.about.image_second}`" alt="" class="image"/>
        </div>
        <span class="description">
          {{ this.about.description }}
        </span>
        <div class="second-image-container">
          <img :src="`${this.backendURL}${this.about.image_third}`" alt="" class="image"/>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  inject: ['backendURL'],
  props: [
      'about'
  ],
  emits: [
  ],
  methods: {

  }
}
</script>

<style scoped>
.about-component {
  margin-top: 12.5rem;
  //margin-right: 10.5rem;
  //margin-left: 10.5rem;
  //margin-bottom: 0;
  height: 52.75rem;
  position: relative;
}

.union {
  position: absolute;
  z-index: 0;
  left: 4.94rem;
  top: 2.69rem;
}

.content{
  margin-left: 23rem;
  margin-right: 23rem;
  position: relative;
}

.row-first {
  display: flex;
  gap: 5rem;
  align-items: center;
}

.row-second {
  display: flex;
}

.first-image-container {
  display: flex;
  align-items: flex-end;
}

.description {
  height: 27rem;
  display: flex;
  align-items: center;
  font-size: 1.125rem;
  margin-left: 6.25rem;
  margin-right: 5.75rem;
}

.second-image-container {

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