<template>
  <div class="reviews-component">
    <div class="review-max">
      <h2 class="title">
        Отзывы
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
              v-for="(review, reviewIndex) in this.reviews"
              :key="reviewIndex"
          >
            <div class="review">
              <div class="author">
                <div class="image-container" v-if="review.author_photo">
                  <img :src="`${this.backendURL}${this.formattedLink(review.author_photo)}`"
                       alt="Кама - производство мягкой мебели | Фото автора отзыва" class="image"/>
                </div>

                <div class="image-container" v-else>
                  <img src="/images/no-photo.png" alt="Кама - производство мягкой мебели | Фото автора отзыва"
                       class="image"/>
                </div>

                <div class="author-name">
                  {{ review.author }}
                </div>
              </div>

              <div class="review-images" v-if="review.photos.length > 0">
                <div v-for="(photo, photoIndex) in review.photos.slice(0, 5)" class="image-container"
                   @click="openImagePopUp(reviewIndex, photoIndex)">
                  <img :src="`${this.backendURL}${this.formattedLink(photo.photo)}`"
                       alt="Кама - производство мягкой мебели | Фото отзыва" class="image"/>
                </div>
              </div>

              <div class="review-text-wrapper">
                <div :class="{ 'clamped': !isExpanded[reviewIndex] }" class="review-text" v-show="true"
                     v-html="review.review"></div>
                <div v-if="isTooLong[reviewIndex]" @click="togglePopup(review)" class="read-more">
                  Открыть полностью
                </div>
              </div>

            </div>
          </swiper-slide>
        </swiper>
        <div :class="{'swiper-controls': true, 'hidden': this.reviews.length <= 2}">
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

    <ImageSliderPopUp
        :visible="popUpVisible"
        :images="reviews[currentReview] ? reviews[currentReview].photos : []"
        :currentImageIndex="currentImage"
        @closePopUp="closeImagePopUp()"
    />

  </div>
</template>

<script>
import {Navigation, Pagination, Scrollbar, A11y} from 'swiper/modules';
import {Swiper, SwiperSlide} from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import {computed, onBeforeUnmount, onMounted, ref} from "vue";
import ImageSliderPopUp from "../base/ImageSliderPopUp.vue";


export default {
  name: "Reviews",
  components: {
    Swiper,
    SwiperSlide,
    ImageSliderPopUp,
  },
  inject: ['backendURL'],
  props: [
    'reviews'
  ],
  emits: [
    'popUpCall'
  ],
  data() {
    return {
      isReviewExpanded: {},
      shouldShowReadMore: {},
      isExpanded: {},
      isTooLong: {},
      popUpVisible: false,
      currentImage: 0,
      currentReview: 0,
    }
  },
  mounted() {
    this.$nextTick(() => {
      setTimeout(() => {
        const elements = this.$el.querySelectorAll('.review-text');
        elements.forEach((element, index) => {
          this.isTooLong[index] = element.scrollHeight > element.clientHeight;
        });
      }, 1000);
    });
  },
  methods: {
    togglePopup(review) {
      this.$emit('popUpCall', review);
    },
    openImagePopUp(reviewIndex, photoIndex) {
      this.popUpVisible = true;
      this.currentReview = reviewIndex
      this.currentImage = photoIndex
    },
    closeImagePopUp() {
      this.popUpVisible = false;
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
      } else {
        return 2;
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
  computed: {
    formattedLink() {
      return (link) => {
        let newLink = link.replace('http://127.0.0.1:8000', '');
        newLink = newLink.replace('https://kamamebel.com', '');
        return newLink;
      };
    }
  },
}
</script>

<style scoped>
.reviews-component {
  margin-top: 12.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.review-max {
  text-align: center;
  max-width: 74rem;
  width: 100%;
}

.content {
  margin-top: 4rem;
}

.review {
  background: #fff;
  padding: 3rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  height: 20rem;
}

.author {
  display: flex;
  flex-direction: row;
  gap: 1.25rem;
  align-items: center;
}

.author-name {
  text-align: left;
}

.author .image-container {
  height: 3.75rem;
  width: 3.75rem;
  overflow: hidden;
  border-radius: 50%;
}

.review-images .image-container {
  height: 4.375rem;
  width: 4.375rem;
  overflow: hidden;
}

.image-container {
  cursor: pointer;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  aspect-ratio: 1/1;
}

.review-images {
  display: flex;
  flex-direction: row;
  gap: 0.5rem;
}

.review-text-wrapper {
  position: relative;
}

.review-text.clamped {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 0.5rem;
}

.read-more {
  position: absolute;
  color: #000;
  font-size: 1.125rem;
  cursor: pointer;
}

.review-text {
  text-align: left;
  color: #484848;
  font-size: 1.125rem;
}

.swiper-controls {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 50px;
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

.hidden {
  visibility: hidden;
}

@media screen and (max-width: 1200px) {
  .reviews-component {
    margin-top: 9.5rem;
  }

  .author-name {
    font-size: 1.125rem;
  }

  .review-text, .read-more {
    font-size: 1rem;
  }
}

@media screen and (max-width: 990px) {
  .reviews-component {
    margin-top: 7.5rem;
  }

  .content {
    margin-top: 2.5rem;
  }

  .author-name {
    font-size: 1rem;
  }

  .review-text, .read-more {
    font-size: 0.9375rem;
    line-height: 1.7rem;
  }

  .review-text.clamped {
    -webkit-line-clamp: 4;
  }

  .review-images .image-container {
    height: 3.75rem;
    width: 3.75rem;
  }

  .review {
    padding: 2rem;
  }

}

@media screen and (max-width: 640px) {
  .reviews-component {
    margin-top: 6.25rem;
  }

  .content {
    margin-top: 2rem;
  }

  .review-text, .read-more {
    font-size: 0.875rem;
    line-height: 1.7rem;
  }

  .review {
    gap: 1.5rem;
  }

  .review-images .image-container {
    max-height: 3.75rem;
    height: unset;
    width: 3.75rem;
    aspect-ratio: 1/1;
  }
}

@media screen and (max-width: 360px) {

}
</style>