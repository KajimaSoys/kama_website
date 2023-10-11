<template>
  <div class="review-popup-component">
    <transition name="fade">
      <div v-if="visible" class="popup-background" @click.self="close">
        <div class="popup">
          <div class="popup-max popup-content">
            <swiper
                :navigation="true"
                :modules="modules"
                :keyboard="{enabled: true}"
                class="mySwiper"
                :initial-slide="this.currentImageIndex"
                :space-between="32"
            >
              <swiper-slide
                  v-for="(image, index) in this.images"
                  :key="index"
              >
                <div class="image-container">
                  <img :src="`${this.backendURL}${this.formattedLink(image.photo)}`"
                       alt="Кама - производство мягкой мебели | Фото дивана" class="image"/>
                </div>
              </swiper-slide>
            </swiper>

          </div>

          <button class="close-btn" @click="close" ref="closePopUp">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M8 24L24 8M8 8L24 24" stroke="#9F9F9F" stroke-width="1.5" stroke-linecap="round"
                    stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import {Navigation, Pagination, Scrollbar, A11y, Keyboard} from 'swiper/modules';
import {Swiper, SwiperSlide} from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/keyboard'

export default {
  name: "ImageSliderPopUp",
  components: {
    Swiper,
    SwiperSlide,
    Keyboard
  },
  inject: ['backendURL'],
  props: [
    'visible',
    'images',
    'currentImageIndex'
  ],
  emits: ['closePopUp'],
  data() {
    return {
      review: {}
    }
  },
  methods: {
    close() {
      this.$emit('closePopUp');
    },
  },
  watch: {
    popup_review(newVal) {
      this.review = newVal
    }
  },
  computed: {
    formattedLink() {
      return (link) => {
        let newLink = link.replace('http://127.0.0.1:8000', '');
        newLink = newLink.replace('https://kamamebel.com', '');
        return newLink;
      };
    }
  },
  setup() {
    return {
      modules: [Navigation, Keyboard],
    };
  },
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.popup-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 101;
}

.popup {
  background-color: white;
  padding: 3rem 3rem;
  position: relative;
  z-index: 101;
  width: 85vw;
  height: 80vh;
}

.close-btn {
  position: absolute;
  z-index: 101;
  top: 0;
  right: 0.5rem;
  background: transparent;
  border: none;
  font-size: 3rem;
  cursor: pointer;
}

.close-btn path {
  transition: all 0.1s ease-in-out;
}

.close-btn:hover path {
  stroke: #000;
}

.popup-content {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  align-items: center;
}

.image-container {
  max-height: 80vh;
  display: flex;
  align-items: center;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

:deep(.swiper-button-prev), :deep(.swiper-button-next) {
  width: calc(8rem / 44 * 27);
  height: 110%;
  margin-top: calc(0px - (50% / 2));
  left: unset;
  top: var(--swiper-navigation-top-offset, 39%);
  background: linear-gradient(270deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
  transition: background 0.3s ease-in-out !important;
}

:deep(.swiper-button-next) {
  right: 0;
}

:deep(.swiper-button-prev:hover) {
  background: linear-gradient(270deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, .5) 100%);
}

:deep(.swiper-button-next:hover) {
  background: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, .5) 100%);
}

:deep(.swiper-button-prev:after), :deep(.swiper-button-next:after) {
  font-size: 30px;
}

:deep(.swiper-button-prev:hover:after), :deep(.swiper-button-next:hover:after) {
  color: rgba(255, 255, 255, 1);
}


@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 990px) {

}

@media screen and (max-width: 640px) {
  .popup {
    padding: 2rem 2rem;
    width: 75vw;
  }

  .close-btn {
    top: 0;
    right: 0rem;
    font-size: 2.5rem;
  }

  .close-btn svg {
    width: 24px;
  }
}

@media screen and (max-width: 400px) {

}
</style>