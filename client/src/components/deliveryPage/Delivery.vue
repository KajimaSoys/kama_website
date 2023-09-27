<template>
  <div class="delivery-component">
    <div class="delivery-max">
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
  </div>
</template>

<script>
export default {
  name: "Delivery",
  inject: ['backendURL'],
  props: [
    'delivery'
  ],
  emits: [],
  methods: {}
}
</script>

<style scoped>
.delivery-component {
  margin-top: 6.25rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.delivery-max {
  max-width: 74rem;
  width: 100%;
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
  margin-top: 9rem;
}

.delivery {
  flex: 2;
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
  flex: 3;
  position: relative;
  width: 100%;
}

.map {
  position: absolute;
  bottom: 2rem;
  width: 100%;
}

.map-caption {
  position: absolute;
  bottom: 10rem;
  left: 7rem;
}

@media screen and (max-width: 1200px) {
  .delivery-component {
    margin-top: 4rem;
  }

  h1.title {
    font-size: 3.6875rem;
  }

  h2 {
    font-size: 2.125rem;
  }

  .content {
    margin-top: 7rem;
  }

  .description {
    font-size: 1rem;
  }

  .delivery {
    gap: 1rem;
  }

  .van {
    margin-top: 3rem;
    margin-bottom: 1rem;
  }
}

@media screen and (max-width: 990px) {
  .delivery-component {

  }

  h1.title {
    font-size: 2.5rem;
  }

  h2 {
    font-size: 1.625rem;
    text-align: center;
    width: 80%;
  }

  .content {
    margin-top: 4rem;
    flex-direction: column;
    gap: 0;
  }

  .delivery {
    align-items: center;
  }


  .description {
    max-width: 65%;
    text-align: center;
  }

  .images {
    max-width: 45rem;
    margin-left: auto;
    margin-right: auto;
  }

  .map {
    position: relative;
    bottom: 0;
    width: 100%;
  }

  .map-caption {
    bottom: 18vw;
    left: 20vw;
  }

  .van {
    margin-top: 1rem;
    margin-bottom: 0;
  }

  .van img {
    width: 8.75rem;
  }

}

@media screen and (max-width: 640px) {
  .delivery-component {
    margin-top: 2rem;
  }

  h1.title {
    font-size: 2.125rem;
  }

  h2 {
    font-size: 1.375rem;
    margin-bottom: 0;
  }

  .content {
    margin-top: 2rem;
  }

  .description {
    font-size: 0.875rem;
    line-height: 1.3125rem;
    max-width: 80%;
  }

  .map-caption {
    width: 50vw;
    min-width: 14rem;

  }
}

@media screen and (max-width: 360px) {

}
</style>