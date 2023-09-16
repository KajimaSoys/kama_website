<template>
  <div class="filters-component">
      <div class="filters">

      <!-- Фильтр по форме дивана -->
      <div v-if="filters.sofaForms.length > 1" class="filter">
        <span class="filter-title">Форма:</span>
        <select v-model="filters.currentSofaForms">
          <option value="all">Любая</option>
          <option v-for="form in filters.sofaForms" :key="form" :value="form">
            {{ translations[form] }}
          </option>
        </select>
      </div>

      <!-- Фильтр по типу дивана -->
      <div v-if="filters.sofaTypes.length > 1" class="filter">
        <span class="filter-title">Тип</span>
        <select v-model="filters.currentSofaTypes">
          <option value="all">Любой</option>
          <option v-for="type in filters.sofaTypes" :key="type" :value="type">
            {{ translations[type] }}
          </option>
        </select>
      </div>

      <!-- Фильтр по механизму раскладывания -->
      <div v-if="filters.foldingMechanisms.length > 1" class="filter">
        <span class="filter-title">Механизм раскладывания</span>
        <select v-model="filters.currentFoldingMechanisms">
          <option value="all">Любой</option>
          <option v-for="mechanism in filters.foldingMechanisms" :key="mechanism" :value="mechanism">
            {{ translations[mechanism] }}
          </option>
        </select>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Filters",
  inject: ['backendURL'],
  props: [
      'filters'
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

  }
}
</script>

<style scoped>
.filters-component {
  margin-top: 4rem;
}

.filters{
  display: flex;
  flex-direction: row;
  gap: 1rem;
  justify-content: center;
}

.filter {
  padding: 1rem 2rem;
  background: #E9E9E9;
}

.filter-title {
  color: #8A8A8A;
  font-size: 1.125rem;
}

select {
  padding-left: 0.5rem;
  box-sizing: border-box;
  border: 2px solid #E9E9E9;
  border-radius: 4px;
  background-color: #E9E9E9;
  font-size: 1.125rem;
  color: #212121;
}

select:focus, select:focus-visible {
  border-color: #E9E9E9;
}

select:hover {
  cursor: pointer;
}

option:hover {
  background-color: #E9E9E9;
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