<template>
  <div class="image-slider-component">
    <div class="image-slider-max">
      <div class="swiper-content" v-if="swiperOn">

        <swiper
            :modules="modules"
            :slides-per-view="1"
            :space-between="32"
            :navigation="{ nextEl: '.swiper-button-next-2', prevEl: '.swiper-button-prev-2' }"
            :pagination="{
          el: '.swiper-pagination-2',
          clickable: true,
          bulletClass: 'swiper-pagination-bullet',
          bulletActiveClass: 'swiper-pagination-bullet-active',
          dynamicBullets: true}"
        >
          <swiper-slide
              v-for="(image, index) in this.images"
              :key="index"
          >
            <div class="image-container">
              <img :src="`${this.backendURL}${this.formattedLink(image.image)}`" alt="Кама - производство мягкой мебели | Фото дивана" class="image"/>
            </div>
          </swiper-slide>
        </swiper>
        <div :class="{'swiper-controls': true, 'hidden': this.images && this.images.length < 2}">
          <div class="swiper-button-prev swiper-button-prev-2">
            <svg width="20" height="18" viewBox="0 0 20 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M8.0973 0.156443L0.183064 8.53296L0.182131 8.53401L0.172611 8.54412C-0.0572777 8.78808 -0.0578003 9.2114 0.172625 9.456L0.181719 9.46565L0.182583 9.46662L8.09723 17.8436C8.29484 18.0527 8.58788 18.0522 8.78497 17.8416C9.01494 17.5958 9.01372 17.1747 8.78313 16.9306L1.86931 9.61291H19.4835C19.7116 9.61291 20 9.39746 20 9.00001C20 8.60256 19.7116 8.3871 19.4835 8.3871H1.86919L8.78325 1.06935C9.01382 0.825229 9.01501 0.404166 8.78505 0.158436C8.58785 -0.0522866 8.29489 -0.0526697 8.0973 0.156443Z"
                    fill="black"/>
            </svg>
          </div>
          <div class="swiper-pagination swiper-pagination-2"></div>
          <div class="swiper-button-next swiper-button-next-2">
            <svg width="20" height="18" viewBox="0 0 20 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M11.9027 0.156443L19.8169 8.53296L19.8179 8.53401L19.8274 8.54412C20.0573 8.78808 20.0578 9.2114 19.8274 9.456L19.8183 9.46565L19.8174 9.46662L11.9028 17.8436C11.7052 18.0527 11.4121 18.0522 11.215 17.8416C10.9851 17.5958 10.9863 17.1747 11.2169 16.9306L18.1307 9.61291H0.516543C0.288381 9.61291 0 9.39746 0 9.00001C0 8.60256 0.288382 8.3871 0.516543 8.3871H18.1308L11.2168 1.06935C10.9862 0.825229 10.985 0.404166 11.215 0.158436C11.4121 -0.0522866 11.7051 -0.0526697 11.9027 0.156443Z"
                    fill="black"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="plain-content" v-if="!swiperOn">
        <div
            class="image-container"
            v-for="(image, index) in this.images"
            :key="index"
        >
          <img :src="`${this.backendURL}${this.formattedLink(image.image)}`" alt="Кама - производство мягкой мебели | Фото дивана" class="image"/>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {Navigation, Pagination, Scrollbar, A11y} from 'swiper/modules';
import {Swiper, SwiperSlide} from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

export default {
  name: "ImageSlider",
  components: {
    Swiper,
    SwiperSlide,
  },
  inject: ['backendURL'],
  props: [
    'images'
  ],
  emits: [],
  data() {
    return {
      swiperOn: true
    }
  },
  computed: {
    formattedLink() {
      return (link) => {
        let newLink = link.replace('http://127.0.0.1:8000', '');
        newLink = newLink.replace('https://kamamebel.com', '');
        newLink = newLink.replace('http://kamamebel.com', '');
        return newLink;
      };
    }
  },
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    return {
      onSwiper,
      onSlideChange,
      modules: [Navigation, Pagination, Scrollbar, A11y],
    };
  },
  methods: {
    updateWindowWidth() {
      if (window.innerWidth > 990) {
        this.swiperOn = this
      } else {
        this.swiperOn = false
      }
    },
  },

  mounted() {
    setTimeout(() => {
      const element = document.querySelector('.swiper-button-next.swiper-button-next-2.swiper-button-disabled.swiper-button-lock');
      if (element) {
        element.classList.remove('swiper-button-disabled', 'swiper-button-lock');
      }
    }, 500)

    window.addEventListener('resize', this.updateWindowWidth);
  },
  beforeUnmount() {
    window.addEventListener('resize', this.updateWindowWidth);
  },
}
</script>

<style scoped>
.image-slider-component {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 6.25rem;
  margin-right: 1rem;
  margin-left: 1rem;
}

.image-slider-max {
  max-width: 90rem;
  width: 100%;
  display: flex;
  justify-content: center;
}

.swiper-content {
  position: relative;
  width: 100%;
}

.swiper {
  margin-left: auto;
  margin-right: auto;
  position: relative;
  overflow: hidden;
  overflow: clip;
  list-style: none;
  z-index: 1;
  display: block;
  max-width: 74rem;
}

.swiper-controls {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 50%;
  transform: translate(0, -50%);
}


.swiper-button-next,
.swiper-button-prev {
  height: 38.75rem;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  transform: translate(0%, -47%);
}

.swiper-button-prev {
  left: 0;
}

.swiper-button-next {
  right: 0;
}

.image-container {
  height: 38.75rem;
  overflow: hidden;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .2s ease-in-out;
}


.swiper-button-prev svg, .swiper-button-next svg {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome, Safari, Opera */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Нестандартное свойство */
}

svg path {
  transition: fill 0.2s ease-in-out;
}

.swiper-button-next:after, .swiper-button-prev:after {
  content: none;
}

.swiper-button-next:after, .swiper-button-prev:after {
  font-family: none;
  font-size: none;
  text-transform: none !important;
  letter-spacing: 0;
  font-variant: initial;
  line-height: 1;
}

.swiper-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
  position: inherit;
}

.swiper-pagination-bullets.swiper-pagination-horizontal {
  width: 80px;
  top: 50%;
  transform: translate(-50%, 65%);
}

.hidden {
  visibility: hidden;
}

@media screen and (max-width: 1370px) {
  .swiper {
    max-width: 65rem;
  }
}

@media screen and (max-width: 1200px) {
  .image-container {
    height: 26.375rem;
  }

  .swiper {
    max-width: 50rem;
  }
}

@media screen and (max-width: 990px) {
  .plain-content {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .image-container {
    height: 21.75rem;
  }
}

@media screen and (max-width: 640px) {
  .image-container {
    height: auto;
  }
}

@media screen and (max-width: 360px) {

}
</style>