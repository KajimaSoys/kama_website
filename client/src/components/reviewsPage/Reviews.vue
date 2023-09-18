<template>
  <div class="reviews-component">
    <h1 class="title">
      Отзывы
    </h1>

    <div class="content">
      <div class="review" v-for="(review, index) in this.reviews">
        <div class="author">
          <div class="image-container">
            <img :src="`${this.backendURL}${this.formattedLink(review.author_photo)}`" alt="" class="image"/>
          </div>

          <div class="author-name">
            {{ review.author }}
          </div>
        </div>

        <div class="review-images">
          <a v-for="photo in review.photos" class="image-container" :href="`${this.backendURL}${this.formattedLink(photo.photo)}`" target="_blank">
            <img :src="`${this.backendURL}${this.formattedLink(photo.photo)}`" alt="" class="image"/>
          </a>
        </div>

        <div class="review-text-wrapper">
          <div :class="{ 'clamped': !isExpanded[index] }" class="review-text" v-show="true" v-html="review.review"></div>
          <div v-if="isTooLong[index]" @click="togglePopup(review)" class="read-more">
            Открыть полностью
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Reviews",
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
    }
  },
  mounted() {
    this.$nextTick(() => {
      setTimeout(() => {
        const elements = this.$el.querySelectorAll('.review-text');
        elements.forEach((element, index) => {
          this.isTooLong[index] = element.scrollHeight > element.clientHeight;
          console.log(this.isTooLong[index])
        });
      }, 1000);
    });
  },
  methods: {
    togglePopup(review) {
      this.$emit('popUpCall', review);
    },
  },
  computed: {
    formattedLink(){
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
  margin-left: 23rem;
  margin-right: 23rem;
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

.review-images .image-container {
  height: 4.375rem;
  width: 4.375rem;
  overflow: hidden;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
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

@media screen and (max-width: 1200px){

}

@media screen and (max-width: 990px) {

}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 360px) {

}
</style>