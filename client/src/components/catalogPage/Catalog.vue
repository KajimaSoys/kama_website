<template>
  <div class="catalog-component">
    <div class="catalog-max">
      <div class="model-list" v-if="filteredSofas.length">
        <router-link :to="{ name: 'product', params: { id: sofa.id } }" class="model" v-for="sofa in filteredSofas">
          <div class="image-container">
            <img :src="`${this.backendURL}${sofa.first_image.image}`" :alt="`Кама - производство мягкой мебели | ${sofa.name}`" class="image"/>
          </div>
          <div class="text-container">
            <h2 class="model-name-hover">
              {{ sofa.name }}
            </h2>
            <div class="model-description-hover" v-html="sofa.short_description">
            </div>
            <div class="model-price-hover">
              {{ this.formattedPrice(sofa.price) }}
            </div>
            <h2 class="model-name">
              {{ sofa.name }}
            </h2>
          </div>
        </router-link>
      </div>

      <div class="no-model" v-else>
        <p>К сожалению, по вашему запросу диванов не найдено. Попробуйте изменить параметры фильтрации.</p>
      </div>
    </div>


    <div class="union">
      <svg xmlns="http://www.w3.org/2000/svg" width="1716" height="656" viewBox="0 0 1716 656" fill="none">
        <path
            d="M1147.71 186.541C1197.49 54.9356 1331.2 -19.4501 1473.83 4.86829C1615.71 29.1867 1715.26 142.911 1716 281.669V656H1496.86V282.384C1496.86 228.741 1454.51 215.866 1435.94 213.005C1418.11 209.429 1373.54 207.998 1354.23 258.066L1206.37 656H973.279L1147.71 186.541Z"
            fill="white"/>
        <path
            d="M475.371 80.5768C617.257 104.18 716.8 218.62 716.8 357.378V656H498.4V357.378C498.4 304.449 456.057 290.859 437.486 287.998C419.657 285.137 375.086 283.707 355.772 333.774L200.598 656H-33.0283L150 260.819C199.029 130.644 332.743 56.2584 475.371 80.5768Z"
            fill="white"/>
      </svg>
    </div>

  </div>
</template>

<script>
export default {
  name: "Catalog",
  inject: ['backendURL'],
  props: [
    'sofas',
    'filters'
  ],
  emits: [],
  methods: {
    formattedPrice(price) {
      let integerPart = parseInt(price).toString();
      integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
      return `от ${integerPart} ₽`;
    }
  },
  computed: {
    filteredSofas() {
      return this.sofas.filter(sofa => {
        let isFormValid = this.filters.currentSofaForms === 'all' || sofa.sofa_form === this.filters.currentSofaForms;
        let isTypeValid = this.filters.currentSofaTypes === 'all' || sofa.sofa_type === this.filters.currentSofaTypes;
        let isMechanismValid = this.filters.currentFoldingMechanisms === 'all' || sofa.folding_mechanism === this.filters.currentFoldingMechanisms;

        return isFormValid && isTypeValid && isMechanismValid;
      });
    }
  },
}
</script>

<style scoped>
.catalog-component {
  margin-top: 4rem;
  margin-bottom: 30rem;

  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  position: relative;
}

.catalog-max {
  max-width: 74rem;
  width: 100%;
  margin-left: 1rem;
  margin-right: 1rem;
}

.model-list {
  display: grid;
  position: relative;

  grid-template-columns: 1fr 1fr;

  grid-column-gap: 1rem;
  grid-row-gap: 1rem;
}

.model {
  position: relative;
  cursor: pointer;
}

.image-container {
  height: 28rem;
  overflow: hidden;
  position: relative;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .2s ease-in-out;
}

.text-container {
  position: absolute;
  top: 0;
  height: 100%;
  width: 100%;
  text-align: center;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.00) 60%, rgba(0, 0, 0, 0.20) 100%);
  transition: background-color 0.2s ease-in-out;
}

.model-name {
  color: #FFF;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  width: 100%;
  position: absolute;
  bottom: 2rem;
  transition: opacity 0.2s ease-in-out;
  opacity: 1;
}

.model-name-hover {
  color: #FFF;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  width: 100%;
  position: absolute;
  bottom: 18.5rem;
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
}

.model-description-hover {
  color: #FFF;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
  top: 11.5rem;
  position: relative;
  width: 60%;
  margin-left: auto;
  margin-right: auto;
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
}

.model-price-hover {
  color: #FFF;
  text-align: center;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
  width: 100%;
  position: absolute;
  top: 18.5rem;
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
}

.model:hover .text-container {
  background: rgba(0, 0, 0, 0.60);
}

.model:hover .model-description-hover, .model:hover .model-price-hover, .model:hover .model-name-hover {
  opacity: 1;
}

.model:hover .model-name {
  opacity: 0;
}

.model:hover .image {
  transform: scale(1.05);
}

.no-model {
  width: 80%;
  text-align: center;
  margin: 0 auto;
}

.union {
  position: absolute;
  z-index: -1;
  bottom: -49rem;
  left: 0;
}

@media screen and (max-width: 1200px) {
  .catalog-component {
    margin-bottom: 25rem;
  }

  .union {
    bottom: -42rem;
  }

  .union svg {
    width: 100%;
  }

  .image-container {
    height: 22.875rem;
  }

  .model-name-hover {
    bottom: 14.5rem;
  }

  .model-description-hover {
    top: 10.5rem;
  }

  .model-price-hover {
    top: 16.5rem;
  }
}

@media screen and (max-width: 990px) {
  .catalog-component {
    margin-bottom: 21rem;
  }

  .union {
    bottom: -38rem;
  }

  .model-name {
    font-size: 1.125rem;
    bottom: 1rem;
  }

  .model-name-hover {
    font-size: 1.125rem;
    bottom: 10rem;
  }

  .model-description-hover {
    font-size: 1rem;
    width: 85%;
    top: 5.5rem;
  }

  .model-price-hover {
    font-size: 1rem;
    top: 10.5rem;
  }

  .image-container {
    height: 14.25rem;
  }

  .no-model {
    font-size: 1rem;
  }
}

@media screen and (max-width: 640px) {
  .catalog-component {
    margin-bottom: 12rem;
  }

  .union {
    bottom: -30rem;
  }

  .model-list {
    grid-template-columns: auto;
  }

  .image-container {
    height: 15.75rem;
  }

  .model-name {
    font-size: 1rem;
    bottom: 1rem;
  }

  .model-name-hover {
    font-size: 1rem;
    bottom: 11rem;
  }

  .model-description-hover {
    font-size: 0.875rem;
    top: 6.5rem;
  }

  .model-price-hover {
    font-size: 0.875rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>