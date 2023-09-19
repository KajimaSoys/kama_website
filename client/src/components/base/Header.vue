<template>
  <div :class="{'header-component': true, 'hidden': isHidden}">
    <div class="flex-row">
      <router-link class="logo" to="/">
        <img :src="`${this.backendURL}${this.header.logo}`" alt="Кама - Мягкая мебель для вашего дома. Логотип." width="140" height="60">
      </router-link>

      <div class="navigate-links">
        <router-link :to="{ name: 'catalog' }" class="menu-item">Каталог</router-link>
        <router-link :to="{ name: 'delivery' }" class="menu-item">Доставка и оплата</router-link>
        <a class="menu-item" @click="this.scrollToElement('about_block')"> О компании</a>
        <a class="menu-item" @click="this.scrollToElement('contacts_block')"> Контакты</a>
        <router-link :to="{ name: 'reviews' }" class="menu-item"> Отзывы</router-link>
      </div>

      <div class="number" @click="this.$emit('popUpCall')">
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
      'popUpCall'
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
    },
    scrollToElement(elementId) {
      const element = document.getElementById(elementId);

      if (this.$route.path === "/"){
        element.scrollIntoView({ behavior: "smooth" });

        this.isBurgerMenuOpen = false;
        if (this.isBurgerMenuOpen) {
          document.body.style.overflow = "hidden";
        } else {
          document.body.style.overflow = "";
        }
      } else {
        this.$router.push({ path: "/", hash: `#${elementId}` });
      }
    },
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
  cursor: pointer;
}

.number span {
  transition: color 0.2s ease-in-out;
}

a {
  text-decoration: none;
  color: #484848;
}

.menu-item{
  text-decoration: none;
  color: #484848;
  cursor: pointer;
  position: relative;
  transition: color 0.4s ease;
}

.menu-item:hover{
  color: #000;
}

.menu-item:before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  right: 50%;
  background: #000;
  height: 2px;
  transition: all .4s ease;
}

.menu-item:hover:before {
  left: 0;
  right: 0;
}

.number:hover span {
  color: #000;
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