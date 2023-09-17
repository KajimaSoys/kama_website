<template>
  <div :class="{'header-component': true, 'hidden': isHidden}">
    <div class="flex-row">
      <a class="logo" href="/">
        <img :src="`${this.backendURL}${this.header.logo}`" alt="Кама - Мягкая мебель для вашего дома. Логотип." width="140" height="60">
      </a>

      <div class="navigate-links">
        <router-link :to="{ name: 'catalog' }">Каталог</router-link>
        <router-link :to="{ name: 'delivery' }">Доставка и оплата</router-link>
        <a> О компании</a>
        <a> Контакты</a>
        <router-link :to="{ name: 'reviews' }"> Отзывы</router-link>
      </div>

      <div class="number">
        <img src="/icons/phone.svg" alt="" width="18" height="18">
        <span>{{ this.header.number }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  inject: ['backendURL'],
  props: [
      'header'
  ],
  emits: [
  ],
  data() {
    return {
      isHidden: false,
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;

      if (currentScrollPosition < this.lastScrollPosition) {
        this.isHidden = false;
      } else {
        this.isHidden = true;
      }

      this.lastScrollPosition = currentScrollPosition;
    }
  }
}
</script>

<style scoped>
.header-component {
  height: 7rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-bottom: solid 0.1rem #e6e6e6;
  background: #F8F8F8;
  position: sticky;
  top: 0;
  transition: top 0.3s ease-in-out;
  z-index: 100;
}

.hidden {
  top: -7rem;
}

.header-component .flex-row{
  justify-content: space-around;
}

.navigate-links {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2.5rem;
}

.number {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0.75rem;
}

a {
  text-decoration: none;
  color: #484848;;
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