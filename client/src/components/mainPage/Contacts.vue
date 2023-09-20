<template>
  <div class="contacts-component">
    <div class="contacts-max">
      <div class="content">
        <div class="info">
          <h2 class="title">
            Контакты
          </h2>

          <div class="number">
            <a :href="`tel:${ this.contacts.number }`"> {{ this.contacts.number }}</a>
          </div>

          <div class="mail">
            <a :href="`mailto:${this.contacts.mail}`">{{ this.contacts.mail }}</a>

          </div>

          <div class="links">
            <a class="whatsapp-link" :href="this.contacts.whatsapp_link" target="_blank">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <g clip-path="url(#clip0_114_523)">
                  <path
                      d="M0 24L1.72042 17.6031C0.332943 15.1112 -0.10787 12.2033 0.478864 9.41309C1.0656 6.62288 2.64052 4.13748 4.91464 2.41298C7.18876 0.68848 10.0095 -0.159455 12.8593 0.0247736C15.7091 0.209002 18.3968 1.41304 20.4291 3.41594C22.4615 5.41883 23.7022 8.08625 23.9236 10.9287C24.145 13.7712 23.3322 16.598 21.6344 18.8904C19.9366 21.1829 17.4677 22.7873 14.6807 23.4091C11.8937 24.0309 8.97552 23.6285 6.46172 22.2757L0 24ZM6.77329 19.8819L7.17291 20.1186C8.99371 21.196 11.1204 21.6419 13.2215 21.3867C15.3226 21.1315 17.2802 20.1896 18.7891 18.7077C20.298 17.2258 21.2736 15.2873 21.5637 13.1941C21.8538 11.101 21.4422 8.97077 20.393 7.13553C19.3439 5.30028 17.7161 3.86306 15.7633 3.04784C13.8106 2.23262 11.6425 2.0852 9.5971 2.62854C7.55165 3.17188 5.74369 4.37546 4.45496 6.05173C3.16622 7.728 2.46911 9.78279 2.47225 11.8959C2.47054 13.648 2.9559 15.3662 3.87432 16.8593L4.12493 17.2717L3.16313 20.8421L6.77329 19.8819Z"
                      fill="#6E6E6E"/>
                  <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M16.4726 13.5385C16.2383 13.3498 15.964 13.2171 15.6706 13.1503C15.3771 13.0835 15.0723 13.0844 14.7793 13.153C14.339 13.3356 14.0545 14.0254 13.7701 14.3702C13.7101 14.4529 13.6219 14.5109 13.5222 14.5333C13.4224 14.5557 13.3179 14.541 13.2282 14.4919C11.6164 13.8617 10.2653 12.7059 9.39451 11.2123C9.32024 11.1191 9.28508 11.0008 9.29645 10.8822C9.30782 10.7637 9.36483 10.6541 9.45547 10.5767C9.77276 10.2631 10.0057 9.87472 10.1328 9.44743C10.161 8.97612 10.0529 8.50666 9.82123 8.09502C9.64216 7.51791 9.30136 7.00404 8.8391 6.61412C8.60068 6.50707 8.33633 6.47118 8.07793 6.51077C7.81953 6.55037 7.57813 6.66376 7.38284 6.83727C7.04382 7.12929 6.77472 7.49351 6.59537 7.9031C6.41603 8.3127 6.33099 8.75724 6.34653 9.204C6.34758 9.45488 6.37942 9.70468 6.44136 9.94782C6.59864 10.532 6.84051 11.0901 7.15933 11.6045C7.38934 11.9986 7.64031 12.38 7.91116 12.7473C8.79138 13.9537 9.89784 14.9779 11.1691 15.7632C11.8071 16.1623 12.4889 16.4867 13.2011 16.7302C13.941 17.065 14.7578 17.1935 15.565 17.1021C16.0249 17.0326 16.4606 16.8513 16.8338 16.5742C17.207 16.2971 17.5063 15.9327 17.7053 15.513C17.8223 15.2595 17.8578 14.976 17.8069 14.7016C17.685 14.1403 16.9332 13.809 16.4726 13.5385Z"
                        fill="#6E6E6E"/>
                </g>
                <defs>
                  <clipPath id="clip0_114_523">
                    <rect width="24" height="24" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </a>

            <a :href="this.contacts.tg_link" class="tg-link" target="_blank">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path
                    d="M2.90752 10.9675C2.90752 10.9675 12.3427 6.78305 15.615 5.30961C16.8695 4.72029 21.1235 2.83428 21.1235 2.83428C21.1235 2.83428 23.0869 2.00923 22.9233 4.01302C22.8687 4.83815 22.4324 7.72597 21.9961 10.8496C21.3416 15.2698 20.6326 20.1025 20.6326 20.1025C20.6326 20.1025 20.5235 21.4581 19.5964 21.6939C18.6692 21.9296 17.1421 20.8688 16.8695 20.633C16.6512 20.4562 12.779 17.8041 11.361 16.5075C10.9792 16.1539 10.543 15.4467 11.4155 14.6215C13.379 12.6766 15.7241 10.2603 17.1421 8.72795C17.7966 8.02068 18.451 6.37048 15.7241 8.37427C11.8519 11.2622 8.03417 13.9732 8.03417 13.9732C8.03417 13.9732 7.16152 14.5626 5.52538 14.0321C3.88916 13.5018 1.9803 12.7945 1.9803 12.7945C1.9803 12.7945 0.671447 11.9105 2.90752 10.9675Z"
                    fill="#6E6E6E"/>
              </svg>
            </a>
          </div>
        </div>

        <div class="image-first">
          <img :src="`${this.backendURL}${this.contacts.image_first}`" alt="" class="image"/>
        </div>

        <div class="image-second">
          <img :src="`${this.backendURL}${this.contacts.image_second}`" alt="" class="image"/>
        </div>
      </div>
    </div>


    <div class="union">
      <svg xmlns="http://www.w3.org/2000/svg" width="1716" height="656" viewBox="0 0 1716 656" fill="none">
        <path
            d="M1147.71 186.541C1197.49 54.9356 1331.2 -19.4501 1473.83 4.86829C1615.71 29.1867 1715.26 142.911 1716 281.669V656H1496.86V282.384C1496.86 228.741 1454.51 215.866 1435.94 213.005C1418.11 209.429 1373.54 207.998 1354.23 258.066L1206.37 656H973.279L1147.71 186.541Z"
            fill="white"/>
        <path
            d="M475.371 80.5768C617.257 104.18 716.8 218.62 716.8 357.378V656H498.4V357.378C498.4 304.449 456.057 290.859 437.486 287.998C419.657 285.137 375.086 283.707 355.772 333.774L200.598 656H-33.0283L150 260.819C199.029 130.644 332.743 56.2584 475.371 80.5768Z"
            fill="white"/>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: "Contacts",
  inject: ['backendURL'],
  props: [
    'contacts'
  ],
  emits: [],
  methods: {}
}
</script>

<style scoped>
.contacts-component {
  padding-top: 6.25rem;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 6.25rem 1rem 12.5rem;
}

.contacts-max {
  max-width: 74rem;
  width: 100%;
}

.content {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 24.6875rem;
}

.number {
  margin-top: 2rem;
}

.mail {
  margin-top: 1rem;
}

.number a, .mail a {
  text-decoration: none;
  color: #000;
  transition: opacity 0.2s ease-in-out;
}

.number:hover a, .mail:hover a {
  opacity: 0.5
}

.links {
  margin-top: 4rem;
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.whatsapp-link, .tg-link {
  transition: opacity 0.2s ease-in-out;
}

.whatsapp-link:hover, .tg-link:hover {
  opacity: 0.5
}

.image-first {
  display: flex;
  align-items: flex-end;
}

.union {
  position: absolute;
  z-index: -1;
  bottom: -32rem;
}

@media screen and (max-width: 1200px) {
  .contacts-component {
    margin-top: 4.75rem;
    padding-top: 4.75rem;
  }

  .number, .mail {
    font-size: 1.125rem;
  }

  .content {
    height: 27.6875rem;
  }
}

@media screen and (max-width: 990px) {
  .contacts-component {
    margin-top: 3.75rem;
    padding-top: 3.75rem;
  }

  .number, .mail {
    font-size: 1rem;
  }

  .content {
    height: 28rem;
  }

  .image-first {
    position: absolute;
    bottom: 0;
    width: 8.75rem;
  }

  .image-first img {
    width: 100%;
  }

  .image-second {
    width: 24.5rem;
  }

  .image-second img {
    width: 100%;
  }

  .links {
    margin-top: 2rem;
  }
}

@media screen and (max-width: 640px) {
  .contacts-component {
    margin-top: 3.125rem;
    padding-top: 3.125rem;
  }

  .content {
    flex-direction: column;
    align-items: center;
  }

  .title, .number, .mail {
    text-align: center;
  }


  .links {
    gap: 2rem;
    justify-content: center;
  }

  .info {
    order: 1;
  }

  .image-first {
    position: relative;
    width: 100%;
    justify-content: flex-end;
    margin-top: 1.2rem;
    order: 3;
  }

  .image-first img {
    width: 40%;
  }

  .image-second {
    order: 2;
    margin-top: 4rem;
    width: 100%;
    position: relative;
    left: 0;
  }

  .image-second img {
    width: 70%;
  }
}

@media screen and (max-width: 360px) {

}
</style>