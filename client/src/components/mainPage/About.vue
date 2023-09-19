<template>
  <div class="about-component">
    <div class="about-max">
      <svg class="union" xmlns="http://www.w3.org/2000/svg" width="1841" height="731" viewBox="0 0 1841 731"
           fill="none">
        <path fill-rule="evenodd" clip-rule="evenodd"
              d="M89 0H1604C1790.12 0 1941 163.64 1941 365.5C1941 567.36 1790.12 731 1604 731H200C89.543 731 0 641.457 0 531V453H1604C1639.35 453 1668 424.346 1668 389C1668 353.654 1639.35 325 1604 325H389C223.315 325 89 190.685 89 25V0Z"
              fill="white"/>
      </svg>

      <div class="content">

        <div class="row-first">
          <div class="image-container">
            <div class="image-background"></div>
            <img :src="`${this.backendURL}${this.about.image_first}`" alt="" class="image"/>
          </div>
          <div class="title">
            <div class="title-background"></div>
            <h2>{{ this.about.title }}</h2>
          </div>

        </div>

        <div class="row-second">
          <div class="first-image-container">
            <img :src="`${this.backendURL}${this.about.image_second}`" alt="" class="image"/>
          </div>
          <div class="description">
            <div class="description-background"></div>
            {{ this.about.description }}
          </div>
          <div class="second-image-container">
            <img :src="`${this.backendURL}${this.about.image_third}`" alt="" class="image"/>
          </div>

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
  emits: [],
  methods: {}
}
</script>

<style scoped>
.about-component {
  margin-top: 6.25rem;
  padding-top: 6.25rem;
  height: 52.75rem;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.about-max {
  max-width: 74rem;
  width: 100%;
}

.union {
  position: absolute;
  z-index: 0;
  top: 8.94rem;
  left: 55%;
  transform: translate(-50%, 0%);
}

.content {
  position: relative;
}

.title-background, .description-background, .image-background {
  visibility: hidden;
}

.row-first {
  display: flex;
  gap: 5rem;
  align-items: center;
}

.row-second {
  display: flex;
}

.image-container .image {
  height: 100%;
  object-fit: cover;
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
  color: #000;
}

.second-image-container {

}

@media screen and (max-width: 1200px) {
  .row-first {
    gap: 4rem;
  }

  .description {
    font-size: 1rem;
    margin-left: 2.25rem;
    margin-right: 2.25rem;
    position: relative;
  }

  .image-container .image {
    width: 100%;
  }

  .first-image-container .image, .second-image-container .image {
    width: 250px;
  }

  .row-first .image-container {
    flex: 2;
  }

  .row-first .title {
    flex: 2;
    position: relative;
  }

  .union {
    visibility: hidden;
  }

  .title-background, .description-background {
    visibility: visible;
    background: white;
    z-index: -1;
    position: absolute;
    width: 300%;
    height: 16rem;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

@media screen and (max-width: 990px) {
  .row-first {
    flex-direction: column;
    gap: 3rem;
  }

  .title {
    text-align: center;
    margin-left: 6rem;
    margin-right: 6rem;
    flex: auto;
  }

  .image-background {
    visibility: visible;
    background: white;
    z-index: -1;
    position: absolute;
    width: 300%;
    height: 14rem;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -90%);
  }

  .title-background {
    height: 14rem;
    transform: translate(-50%, -70%);
  }

  .description-background {
    visibility: hidden;
  }

  .image-container {
    flex: auto;
    margin-left: 4rem;
    margin-right: 4rem;
    position: relative;
  }

  .content {
    display: flex;
    flex-direction: column;
    gap: 5rem;
  }

  .row-second {
    gap: 3rem;
  }

  .first-image-container {
    align-items: flex-start;
  }

  .description {
    align-items: flex-start;
  }

  .second-image-container {
    position: absolute;
    bottom: 3rem;
    left: 21rem;
  }

  .second-image-container .image {
    width: 9rem;
  }
}

@media screen and (max-width: 640px) {
  .image-container {
    margin-left: 0;
    margin-right: 0;
  }

  .title {
    margin-left: 0;
    margin-right: 0;
  }

  .row-second {
    flex-direction: column;
    gap: 4rem;
  }

  .first-image-container .image {
    width: 9rem;
  }

  .description {
    margin-left: 6rem;
    margin-right: 0;
    font-size: 0.875rem;
    line-height: 150%;
    height: 19rem;
  }

  .second-image-container {
    bottom: 0;
    left: 6rem;
  }

  .second-image-container .image {
    width: 8rem;
  }

  .image-background {
    transform: translate(-50%, -95%);
  }

  .title-background {
    transform: translate(-50%, -45%);
  }
}

@media screen and (max-width: 360px) {
  .description {
    height: 23rem;
  }
}
</style>