<template>
  <div class="description-component">
    <div class="description-max">
      <div class="content">
        <div class="info">
          <h1 class="title">
            {{ description.name }}
          </h1>
          <div class="description" v-html="description.description">
          </div>

        </div>

        <div class="parameters">
          <div class="parameter">
            <div class="parameter-title">
              Форма
            </div>
            <div class="parameter-value">
              {{ translations[description.sofa_form] }}
            </div>
          </div>

          <div class="parameter">
            <div class="parameter-title">
              Тип
            </div>
            <div class="parameter-value">
              {{ translations[description.sofa_type] }}
            </div>
          </div>

          <div class="parameter">
            <div class="parameter-title">
              Механизм раскладывания
            </div>
            <div class="parameter-value" v-if="description.folding_mechanism">
              {{ translations[description.folding_mechanism] }} <span
                v-if="description.folding_size">(Расклад {{ description.folding_size }}мм)</span>
            </div>
            <div class="parameter-value" v-else>
              Отсутствует
            </div>
          </div>

          <div class="parameter">
            <div class="parameter-title">
              Общие размеры
            </div>
            <div class="parameter-value">
              {{ description.width }}*{{ description.depth }} мм
            </div>
          </div>

          <div class="parameter">
            <div class="parameter-title">
              Высота
            </div>
            <div class="parameter-value">
              {{ description.height }} мм
            </div>
          </div>

          <div class="parameter">
            <div class="parameter-title">
              Ширина
            </div>
            <div class="parameter-value">
              {{ description.width }} мм
            </div>
          </div>

          <div class="parameter">
            <div class="parameter-title">
              Глубина
            </div>
            <div class="parameter-value">
              {{ description.depth }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.seat_depth">
            <div class="parameter-title">
              Глубина посадочного места
            </div>
            <div class="parameter-value">
              {{ description.seat_depth }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.back_height">
            <div class="parameter-title">
              Высота спинки
            </div>
            <div class="parameter-value">
              {{ description.back_height }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.armrest_height">
            <div class="parameter-title">
              Высота подлокотников
            </div>
            <div class="parameter-value">
              {{ description.armrest_height }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.seat_height">
            <div class="parameter-title">
              Высота посадочного места
            </div>
            <div class="parameter-value">
              {{ description.seat_height }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.legs_height">
            <div class="parameter-title">
              Высота ножек
            </div>
            <div class="parameter-value">
              {{ description.legs_height }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.straight_module_depth">
            <div class="parameter-title">
              Глубина прямого модуля
            </div>
            <div class="parameter-value">
              {{ description.straight_module_depth }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.corner_module_depth">
            <div class="parameter-title">
              Глубина углового модуля
            </div>
            <div class="parameter-value">
              {{ description.corner_module_depth }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.module_depth">
            <div class="parameter-title">
              Глубина модуля
            </div>
            <div class="parameter-value">
              {{ description.module_depth }} мм
            </div>
          </div>

          <div class="parameter" v-if="description.pouf_depth">
            <div class="parameter-title">
              Глубина пуфа
            </div>
            <div class="parameter-value">
              {{ description.pouf_depth }} мм
            </div>
          </div>
        </div>

        <div class="contact">
          <div class="price-block">
            <div class="contact-text">
              <div class="contact-text-title">
                Узнайте стоимость за 10 минут
              </div>
              <div class="contact-text-description">
                Наш менеджер рассчитает стоимость выбранной модели по вашим размерам в течение 10 минут
              </div>
            </div>
            <div class="price">
              {{ formattedPrice(description.price) }}
            </div>
          </div>
          <div class="buttons-container">
            <a class="description-button" :href="this.contacts.tg_link" target="_blank">
            <span class="button-text">
              Связаться в Telegram
            </span>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path
                    d="M2.90752 10.9675C2.90752 10.9675 12.3427 6.78305 15.615 5.30961C16.8695 4.72029 21.1235 2.83428 21.1235 2.83428C21.1235 2.83428 23.0869 2.00923 22.9233 4.01302C22.8687 4.83815 22.4324 7.72597 21.9961 10.8496C21.3416 15.2698 20.6326 20.1025 20.6326 20.1025C20.6326 20.1025 20.5235 21.4581 19.5964 21.6939C18.6692 21.9296 17.1421 20.8688 16.8695 20.633C16.6512 20.4562 12.779 17.8041 11.361 16.5075C10.9792 16.1539 10.543 15.4467 11.4155 14.6215C13.379 12.6766 15.7241 10.2603 17.1421 8.72795C17.7966 8.02068 18.451 6.37048 15.7241 8.37427C11.8519 11.2622 8.03417 13.9732 8.03417 13.9732C8.03417 13.9732 7.16152 14.5626 5.52538 14.0321C3.88916 13.5018 1.9803 12.7945 1.9803 12.7945C1.9803 12.7945 0.671447 11.9105 2.90752 10.9675Z"
                    fill="white"/>
              </svg>
            </a>
            <a class="description-button" :href="this.contacts.whatsapp_link" target="_blank">
          <span class="button-text">
            Связаться в What’s App
          </span>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <g clip-path="url(#clip0_174_226)">
                  <path
                      d="M0 24L1.72042 17.6031C0.332943 15.1112 -0.10787 12.2033 0.478864 9.41309C1.0656 6.62288 2.64052 4.13748 4.91464 2.41298C7.18876 0.68848 10.0095 -0.159455 12.8593 0.0247736C15.7091 0.209002 18.3968 1.41304 20.4291 3.41594C22.4615 5.41883 23.7022 8.08625 23.9236 10.9287C24.145 13.7712 23.3322 16.598 21.6344 18.8904C19.9366 21.1829 17.4677 22.7873 14.6807 23.4091C11.8937 24.0309 8.97552 23.6285 6.46172 22.2757L0 24ZM6.77329 19.8819L7.17291 20.1186C8.99371 21.196 11.1204 21.6419 13.2215 21.3867C15.3226 21.1315 17.2802 20.1896 18.7891 18.7077C20.298 17.2258 21.2736 15.2873 21.5637 13.1941C21.8538 11.101 21.4422 8.97077 20.393 7.13553C19.3439 5.30028 17.7161 3.86306 15.7633 3.04784C13.8106 2.23262 11.6425 2.0852 9.5971 2.62854C7.55165 3.17188 5.74369 4.37546 4.45496 6.05173C3.16622 7.728 2.46911 9.78279 2.47225 11.8959C2.47054 13.648 2.9559 15.3662 3.87432 16.8593L4.12493 17.2717L3.16313 20.8421L6.77329 19.8819Z"
                      fill="white"/>
                  <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M16.4716 13.5385C16.2374 13.3498 15.963 13.2171 15.6696 13.1503C15.3762 13.0835 15.0713 13.0844 14.7783 13.153C14.338 13.3356 14.0536 14.0254 13.7691 14.3702C13.7091 14.4529 13.6209 14.5109 13.5212 14.5333C13.4214 14.5557 13.3169 14.541 13.2272 14.4919C11.6154 13.8617 10.2644 12.7059 9.39353 11.2123C9.31926 11.1191 9.28411 11.0008 9.29548 10.8822C9.30685 10.7637 9.36385 10.6541 9.45449 10.5767C9.77178 10.2631 10.0047 9.87472 10.1318 9.44743C10.16 8.97612 10.0519 8.50666 9.82025 8.09502C9.64118 7.51791 9.30038 7.00404 8.83812 6.61412C8.5997 6.50707 8.33535 6.47118 8.07695 6.51077C7.81855 6.55037 7.57715 6.66376 7.38187 6.83727C7.04284 7.12929 6.77375 7.49351 6.5944 7.9031C6.41505 8.3127 6.33001 8.75724 6.34555 9.204C6.3466 9.45488 6.37845 9.70468 6.44038 9.94782C6.59766 10.532 6.83953 11.0901 7.15835 11.6045C7.38837 11.9986 7.63934 12.38 7.91018 12.7473C8.7904 13.9537 9.89686 14.9779 11.1681 15.7632C11.8061 16.1623 12.4879 16.4867 13.2001 16.7302C13.94 17.065 14.7569 17.1935 15.564 17.1021C16.0239 17.0326 16.4596 16.8513 16.8328 16.5742C17.2061 16.2971 17.5053 15.9327 17.7044 15.513C17.8213 15.2595 17.8568 14.976 17.806 14.7016C17.684 14.1403 16.9322 13.809 16.4716 13.5385Z"
                        fill="white"/>
                </g>
                <defs>
                  <clipPath id="clip0_174_226">
                    <rect width="24" height="24" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </a>

          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "Description",
  inject: ['backendURL'],
  props: [
    'description',
    'contacts'
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
    formattedPrice(price) {
      let integerPart = parseInt(price).toString();
      integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
      return `от ${integerPart} ₽`;
    }
  }
}
</script>

<style scoped>
.description-component {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 6.25rem;
  margin-right: 1rem;
  margin-left: 1rem;
}

.description-max {
  max-width: 74rem;
  width: 100%;
}

.content {
  display: grid;
  grid-template-columns: 2fr 1fr;
}

.info {
  grid-area: 1 / 1 / 1 / 1;
}

.title {
  color: #212121;
  font-size: 2.625rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  letter-spacing: -0.0525rem;
}

.description {
  margin-top: 2rem;
  color: #212121;
  font-size: 1.125rem;
  width: 85%;
}

.parameters {
  grid-area: 2 / 1 / 2 / 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 60%;
}

.parameter {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.parameter-title {
  color: #A9A9A9;
  font-size: 1.125rem;
}

.parameter-value {
  color: #212121;
  font-size: 1.125rem;
}

.contact {
  grid-area: 1 / 2 / 1 / 2;
  height: 23rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.price-block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 2rem;
  background-color: #fff;
  height: 18rem;
}

.contact-text-title {
  color: #212121;
  font-size: 1.5rem;
  width: 85%;
}

.contact-text-description {
  color: #484848;
  font-size: 1rem;
  margin-top: 1rem;
}

.price {
  color: #212121;
  margin-top: 3.5rem;
}

.buttons-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.description-button {
  display: flex;
  height: 3rem;
  padding: 1rem 2rem;
  justify-content: space-between;
  align-items: center;
  background: #212121;
  text-decoration: none;

  position: relative;
  transition: background-color 0.5s ease;
}

.description-button:hover {
  background: #21212100;
}


.description-button:before {
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

.description-button:hover:before {
  clip-path: inset(-10% 0 0 -10%);
}

.description-button span {
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

svg {
  flex-shrink: 0;
  position: relative;
  overflow: visible;
}

.description-button:hover span {
  background-position: 0 100%;
}

.description-button path {
  transition: fill 0.4s ease;
}

.description-button:hover path {
  fill: #212121;
}

@media screen and (max-width: 1200px) {
  .content {
    grid-template-columns: 5fr 3fr;
  }

  .title {
    font-size: 2.125rem;
  }

  .description {
    font-size: 1rem;
    width: 90%;

  }

  .parameters {
    width: 85%;
  }
}

@media screen and (max-width: 990px) {
  .content {
    grid-template-columns: none;
    gap: 4rem;
  }

  .title {
    font-size: 1.625rem;
  }

  .description {
    width: 100%;
    margin-top: 1rem;
  }

  .contact {
    grid-area: 2 / 1 / 2 / 1;
    height: auto;
  }

  .contact-text {
    width: 60%;
  }

  .contact-text-title {
    font-size: 1.125rem;
    width: 100%;
  }

  .price {
    margin-top: 0;
    font-size: 1.125rem;
  }

  .price-block {
    flex-direction: row;
    height: auto;
  }

  .buttons-container {
    flex-direction: row;
  }

  .description-button {
    flex: 1;
    padding: 1rem 1.5rem;
  }

  .description-button span {
    font-size: 1rem;
  }

  .parameters {
    grid-area: 3 / 1 / 3 / 1;
    width: 100%;
    gap: 0;
  }

  .parameter {
    height: 3rem;
    align-items: center;
    border-bottom: #E6E6E6 1px solid;
  }
}

@media screen and (max-width: 640px) {
  .title {
    font-size: 1.375rem;
  }

  .description {
    font-size: 0.875rem;
  }

  .contact {
    gap: 0.5rem;
  }

  .price-block {
    padding: 2rem 1rem;
  }

  .contact-text-title {
    font-size: 1rem;
  }

  .contact-text-description {
    font-size: 0.875rem;
  }

  .price {
    font-size: 1rem;
  }

  .buttons-container {
    flex-direction: column;
    gap: 0.5rem;
  }

  .parameter-title, .parameter-value {
    font-size: 0.875rem;
    line-height: 1.1375rem;
  }

  .parameter-value {
    width: 37%;
    text-align: right;
  }
}

@media screen and (max-width: 360px) {

}
</style>