<template>
  <div class="other-variants-component">
    <div class="other-variants-max">
      <h2 class="title">
        Другие варианты исполнения
      </h2>

      <div class="content">
        <router-link
            v-for="sofa in this.otherVariants"
            :to="{ name: 'product', params: { id: sofa.id } }"
            class="variant">
          <div class="image-container">
            <img :src="`${this.backendURL}${sofa.first_image.image}`" :alt="`Кама - производство мягкой мебели | Фото похожего дивана - ${sofa.name}`" class="image"/>
          </div>
          <div class="button">
            <span>{{ this.findDifference(sofa) }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M3 11.9999H21M21 11.9999L14 5M21 11.9999L14 18.9999" stroke="white" stroke-width="1.5"
                    stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </router-link>
      </div>
    </div>

  </div>
</template>

<script>
import Payment from "../deliveryPage/Payment.vue";

export default {
  name: "OtherVariants",
  components: {Payment},
  inject: ['backendURL'],
  props: [
    'otherVariants',
    'sofaForm',
    'sofaType',
    'foldingMechanism',
  ],
  emits: [],
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
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.other-variants-max {
  max-width: 74rem;
  width: 100%;
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

.variant:hover .image {
  transform: scale(1.05);
}

.button {
  display: flex;
  padding: 1rem;
  justify-content: space-between;
  align-items: center;
  background: #212121;

  text-decoration: none;
  transition: background-color 0.5s ease;
}

.variant:hover .button {
  background: #2121212e;
}

.button:before {
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

.variant:hover .button:before {
  clip-path: inset(-10% 0 0 -10%);
}

.button span {
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

.arrow-right {
  flex-shrink: 0;
  position: relative;
  overflow: visible;
}

.variant:hover span {
  background-position: 0 100%;
}

.button path {
  transition: stroke 0.4s ease;
}

.variant:hover path {
  stroke: #212121;
}

@media screen and (max-width: 1200px) {
  .content {
    margin-top: 2rem;
  }

  .image-container {
    height: 11rem;
  }
}

@media screen and (max-width: 990px) {
  .other-variants-component {
    margin-top: 7.5rem;
  }

  h2.title {
    text-align: center;
  }

  .content {
    flex-direction: column;
    max-width: 40rem;
    margin-left: auto;
    margin-right: auto;
    gap: 2rem;
  }

  .image-container {
    height: 17rem;
  }
}

@media screen and (max-width: 640px) {
  .other-variants-component {
    margin-top: 6.25rem;
  }

  .image-container {
    height: 45vw;
  }

  .button span {
    font-size: 1rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>