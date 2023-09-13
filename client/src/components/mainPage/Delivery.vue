<template>
  <div class="delivery-component">
    <div class="content">
      <div class="delivery">
        <h2>
          {{ this.delivery.title }}
        </h2>

        <div class="description">
          {{ this.delivery.description_first }}
        </div>

        <div class="van">
          <img src="images/vinyl-van.png" alt=""/>
        </div>

        <div class="description">
          {{ this.delivery.description_second }}
        </div>

      </div>
      <div class="images">
        <img src="images/map.png" class="map" alt=""/>
        <img src="images/map-caption.png" class="map-caption" alt=""/>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "Delivery",
  inject: ['backendURL'],
  props: [
      'delivery'
  ],
  emits: [
  ],
  methods: {

  }
}
</script>

<style scoped>
.delivery-component {
  padding-top: 12.5rem;
  margin-left: 23rem;
  margin-right: 23rem;
}

.content {
  display: flex;
  flex-direction: row;
  gap: 2rem;
}

.delivery {
  flex: 2;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.description {
  max-width: 80%;
}

.images {
  flex: 3;
  position: relative;
}

.map {
  position: absolute;
  bottom: 2rem;
}

.map-caption{
  position: absolute;
  bottom: 10rem;
  left: 7rem;
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