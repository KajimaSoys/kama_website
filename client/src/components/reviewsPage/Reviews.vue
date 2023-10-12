<template>
  <div class="reviews-component">
    <div class="reviews-max">
      <h1 class="title">
        Отзывы
      </h1>

      <div class="content">
        <div class="review" v-for="(review, reviewIndex) in this.reviews">
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

          <ImageSliderPopUp
              :visible="popUpVisible[reviewIndex]"
              :images="review.photos"
              :currentImageIndex="currentImage"
              @closePopUp="closeImagePopUp(reviewIndex)"
          />

        </div>
      </div>

      <div class="button-container">
        <div class="review-button">
            <span class="button-text">
              Оставить отзыв
            </span>

          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none">
                <path d="M12 2V22M2 12H22" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
              </svg>
        </div>

      </div>
    </div>


  </div>
</template>

<script>
import ImageSliderPopUp from "../base/ImageSliderPopUp.vue";

export default {
  name: "Reviews",
  inject: ['backendURL'],
  components: {
    ImageSliderPopUp,
  },
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
      popUpVisible: {},
      currentImage: 0
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
      this.popUpVisible[reviewIndex] = true;
      this.currentImage = photoIndex
    },
    closeImagePopUp(reviewIndex) {
      this.popUpVisible[reviewIndex] = false;
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
}
</script>

<style scoped>
.reviews-component {
  margin-top: 6.25rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.reviews-max {
  text-align: center;
  max-width: 74rem;
  width: 100%;
}

h1.title {
  text-align: center;
}

.content {
  margin-top: 4rem;

  display: grid;
  position: relative;
  grid-template-columns: 1fr 1fr;
  grid-column-gap: 1rem;
  grid-row-gap: 1rem;
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

.author .image-container {
  height: 3.75rem;
  width: 3.75rem;
  overflow: hidden;
  border-radius: 50%;
}

.author-name {
  text-align: left;
}

.review-images .image-container {
  height: 4.375rem;
  width: 4.375rem;
  overflow: hidden;
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

.button-container {
  position: sticky;
  bottom: 4rem;
  margin-top: 4rem;
  width: 24rem;
  margin-left: auto;
  margin-right: auto;
  cursor: pointer;
}

.review-button {
  display: flex;
  height: 3rem;
  padding: 1rem 2rem;
  justify-content: space-between;
  align-items: center;
  background: #212121;
  text-decoration: none;

  position: relative;
  transition: background-color 0.5s ease;
}

.review-button:hover {
  background: #21212100;
}


.review-button:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100%;
  background: #E6E6E6;
  z-index: 0;
  clip-path: inset(-1% 100% -1% 0);
  transition: clip-path 0.5s ease;
}

.review-button:hover:before {
  clip-path: inset(-10% 0 0 -10%);
}

.review-button span {
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

svg {
  flex-shrink: 0;
  position: relative;
  overflow: visible;
}

.review-button:hover span {
  background-position: 0 100%;
}

.review-button path {
  transition: stroke 0.4s ease;
}

.review-button:hover path {
  stroke: #212121;
}


@media screen and (max-width: 1200px) {
  .reviews-component {
    margin-top: 4rem;
  }

  .content {

  }

  .author-name {
    font-size: 1.125rem;
  }

  .review-text, .read-more {
    font-size: 1rem;
  }

}

@media screen and (max-width: 990px) {
  .content {
    grid-template-columns: repeat(2, minmax(0, 1fr));;
  }

  .author-name {
    font-size: 1rem;
    text-align: left;
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

  .review-images .image-container {
    max-height: 3.75rem;
    height: unset;
    width: 3.75rem;
    aspect-ratio: 1/1;
  }

  .button-container {
    width: 29rem;
  }

  .review-button {

    padding: 1rem 1.5rem;
  }

  .review-button span {
    font-size: 1rem;
  }
}

@media screen and (max-width: 640px) {
  .reviews-component {
    margin-top: 2rem;
  }

  .content {
    margin-top: 2rem;
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }

  .review-text, .read-more {
    font-size: 0.875rem;
    line-height: 1.7rem;
  }

  .review {
    gap: 1.5rem;
    height: auto;
  }

  .review-text.clamped {
    margin-bottom: 1rem;
  }

  .read-more {
    bottom: -1rem;
  }

  .button-container {
    width: 100%;
    margin-top: 1rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>