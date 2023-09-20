<template>
  <div class="stages-component">
    <div class="stages-max">
      <h2 class="title">Как создаётся ваша мебель</h2>
      <div class="content">
        <div class="section">
          <div class="stages-first">
            <div class="stage">
              <div class="number">1</div>
              <div class="stage-text">
                <h3>
                  {{ this.stages.title_first }}
                </h3>

                <div class="description">
                  {{ this.stages.description_first }}
                </div>
              </div>
            </div>

            <div class="stage">
              <div class="number">2</div>
              <div class="stage-text">
                <h3>
                  {{ this.stages.title_second }}
                </h3>
                <div class="description">
                  {{ this.stages.description_second }}
                </div>
              </div>
            </div>

            <div class="stage">
              <div class="number">
                3
              </div>
              <div class="stage-text">
                <h3>
                  {{ this.stages.title_third }}
                </h3>
                <div class="description">
                  {{ this.stages.description_third }}
                </div>
              </div>
            </div>


          </div>
          <div class="image-first">
            <img :src="`${this.backendURL}${this.stages.image_first}`" alt="" class="image"/>
          </div>
        </div>

        <div class="section">
          <div class="image-second">
            <img :src="`${this.backendURL}${this.stages.image_second}`" alt="" class="image"/>
          </div>
          <div class="stages-second">
            <div class="stage">
              <div class="number">
                4
              </div>
              <div class="stage-text">
                <h3>
                  {{ this.stages.title_fourth }}
                </h3>
                <div class="description">
                  {{ this.stages.description_fourth }}
                </div>
              </div>
            </div>


            <div class="stage">
              <div class="number">
                5
              </div>
              <div class="stage-text">
                <h3>
                  {{ this.stages.title_fifth }}
                </h3>
                <div class="description">
                  {{ this.stages.description_fifth }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="union">
      <svg xmlns="http://www.w3.org/2000/svg" width="558" height="613" viewBox="0 170 558 613" fill="none">
        <path fill-rule="evenodd" clip-rule="evenodd"
              d="M279 613C433.087 613 558 488.087 558 334L558 -6.65408e-06L329 -3.92329e-06L329 334C329 361.614 306.614 384 279 384C251.386 384 229 361.614 229 334L229 -2.7308e-06L3.32704e-06 0L3.98291e-06 334C5.82038e-06 488.087 124.913 613 279 613Z"
              fill="white"/>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: "Stages",
  inject: ['backendURL'],
  props: [
    'stages'
  ],
  emits: [],
  methods: {}
}
</script>

<style scoped>
.stages-component {
  padding-top: 12.5rem;
  background-color: #F8F8F8;
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 1rem;
  margin-right: 1rem;
}

.stages-max {
  max-width: 74rem;
  width: 100%;
}

.title {
  color: #212121;
  text-align: center;
}

.content {
  margin-top: 6.25rem;
  display: flex;
  flex-direction: column;
  gap: 8.5rem;
}

.section {
  display: flex;
  flex-direction: row;
}

h3 {
  color: #212121;
}

.stages-first, .stages-second {
  display: flex;
  flex-direction: column;
  gap: 5rem;
  flex: 1;
}

.image-first {
  display: flex;
  justify-content: flex-end;
  flex: 1;
}

.image-second {
  flex: 1;
}

.image-first img {
  width: 470px;
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

.description {
  max-width: 80%;
}

.union {
  position: absolute;
  top: 0;
  left: 9rem;
  z-index: -1;
}

@media screen and (max-width: 1200px) {
  .stages-component {
    padding-top: 9.5rem;
  }

  .content {
    margin-top: 4rem;
  }

  .image-second .image {
    width: 90%;
  }

  .stage {
    gap: 2.6rem;
  }

  .description {
    font-size: 1rem;
  }
}

@media screen and (max-width: 990px) {
  .stages-component {
    padding-top: 7.5rem;
  }

  .content {
    gap: 0;
  }

  .section {
    flex-direction: column;
  }


  .stage {
    gap: 2.3rem;
  }

  .stage-text {
    width: 100%;
  }

  .stages-first {
    margin-bottom: 4rem;
  }

  .stages-second {
    margin-top: 4rem;
  }

  .image-first {
    width: 100%;
    justify-content: flex-start;
  }

  .image-first img {
    width: 49%;
  }

  .image-second {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    margin-top: -8rem;
  }

  .image-second .image {
    width: 49%;
  }

}

@media screen and (max-width: 640px) {
  .stages-component {
    padding-top: 6.25rem;
  }

  .content {
    margin-top: 2rem;
    gap: 4rem;
  }

  .stages-first {
    order: 2;
    margin-bottom: 0;
    margin-top: 4rem;
  }

  .image-first {
    order: 1;
  }

  .image-first img {
    width: 100%;
  }

  .stage {
    gap: 1.5rem;
  }

  .description {
    font-size: 0.875rem;
    max-width: 100%;
    line-height: 1.3125rem;
  }

  .stage-text {
    gap: 0.5rem;
  }

  .number {
    min-width: 2rem;
    height: 2rem;
  }

  .image-second {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    margin-top: 0;
  }

  .image-second .image {
    width: 100%;
  }
}

@media screen and (max-width: 360px) {

}
</style>