<template>
  <div class="payment-component">
    <div class="content">
      <div class="image-container">
        <img :src="`${this.backendURL}${this.payment.image}`" alt="" class="image"/>
      </div>
      <div class="stages">
        <h2 class="title">
          {{ this.payment.title_main }}
        </h2>

        <div class="stage">
          <div class="number">
            {{ this.payment.payment_first }}
          </div>
          <div class="stage-text">
            <h3>
              {{ this.payment.title_first }}
            </h3>
            <div class="description">
              {{ this.payment.description_first }}
            </div>
          </div>
        </div>


        <div class="stage">
          <div class="number">
            {{ this.payment.payment_second }}
          </div>
          <div class="stage-text">
            <h3>
              {{ this.payment.title_second }}
            </h3>
            <div class="description">
              {{ this.payment.description_second }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Payment",
  inject: ['backendURL'],
  props: [
      'payment'
  ],
  emits: [
  ],
  methods: {

  }
}
</script>

<style scoped>
.payment-component {
  margin-top: 10.25rem;
  margin-left: 23rem;
  margin-right: 23rem;
}

.content {
  display: flex;
  flex-direction: row;
}

.image-container {
  flex: 1;
}

.image-first img {
  width: 470px;
}

.stages {
  display: flex;
  flex-direction: column;
  gap: 4rem;
  flex: 1;
}

.title {
  color: #000;
  font-size: 2.625rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  letter-spacing: -0.0525rem;
  margin-top: 3rem;
}

.stage {
  display: inline-flex;
  align-items: flex-start;
  gap: 3.75rem;
}

.number {
  display: flex;
  min-width: 2.5rem;
  height: 2.5rem;
  padding: 0.25rem;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0.625rem;
  background: #313131;
  color: #FFF;
}

.stage-text {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

h3 {
  color: #212121;
}

.description {
  color: #484848;
  font-size: 1.125rem;
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