<template>
  <div class="review-popup-component">
  <transition name="fade">
    <div v-if="visible" class="popup-background" @click.self="close">
      <div class="popup">
        <div class="popup-max popup-content">
          <div class="review">
            <div class="author">
              <div class="image-container">
                <img :src="`${this.backendURL}${this.formattedLink(this.review.author_photo)}`" alt="" class="image"/>
              </div>

              <div class="author-name">
                {{ this.review.author }}
              </div>
            </div>

            <div class="review-images">
              <a v-for="photo in this.review.photos" class="image-container" :href="`${this.backendURL}${this.formattedLink(photo.photo)}`" target="_blank">
                <img :src="`${this.backendURL}${this.formattedLink(photo.photo)}`" alt="" class="image"/>
              </a>
            </div>

            <div class="review-text-wrapper">
              <div class="review-text" v-show="true" v-html="this.review.review"></div>
            </div>

          </div>
        </div>

        <button class="close-btn" @click="close" ref="closePopUp">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
            <path d="M8 24L24 8M8 8L24 24" stroke="#9F9F9F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>
    </div>
  </transition>
  </div>
</template>

<script>
export default {
  name: "ReviewPopup",
  inject: ['backendURL'],
  props: [
      'popup_review',
      'visible'
  ],
  emits: [
  ],
  data() {
    return {
      review: {}
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
  },
  watch: {
    popup_review(newVal){
      this.review = newVal
    }
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
}

.close-btn {
  position: absolute;
  z-index: 101;
  top: 1rem;
  right: 1rem;
  background: transparent;
  border: none;
  font-size: 3rem;
  cursor: pointer;
}

.close-btn path{
  transition: all 0.1s ease-in-out;
}

.close-btn:hover path{
  stroke: #000;
}

.popup-content{
  max-width: 50rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  align-items: center;
}

.review {
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 2rem;
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

.review-text {
  text-align: left;
  color: #484848;
  font-size: 1.125rem;
}
</style>