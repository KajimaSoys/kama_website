<template>
  <div class="delivery-component">
    <div class="delivery-max">
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
  padding-top: 12.5rem;
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
    padding-top: 9.5rem;
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
    padding-top: 7.5rem;
  }

  .content {
    flex-direction: column;
    gap: 0;
  }

  .delivery {
    align-items: center;
  }

  h2 {
    margin-bottom: 1rem;
  }

  .description {
    max-width: 65%;
    text-align: center;
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
    margin-top: 1.5rem;
    margin-bottom: 0;
  }

}

@media screen and (max-width: 640px) {
  .delivery-component {
    padding-top: 6.25rem;
  }

  h2 {
    margin-bottom: 0;
    text-align: center;
  }

  .description {
    font-size: 0.875rem;
    line-height: 1.3125rem;
  }

  .map-caption {
    width: 50vw;
    min-width: 14rem;

  }
}

@media screen and (max-width: 360px) {

}
</style>