<template>
  <div class="filters-component">
    <div class="filters">

      <!-- Фильтр по форме дивана -->
      <div v-if="filters.sofaForms.length > 1" class="filter">
        <span class="filter-title">Форма:</span>
        <div class="select-container">
          <select v-model="filters.currentSofaForms">
            <option value="all">Любая</option>
            <option v-for="form in filters.sofaForms" :key="form" :value="form">
              {{ translations[form] }}
            </option>
          </select>
        </div>

      </div>

      <!-- Фильтр по типу дивана -->
      <div v-if="filters.sofaTypes.length > 1" class="filter">
        <span class="filter-title">Тип:</span>
        <div class="select-container">
          <select v-model="filters.currentSofaTypes">
            <option value="all">Любой</option>
            <option v-for="type in filters.sofaTypes" :key="type" :value="type">
              {{ translations[type] }}
            </option>
          </select>
        </div>

      </div>

      <!-- Фильтр по механизму раскладывания -->
      <div v-if="filters.foldingMechanisms.length > 1" class="filter">
        <span class="filter-title">Механизм раскладывания:</span>
        <div class="select-container">
          <select v-model="filters.currentFoldingMechanisms">
            <option value="all">Любой</option>
            <option
                v-for="mechanism in filters.foldingMechanisms"
                :key="mechanism"
                :value="mechanism"
                v-if="mechanism"
            >
              {{ translations[mechanism] }}
            </option>
          </select>
        </div>

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
        '': 'Отсутствует',
      },
    }
  },
  methods: {}
}
</script>

<style scoped>
.filters-component {
  margin-top: 4rem;
}

.filters {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  justify-content: center;
}

.filter {
  padding: 0.5rem 0.5rem 0.5rem 2rem;
  background: #E9E9E9;
  line-height: normal;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
}

.filter-title {
  color: #8A8A8A;
  font-size: 1.125rem;
}

select {
  box-sizing: border-box;
  border: 2px solid #E9E9E9;
  border-radius: 4px;
  background-color: #E9E9E9;
  font-size: 1.125rem;
  color: #212121;
  display: inline-block;

  line-height: 1.5em;
  padding: 0.5em 3.5em 0.5em 1em;

  margin: 0;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-image: linear-gradient(45deg, transparent 50%, gray 50%),
  linear-gradient(135deg, gray 50%, transparent 50%),
  linear-gradient(to right, #ccc, #ccc);
  background-position: calc(100% - 20px) calc(1em + 2px),
  calc(100% - 15px) calc(1em + 2px),
  calc(100% - 2.5em) 0.5em;
  background-size: 5px 5px,
  5px 5px,
  1px 1.5em;
  background-repeat: no-repeat;
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

@media screen and (max-width: 1200px) {
  .filter-title {
    font-size: 1rem;
  }

  select {
    font-size: 1rem;
  }
}

@media screen and (max-width: 990px) {
  .filters {
    flex-direction: column;
    margin-left: 1rem;
    margin-right: 1rem;
    gap: 0.5rem;
  }

  .filter {
    display: flex;
    justify-content: center;
  }

  .filter-title {
    flex: 1;
    text-align: right;
  }

  .select-container {
    flex: 1;
  }

  select {
    width: 11.5rem;
  }
}

@media screen and (max-width: 640px) {
  .filter-title {
    font-size: 0.875rem;
  }

  select {

    font-size: 0.875rem;
  }

  .filter:nth-child(3) select{
    max-width: 11.5rem;
    width: 100%;
  }
}

@media screen and (max-width: 360px) {

}
</style>