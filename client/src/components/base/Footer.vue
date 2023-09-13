<template>
  <div class="footer-component">
    <div class="grid-row">
      <a class="logo" href="/">
        <img :src="`${this.backendURL}${this.footer.logo}`" alt="Кама - Мягкая мебель для вашего дома. Логотип." width="140" height="60">
      </a>

      <div class="navigate-links">
        <a>Каталог</a>
        <a>Отзывы</a>
        <a>Контакты</a>
        <a>Доставка и оплата</a>
        <a>О компании</a>
      </div>

      <div class="number">
        <img src="icons/phone.svg" alt="" width="18" height="18">
        <span>{{ this.footer.number }}</span>
      </div>

      <a class="additional">
        Политика конфиденциальности
      </a>

      <div class="additional">
        Договор оферты
      </div>

      <div class="developers">
        <a>Дизайн - Максим Шемякин</a>
        <a>Разработка - Вадим Гришин</a>
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
  ],
  methods: {

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

.number {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0.75rem;
  color: #212121;
}

.additional {
  color: #9F9F9F;
  font-size: 1rem;
  display: flex;
  height: 100%;
  align-items: flex-end;
}

.developers {
  color: #9F9F9F;
  font-size: 0.875rem;
  display: flex;
  flex-direction: column;;
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