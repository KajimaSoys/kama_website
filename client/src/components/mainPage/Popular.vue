<template>
  <div class="popular-component">
    <div class="popular-max">
      <h2 class="title">
        Популярные модели
      </h2>
      <div class="content">

        <swiper
            :modules="modules"
            :slides-per-view="slidesPerView"
            :space-between="16"
            :navigation="{ nextEl: '.swiper-button-next-2', prevEl: '.swiper-button-prev-2' }"
            :pagination="{ el: '.swiper-pagination-2', clickable: true, bulletClass: 'swiper-pagination-bullet', bulletActiveClass: 'swiper-pagination-bullet-active' }"
        >
          <swiper-slide
              v-for="(model, index) in this.popular_models"
              :key="index"
          >
            <router-link :to="{ name: 'product', params: { id: model.sofa.id } }" class="model">
              <div class="background">
                <div class="image-container">
                  <img :src="`${this.backendURL}${model.sofa.first_image.image}`"
                       :alt="`Кама - производство мягкой мебели | ${model.sofa.name}`" class="image" loading="lazy"/>
                </div>

                <div class="info-container">
                  <div class="model-title">
                    {{ model.sofa.name }}
                  </div>

                  <div class="model-description" v-html="model.sofa.short_description">
                  </div>

                  <div class="model-price">
                    {{ this.formattedPrice(model.sofa.price) }}
                  </div>
                </div>
              </div>

            </router-link>
          </swiper-slide>
        </swiper>
        <div class="swiper-controls">
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

import {ref, computed, onMounted, onBeforeUnmount} from 'vue';

export default {
  name: "Popular",
  components: {
    Swiper,
    SwiperSlide,
  },
  inject: ['backendURL'],
  props: [
    'popular_models'
  ],
  emits: [],
  methods: {
    formattedPrice(price) {
      let integerPart = parseInt(price).toString();
      integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
      return `от ${integerPart} ₽`;
    }
  },
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };

    const windowWidth = ref(window.innerWidth);
    const slidesPerView = computed(() => {
      if (windowWidth.value < 641) {
        return 1;
      } else if (windowWidth.value < 991) {
        return 2;
      } else {
        return 3;
      }
    });
    const updateWindowWidth = () => {
      windowWidth.value = window.innerWidth;
    };

    onMounted(() => {
      window.addEventListener('resize', updateWindowWidth);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', updateWindowWidth);
    });

    return {
      onSwiper,
      onSlideChange,
      slidesPerView,
      modules: [Navigation, Pagination, Scrollbar, A11y],
    };
  },
  computed: {}
}
</script>

<style scoped>
.popular-component {
  margin-top: 12.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.popular-max {
  text-align: center;
  max-width: 74rem;
  width: 100%;
}

.title {

}

.content {
  margin-top: 4rem;
}

.model {
  cursor: pointer;
  text-decoration: none;
}

.background {
  background: #F8F8F8;
  transition: background-color 0.2s ease-in-out;
}

.model:hover .background {
  background: #fff;
}

.model:hover .image {
  transform: scale(1.05);
}

.image-container {
  height: 12.8125rem;
  overflow: hidden;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .2s ease-in-out;
}

.model-title {
  margin-top: 2rem;
  margin-bottom: 0.5rem;
  color: #000;
  padding-left: 1rem;
  padding-right: 1rem;
}

.info-container {
  height: 15rem;
  flex-direction: column;
  display: flex;
  align-items: center;
  position: relative;
}

.model-description {
  color: #484848;
  font-size: 1.125rem;
  max-width: 80%;
}

.model-price {
  color: #212121;
  font-size: 1.125rem;
  position: absolute;
  bottom: 1rem;
}

.swiper-controls {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 3rem;
  flex-direction: row;
  gap: 3rem;
}


.swiper-button-next,
.swiper-button-prev {
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: inherit;
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
  width: inherit;
  visibility: hidden;
}


@media screen and (max-width: 1200px) {
  .popular-component {
    margin-top: 9.5rem;
  }

  .model-title {
    font-size: 1.125rem;
  }

  .model-description, .model-price {
    font-size: 1rem;
  }

  .swiper-controls {
    margin-top: 2rem;
  }
}

@media screen and (max-width: 990px) {
  .popular-component {
    margin-top: 7.5rem;
  }

  .popular-max {
    max-width: 45rem;
  }

  .content {
    margin-top: 3rem;
  }
}

@media screen and (max-width: 640px) {
  .popular-component {
    margin-top: 6.25rem;
  }

  .popular-max {
    max-width: 30rem;
  }

  .content {
    margin-top: 2rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>