<template>
  <div class="own-configuration-component">
    <div class="own-configuration-max">
      <h2 class="title">
        Создайте свою конфигурацию
      </h2>
      <div class="description">
        Выберите размеры, конструкцию, цвет, ткань и фурнитуру под себя. Для этого свяжитесь с менеджером
      </div>
      <div class="buttons">
        <a class="button" :href="this.contacts.tg_link" target="_blank">
        <span class="button-text">
          Связаться в Telegram
        </span>
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path
                d="M2.90752 10.9675C2.90752 10.9675 12.3427 6.78305 15.615 5.30961C16.8695 4.72029 21.1235 2.83428 21.1235 2.83428C21.1235 2.83428 23.0869 2.00923 22.9233 4.01302C22.8687 4.83815 22.4324 7.72597 21.9961 10.8496C21.3416 15.2698 20.6326 20.1025 20.6326 20.1025C20.6326 20.1025 20.5235 21.4581 19.5964 21.6939C18.6692 21.9296 17.1421 20.8688 16.8695 20.633C16.6512 20.4562 12.779 17.8041 11.361 16.5075C10.9792 16.1539 10.543 15.4467 11.4155 14.6215C13.379 12.6766 15.7241 10.2603 17.1421 8.72795C17.7966 8.02068 18.451 6.37048 15.7241 8.37427C11.8519 11.2622 8.03417 13.9732 8.03417 13.9732C8.03417 13.9732 7.16152 14.5626 5.52538 14.0321C3.88916 13.5018 1.9803 12.7945 1.9803 12.7945C1.9803 12.7945 0.671447 11.9105 2.90752 10.9675Z"
                fill="#2A2B2D"/>
          </svg>
        </a>
        <a class="button" :href="this.contacts.whatsapp_link" target="_blank">
        <span class="button-text">
          Связаться в What’s App
        </span>
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <g clip-path="url(#clip0_174_226)">
              <path
                  d="M0 24L1.72042 17.6031C0.332943 15.1112 -0.10787 12.2033 0.478864 9.41309C1.0656 6.62288 2.64052 4.13748 4.91464 2.41298C7.18876 0.68848 10.0095 -0.159455 12.8593 0.0247736C15.7091 0.209002 18.3968 1.41304 20.4291 3.41594C22.4615 5.41883 23.7022 8.08625 23.9236 10.9287C24.145 13.7712 23.3322 16.598 21.6344 18.8904C19.9366 21.1829 17.4677 22.7873 14.6807 23.4091C11.8937 24.0309 8.97552 23.6285 6.46172 22.2757L0 24ZM6.77329 19.8819L7.17291 20.1186C8.99371 21.196 11.1204 21.6419 13.2215 21.3867C15.3226 21.1315 17.2802 20.1896 18.7891 18.7077C20.298 17.2258 21.2736 15.2873 21.5637 13.1941C21.8538 11.101 21.4422 8.97077 20.393 7.13553C19.3439 5.30028 17.7161 3.86306 15.7633 3.04784C13.8106 2.23262 11.6425 2.0852 9.5971 2.62854C7.55165 3.17188 5.74369 4.37546 4.45496 6.05173C3.16622 7.728 2.46911 9.78279 2.47225 11.8959C2.47054 13.648 2.9559 15.3662 3.87432 16.8593L4.12493 17.2717L3.16313 20.8421L6.77329 19.8819Z"
                  fill="#2A2B2D"/>
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M16.4716 13.5385C16.2374 13.3498 15.963 13.2171 15.6696 13.1503C15.3762 13.0835 15.0713 13.0844 14.7783 13.153C14.338 13.3356 14.0536 14.0254 13.7691 14.3702C13.7091 14.4529 13.6209 14.5109 13.5212 14.5333C13.4214 14.5557 13.3169 14.541 13.2272 14.4919C11.6154 13.8617 10.2644 12.7059 9.39353 11.2123C9.31926 11.1191 9.28411 11.0008 9.29548 10.8822C9.30685 10.7637 9.36385 10.6541 9.45449 10.5767C9.77178 10.2631 10.0047 9.87472 10.1318 9.44743C10.16 8.97612 10.0519 8.50666 9.82025 8.09502C9.64118 7.51791 9.30038 7.00404 8.83812 6.61412C8.5997 6.50707 8.33535 6.47118 8.07695 6.51077C7.81855 6.55037 7.57715 6.66376 7.38187 6.83727C7.04284 7.12929 6.77375 7.49351 6.5944 7.9031C6.41505 8.3127 6.33001 8.75724 6.34555 9.204C6.3466 9.45488 6.37845 9.70468 6.44038 9.94782C6.59766 10.532 6.83953 11.0901 7.15835 11.6045C7.38837 11.9986 7.63934 12.38 7.91018 12.7473C8.7904 13.9537 9.89686 14.9779 11.1681 15.7632C11.8061 16.1623 12.4879 16.4867 13.2001 16.7302C13.94 17.065 14.7569 17.1935 15.564 17.1021C16.0239 17.0326 16.4596 16.8513 16.8328 16.5742C17.2061 16.2971 17.5053 15.9327 17.7044 15.513C17.8213 15.2595 17.8568 14.976 17.806 14.7016C17.684 14.1403 16.9322 13.809 16.4716 13.5385Z"
                    fill="#2A2B2D"/>
            </g>
            <defs>
              <clipPath id="clip0_174_226">
                <rect width="24" height="24" fill="#2A2B2D"/>
              </clipPath>
            </defs>
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "OwnConfiguration",
  inject: ['backendURL'],
  props: [
    'contacts'
  ],
  emits: [],
  methods: {}
}
</script>

<style scoped>
.own-configuration-component {
  margin-top: 10rem;
  height: 29.75rem;
  background: #2A2B2D;
  display: flex;
  justify-content: center;
}

.own-configuration-max {
  max-width: 74rem;
  width: 100%;
  padding: 0 1rem 0 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title {
  color: #fff;
  text-align: center;
  padding-top: 6.25rem;
}

.description {
  margin-top: 1rem;
  color: #fff;
  text-align: center;
  font-size: 1.125rem;
  width: 50%;
}

.buttons {
  margin-top: 4rem;
  display: flex;
  flex-direction: row;
  gap: 1rem;
  justify-content: center;
}

.button {
  background: #FFF;
  padding: 0.2rem 2rem;
  display: flex;
  width: 20.1875rem;
  height: 4.375rem;
  justify-content: space-between;
  align-items: center;
  position: relative;
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.5s ease;
}

.button:hover {
  background: #ffffff00;
}

.button:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100%;
  background: #212121;
  z-index: 0;
  clip-path: inset(-1% 100% -1% 0);
  transition: clip-path 0.5s ease;
}

.button:hover:before {
  clip-path: inset(-10% 0 0 -10%);
}

.button span {
  color: #212121;
  text-align: left;
  font-size: 1.125rem;
  position: relative;
  font-weight: 500;
  transition: color .2s ease-in-out;
}

svg {
  z-index: 1;
}

svg path {
  transition: all .2s ease-in-out;
}

.button:hover {
  background: #212121;
}

.button:hover span {
  color: #fff;
}

.button:hover svg path {
  fill: #fff;
}


@media screen and (max-width: 1200px) {
  .own-configuration-component {
    height: 28.1875rem;
    margin-top: 9.5rem;

  }

  .description {
    font-size: 1rem;
  }

  .button {
    padding: 1rem 2rem;
    height: auto;
    width: 19.5rem;
  }
}

@media screen and (max-width: 990px) {
  .own-configuration-component {
    height: 20.75rem;
    margin-top: 7.5rem;
  }

  .title {
    padding-top: 4rem;
  }

  .description {
    width: 85%;
  }

  .buttons {
    margin-top: 2.5rem;
    width: 100%;
    max-width: 40rem;
  }

  .button {
    padding: 1rem 1.5rem;
    width: auto;
    flex: 1;
  }

  .button span {
    font-size: 1rem;
  }
}

@media screen and (max-width: 640px) {
  .own-configuration-component {
    height: auto;
    margin-top: 6.25rem;
  }

  .description {
    font-size: 0.875rem;
  }

  .buttons {
    flex-direction: column;
    gap: 0.5rem;
    margin-bottom: 4rem;
  }

  .button {
    max-width: 16rem;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
  }
}

@media screen and (max-width: 360px) {

}
</style>