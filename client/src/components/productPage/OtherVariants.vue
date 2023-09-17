<template>
  <div class="other-variants-component">
    <h2 class="title">
      Другие варианты исполнения
    </h2>

    <div class="content">
      <router-link
          v-for="sofa in this.otherVariants"
          :to="{ name: 'product', params: { id: sofa.id } }"
          class="variant">
        <div class="image-container">
            <img :src="`${this.backendURL}${sofa.first_image.image}`" alt="" class="image"/>
        </div>
        <div class="button">
          <span>{{ this.findDifference(sofa) }}</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M3 11.9999H21M21 11.9999L14 5M21 11.9999L14 18.9999" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "OtherVariants",
  inject: ['backendURL'],
  props: [
      'otherVariants',
      'sofaForm',
      'sofaType',
      'foldingMechanism',
  ],
  emits: [
  ],
  data() {
    return {
      translations: {
        straight: 'Прямой',
        corner: 'Угловой',
        'p-shaped': 'П-образный',
        folding: 'Раскладной',
        non_folding: 'Нераскладной',
        'tik-tac': 'Тик-так',
        dolphin: 'Дельфин',
      },
    }
  },
  methods: {
    findDifference(model) {
      // Проверка первого параметра (форма дивана)
      if (model.sofa_form !== this.sofaForm) {
        return this.translations[model.sofa_form];
      }
      // Проверка второго параметра (тип дивана)
      if (model.sofa_type !== this.sofaType) {
        return this.translations[model.sofa_type];
      }
      // Проверка третьего параметра (механизм складывания)
      if (model.folding_mechanism !== this.foldingMechanism) {
        return 'Механизм - ' + this.translations[model.folding_mechanism];
      }
      // Если все параметры совпадают, возвращаем форму дивана
      return this.translations[this.sofaForm];
    },
  }
}
</script>

<style scoped>
.other-variants-component {
  margin-top: 10rem;
  margin-left: 23rem;
  margin-right: 23rem;
}

.content {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin-top: 4rem;
}

h2.title {
  color: #212121;
  line-height: normal;
}

.variant {
  text-decoration: none;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex-basis: 32%;
}

.image-container {
  height: 13.625rem;
  overflow: hidden;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .2s ease-in-out;
}

.button {
  display: flex;
  padding: 1rem;
  justify-content: space-between;
  align-items: center;
  background: #212121;
}

.button span {
  color: #FFF;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
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