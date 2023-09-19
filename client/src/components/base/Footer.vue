<template>
  <div class="footer-component">
    <div class="grid-row">
      <router-link class="logo" to="/">
        <img :src="`${this.backendURL}${this.footer.logo}`" alt="Кама - Мягкая мебель для вашего дома. Логотип." width="140" height="60">
      </router-link>

      <div class="navigate-links">
        <router-link :to="{ name: 'catalog' }" class="menu-item">Каталог</router-link>
        <router-link :to="{ name: 'reviews' }" class="menu-item"> Отзывы</router-link>
        <a class="menu-item" @click="this.scrollToElement('contacts_block')"> Контакты</a>
        <router-link :to="{ name: 'delivery' }" class="menu-item">Доставка и оплата</router-link>
        <a class="menu-item" @click="this.scrollToElement('about_block')"> О компании</a>
      </div>

      <div class="number" @click="this.$emit('popUpCall')">
        <img src="/icons/phone.svg" alt="" width="18" height="18">
        <span>{{ this.footer.number }}</span>
      </div>

      <div class="additional">
        <router-link :to="{ name: 'policy' }">Политика конфиденциальности</router-link>
      </div>

      <div class="additional">
        Договор оферты
      </div>

      <div class="developers">
        <a href="https://vk.com/shemyakin_er" target="_blank">Дизайн - Максим Шемякин</a>
        <a href="https://t.me/OneDudeAdam" target="_blank">Разработка - Вадим Гришин</a>
        <a href="https://ru.kajimacode.com" target="_blank">Copyright © {{ new Date().getFullYear() }} KajimaCode</a>
      </div>


    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  inject: ['backendURL'],
  props: [
      'footer'
  ],
  emits: [
      'popUpCall'
  ],
  methods: {
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
.footer-component {
  height: 19.8125rem;
  background: #FFF;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.footer-component .grid-row{
  display: grid;
  grid-template-columns: 1fr 2.5fr 1fr;
  gap: 1.5rem 1.5rem;
  justify-items: start;
  margin-left: 23rem;
  margin-right: 23rem;
  align-items: start;
}

.navigate-links {
  display: grid;
  align-items: center;
  gap: 0 4rem;
  grid-template-columns: 1fr 1fr 1fr;
}

.navigate-links a {
  text-decoration: none;
  color: #484848;;
  cursor: pointer;
  transition: 0.2s ease-in-out;
}

.menu-item:hover {
  color: #000;
}

.number {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0.75rem;
  color: #212121;
  cursor: pointer;
}

.number span {
  transition: color 0.2s ease-in-out;
}

.additional {
  color: #9F9F9F;
  font-size: 1rem;
  display: flex;
  height: 100%;
  align-items: flex-end;
  cursor: pointer;
}

.additional a {
  text-decoration: none;
  color: #9F9F9F;
  transition: color 0.2s ease-in-out;
}

.additional:hover a {
  color: #000;
}

.developers {
  display: flex;
  flex-direction: column;;
}

.developers a {
  color: #9F9F9F;
  font-size: 0.875rem;
  text-decoration: none;
  transition: color 0.2s ease-in-out;
}

.developers a:hover{
  color: #000;
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