<template>
  <div class="delivery-component">
    <h1 class="title">
      Доставляем по всей России
    </h1>
    <div class="content">
      <div class="delivery">
        <h2>
          {{ this.delivery.description_first }}
        </h2>

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
  margin-top: 6.25rem;
  margin-left: 23rem;
  margin-right: 23rem;
}

h1.title {
  color: #212121;
  text-align: center;
  font-size: 4.5rem;
  font-style: normal;
  font-weight: 400;
  line-height: 120%; /* 5.4rem */
  letter-spacing: -0.09rem;
}

.content {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  margin-top: 7rem;
}

.delivery {
  flex: 3;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

h2 {
  color: #000;
  font-size: 2.625rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  letter-spacing: -0.0525rem;
}

.description {
  max-width: 80%;
  color: #000;
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
}

.images {
  flex: 4;
  position: relative;
}

.map {
  position: absolute;
  bottom: 0;
}

.map-caption{
  position: absolute;
  bottom: 8rem;
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