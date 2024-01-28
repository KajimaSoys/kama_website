<template>
  <div class="footer-component">

    <div class="footer-max">
      <div class="grid-row">
        <router-link class="logo" to="/">
          <img :src="`${this.backendURL}${this.footer.logo}`" alt="Кама - производство мягкой мебели | Логотип"
               width="140" height="60" loading="lazy">
        </router-link>

        <div class="navigate-links">
          <router-link :to="{ name: 'catalog' }" class="menu-item">Каталог</router-link>
          <router-link :to="{ name: 'reviews' }" class="menu-item"> Отзывы</router-link>
          <a class="menu-item" @click="this.scrollToElement('contacts_block')"> Контакты</a>
          <router-link :to="{ name: 'delivery' }" class="menu-item">Доставка и оплата</router-link>
          <a class="menu-item" @click="this.scrollToElement('about_block')"> О компании</a>
        </div>

        <div class="number" @click="this.$emit('popUpCall')">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path
                d="M3.59469 9.75C2.58134 8.0332 1.91091 6.03524 1.63816 3.81089C1.62176 3.67717 1.61356 3.61031 1.61516 3.47621C1.62604 2.56117 2.4411 1.64007 3.34801 1.5179C3.48091 1.5 3.59274 1.5 3.81641 1.5V1.5C4.05108 1.5 4.16842 1.5 4.27281 1.51099C5.03259 1.59096 5.68043 2.09678 5.94229 2.81448C5.97827 2.91309 6.00673 3.02693 6.06365 3.25459L6.11235 3.44941C6.25096 4.00385 6.32027 4.28107 6.34993 4.55074C6.44905 5.45201 6.23903 6.36023 5.75428 7.12649C5.60925 7.35575 5.42527 7.5744 5.05732 8.0117L3.59469 9.75ZM3.59469 9.75C4.68602 11.5989 6.17506 13.1217 7.9934 14.25M7.9934 14.25C9.76659 15.3503 11.8529 16.0754 14.1889 16.3618C14.3228 16.3782 14.3897 16.3864 14.5238 16.3848C15.4388 16.374 16.3599 15.5589 16.4821 14.652C16.5 14.5191 16.5 14.3997 16.5 14.1609V14.1609C16.5 13.9413 16.5 13.8316 16.489 13.7272C16.409 12.9674 15.9032 12.3196 15.1855 12.0577C15.0869 12.0217 14.9731 11.9933 14.7454 11.9364L14.4711 11.8678C13.8587 11.7147 13.5524 11.6381 13.2521 11.6097C12.4679 11.5354 11.6792 11.6944 10.985 12.0666C10.7191 12.2091 10.4664 12.3983 9.96105 12.7767L7.9934 14.25Z"
                stroke="#484848" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span>{{ this.footer.number }}</span>
        </div>

        <div class="additional policy">
          <router-link :to="{ name: 'policy' }">Политика конфиденциальности</router-link>
        </div>

        <div class="additional offer">
          <router-link :to="{ name: 'terms' }">Положения и условия</router-link>
        </div>

        <div class="developers">
          <a href="https://vk.com/shemyakin_er" target="_blank">Дизайн - Максим Шемякин</a>
          <a href="https://t.me/OneDudeAdam" target="_blank">Разработка - Вадим Гришин</a>
          <a href="https://ru.kajimacode.com" target="_blank">Copyright © {{ new Date().getFullYear() }} KajimaCode</a>
        </div>


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

      if (this.$route.path === "/") {
        element.scrollIntoView({behavior: "smooth"});

        this.isBurgerMenuOpen = false;
        if (this.isBurgerMenuOpen) {
          document.body.style.overflow = "hidden";
        } else {
          document.body.style.overflow = "";
        }
      } else {
        this.$router.push({path: "/", hash: `#${elementId}`});
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
  align-items: center;
  padding-left: 1rem;
  padding-right: 1rem;
}

.footer-max {
  max-width: 74rem;
  width: 100%;
}

.footer-component .grid-row {
  display: grid;
  grid-template-columns: 1fr 2.5fr 1fr;
  gap: 1.5rem 1.5rem;
  justify-items: start;
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
  color: #b4b4b4;
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

.number path {
  transition: stroke 0.2s ease-in-out;
}

.number:hover span {
  color: #b4b4b4;
}

.number:hover path {
  stroke: #b4b4b4;
}

.additional {
  color: #9F9F9F;
  font-size: 1rem;
  display: flex;
  height: 100%;
  align-items: flex-end;
}

.additional a {
  text-decoration: none;
  color: #9F9F9F;
  transition: color 0.2s ease-in-out;
}

.additional a:hover {
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

.developers a:hover {
  color: #000;
}

@media screen and (max-width: 1200px) {
  .logo img {
    width: 7.5rem;
  }

  .navigate-links {
    gap: 0 2rem;
  }

  .footer-component .grid-row {
    gap: 1.5rem 0.5rem;
  }

  .policy {
    grid-area: 2 / 2 / 2 / 2;
  }

  .offer {
    grid-area: 2 / 1 / 2 / 1;
  }

  .developers {
    grid-area: 2 / 3 / 2 / 3;
  }
}

@media screen and (max-width: 990px) {
  .footer-component {
    height: 41.25rem;
  }

  .footer-component .grid-row {
    grid-template-columns: none;
    justify-items: center;
    gap: 0;
  }

  .logo {
    grid-area: 1 / 1 / 1 / 1;
    height: 60px;
  }

  .navigate-links {
    grid-area: 2 / 1 / 2 / 1;
    grid-template-columns: none;
    justify-items: center;
    margin-top: 2rem;
  }

  .navigate-links a:nth-child(1) {
    order: 1;
  }

  .navigate-links a:nth-child(2) {
    order: 3;
  }

  .navigate-links a:nth-child(3) {
    order: 5;
  }

  .navigate-links a:nth-child(4) {
    order: 2;
  }

  .navigate-links a:nth-child(5) {
    order: 4;
  }

  .number {
    grid-area: 3 / 1 / 3 / 1;
    margin-top: 2.5rem;
  }

  .policy {
    grid-area: 4 / 1 / 4 / 1;
    margin-top: 2rem;
    text-align: center;
  }

  .offer {
    grid-area: 5 / 1 / 5 / 1;
    margin-top: 1rem;
  }

  .developers {
    grid-area: 6 / 1 / 6 / 1;
    margin-top: 4rem;
    text-align: center;
  }
}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 360px) {

}
</style>