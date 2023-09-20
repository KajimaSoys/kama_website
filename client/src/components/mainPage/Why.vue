<template>
  <div class="why-component">
    <div class="why-max">
      <div class="block-title">
        <h2>Почему мы?</h2>
      </div>
      <div class="content">

        <div class="flex-row">
          <div class="block-left">
            <div class="component">

              <h3>
                {{ this.why.title_first }}
              </h3>
              <div class="description">
                {{ this.why.description_first }}
              </div>
              <div class="icon-block">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                     fill="none">
                  <path
                      d="M14.7514 5.00307C14.0341 5.02058 13.3246 4.7479 12.8852 4.18073L11.9005 2.90963C11.288 2.11899 10.1856 1.90236 9.31945 2.40243L6.93057 3.78165C6.06443 4.28172 5.70084 5.34474 6.07929 6.27051L6.68709 7.75729C6.9591 8.42266 6.83924 9.17477 6.46406 9.78791C6.37816 9.92829 6.29562 10.0709 6.21657 10.2158C5.87247 10.8462 5.28141 11.3253 4.56982 11.4223L2.97977 11.6392C1.9888 11.7743 1.25 12.6207 1.25 13.6208V16.3793C1.25 17.3794 1.9888 18.2258 2.97977 18.3609L4.56982 18.5778C5.28142 18.6748 5.87248 19.1539 6.21657 19.7843C6.29562 19.9291 6.37814 20.0718 6.46403 20.2121C6.83921 20.8253 6.95906 21.5774 6.68706 22.2427L6.07927 23.7295C5.70081 24.6553 6.0644 25.7183 6.93055 26.2184L9.31943 27.5976C10.1856 28.0976 11.288 27.881 11.9005 27.0904L12.8851 25.8194C13.3245 25.2522 14.0341 24.9795 14.7513 24.997C14.834 24.999 14.9169 25 15 25C15.0832 25 15.1661 24.999 15.2488 24.997C15.9661 24.9795 16.6756 25.2522 17.115 25.8194L18.0995 27.0901C18.712 27.8808 19.8144 28.0974 20.6806 27.5973L23.0694 26.2181C23.9356 25.7181 24.2992 24.655 23.9207 23.7293L23.313 22.2426C23.041 21.5773 23.1608 20.8252 23.536 20.2121C23.6219 20.0717 23.7044 19.9291 23.7834 19.7843C24.1275 19.1539 24.7186 18.6748 25.4302 18.5778L27.0202 18.3609C28.0112 18.2258 28.75 17.3794 28.75 16.3793V13.6208C28.75 12.6207 28.0112 11.7743 27.0202 11.6392L25.4302 11.4223C24.7186 11.3253 24.1275 10.8462 23.7834 10.2158C23.7044 10.071 23.6219 9.92833 23.536 9.78798C23.1608 9.17485 23.041 8.42275 23.313 7.75738L23.9207 6.27073C24.2992 5.34496 23.9356 4.28194 23.0694 3.78187L20.6805 2.40265C19.8144 1.90258 18.712 2.11921 18.0995 2.90985L17.1149 4.18073C16.6755 4.74791 15.966 5.02059 15.2488 5.00308C15.1661 5.00106 15.0832 5.00004 15 5.00004C14.9169 5.00004 14.834 5.00106 14.7514 5.00307Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path
                      d="M18.75 15C18.75 17.0711 17.0711 18.75 15 18.75C12.9289 18.75 11.25 17.0711 11.25 15C11.25 12.9289 12.9289 11.25 15 11.25C17.0711 11.25 18.75 12.9289 18.75 15Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>

            </div>
            <div class="component">
              <h3>
                {{ this.why.title_second }}
              </h3>
              <div class="description">
                {{ this.why.description_second }}
              </div>
              <div class="icon-block">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                     fill="none">
                  <path
                      d="M3.75 5H26.25M8.55 25H21.45C23.1302 25 23.9702 25 24.612 24.673C25.1765 24.3854 25.6354 23.9265 25.923 23.362C26.25 22.7202 26.25 21.8802 26.25 20.2V14.8C26.25 13.1198 26.25 12.2798 25.923 11.638C25.6354 11.0735 25.1765 10.6146 24.612 10.327C23.9702 10 23.1302 10 21.45 10H8.55C6.86984 10 6.02976 10 5.38803 10.327C4.82354 10.6146 4.3646 11.0735 4.07698 11.638C3.75 12.2798 3.75 13.1198 3.75 14.8V20.2C3.75 21.8802 3.75 22.7202 4.07698 23.362C4.3646 23.9265 4.82354 24.3854 5.38803 24.673C6.02976 25 6.86984 25 8.55 25Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
          </div>
          <div class="block-right">
            <svg xmlns="http://www.w3.org/2000/svg" width="235" height="508" viewBox="0 0 235 508" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M0.00106812 262V508C129.343 508 234.195 394.28 234.195 254C234.195 113.72 129.343 0 0.00106812 0V246C4.41885 246.001 8 249.582 8 254C8 258.418 4.41885 261.999 0.00106812 262Z"
                    fill="white"/>
            </svg>
          </div>

        </div>

        <div class="flex-row">
          <div class="block-left">
            <div class="component">
              <h3>
                {{ this.why.title_third }}
              </h3>
              <div class="description">
                {{ this.why.description_third }}
              </div>
              <div class="icon-block">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                     fill="none">
                  <path
                      d="M5 23.5C5 20.1863 7.68629 17.5 11 17.5H19C22.3137 17.5 25 20.1863 25 23.5V23.5C25 25.7091 23.2091 27.5 21 27.5H9C6.79086 27.5 5 25.7091 5 23.5V23.5Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path
                      d="M20 7.5C20 10.2614 17.7614 12.5 15 12.5C12.2386 12.5 10 10.2614 10 7.5C10 4.73858 12.2386 2.5 15 2.5C17.7614 2.5 20 4.73858 20 7.5Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
            <div class="component">
              <h3>
                {{ this.why.title_fourth }}
              </h3>
              <div class="description">
                {{ this.why.description_fourth }}
              </div>
              <div class="icon-block">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                     fill="none">
                  <path
                      d="M13.75 25L11.25 22.5M17.5 21.25L13.125 16.875M25 13.75L20.625 9.375M21.25 17.5L18.75 15M14.0191 25.3559L25.3559 14.0191C26.5439 12.8311 27.138 12.237 27.3605 11.5521C27.5563 10.9495 27.5563 10.3005 27.3605 9.69795C27.138 9.01296 26.5439 8.41894 25.3559 7.23088L22.7691 4.64411C21.5811 3.45606 20.987 2.86204 20.3021 2.63947C19.6995 2.4437 19.0505 2.4437 18.4479 2.63947C17.763 2.86204 17.1689 3.45606 15.9809 4.64411L4.64411 15.9809C3.45606 17.1689 2.86204 17.763 2.63947 18.4479C2.4437 19.0505 2.4437 19.6995 2.63947 20.3021C2.86204 20.987 3.45606 21.5811 4.64412 22.7691L7.23089 25.3559C8.41894 26.5439 9.01296 27.138 9.69795 27.3605C10.3005 27.5563 10.9495 27.5563 11.5521 27.3605C12.237 27.138 12.8311 26.5439 14.0191 25.3559Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
          </div>
          <div class="block-right">
            <svg xmlns="http://www.w3.org/2000/svg" width="235" height="508" viewBox="0 0 235 508" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M0.00106812 262V508C129.343 508 234.195 394.28 234.195 254C234.195 113.72 129.343 0 0.00106812 0V246C4.41885 246.001 8 249.582 8 254C8 258.418 4.41885 261.999 0.00106812 262Z"
                    fill="white"/>
            </svg>
          </div>
        </div>

        <div class="flex-row">
          <div class="block-left">
            <div class="component">
              <h3>
                {{ this.why.title_fifth }}
              </h3>
              <div class="description">
                {{ this.why.description_fifth }}
              </div>
              <div class="icon-block">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                     fill="none">
                  <path
                      d="M3.75 26.25V18.75M3.75 26.25H11.25M3.75 26.25L8.125 21.875L10 20M26.25 3.75V11.25M26.25 3.75H18.75M26.25 3.75L21.875 8.125L20 10"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
            <div class="component">
              <h3>
                {{ this.why.title_sixth }}
              </h3>
              <div class="description">
                {{ this.why.description_sixth }}
              </div>
              <div class="icon-block">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"
                     fill="none">
                  <path
                      d="M11.25 15L13.75 17.5L19.375 11.875M12.4007 2.40522L6.60055 4.98307C5.56875 5.44164 5.05286 5.67092 4.67457 6.03335C4.34019 6.35372 4.08451 6.74715 3.92756 7.18282C3.75 7.6757 3.75 8.24026 3.75 9.36937L3.75 17.8248C3.75 19.0771 3.75 19.7032 3.9226 20.2716C4.07541 20.7747 4.32592 21.2428 4.65982 21.6491C5.03697 22.1079 5.55796 22.4553 6.59992 23.1499L12.3374 26.9749C13.2997 27.6164 13.7808 27.9372 14.3009 28.0618C14.7605 28.1719 15.2395 28.1719 15.6991 28.0618C16.2192 27.9372 16.7003 27.6164 17.6626 26.9749L23.4001 23.1499C24.442 22.4553 24.963 22.1079 25.3402 21.6491C25.6741 21.2428 25.9246 20.7747 26.0774 20.2716C26.25 19.7032 26.25 19.0771 26.25 17.8248L26.25 9.36937C26.25 8.24026 26.25 7.6757 26.0724 7.18282C25.9155 6.74715 25.6598 6.35372 25.3254 6.03335C24.9471 5.67092 24.4312 5.44164 23.3995 4.98307L17.5993 2.40522C16.6421 1.97982 16.1635 1.76711 15.666 1.68311C15.2251 1.60865 14.7749 1.60865 14.334 1.68311C13.8365 1.76711 13.3579 1.97982 12.4007 2.40522Z"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
          </div>
          <div class="block-right">
            <svg xmlns="http://www.w3.org/2000/svg" width="235" height="508" viewBox="0 0 235 508" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M0.00106812 262V508C129.343 508 234.195 394.28 234.195 254C234.195 113.72 129.343 0 0.00106812 0V246C4.41885 246.001 8 249.582 8 254C8 258.418 4.41885 261.999 0.00106812 262Z"
                    fill="white"/>
            </svg>
          </div>

        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "Why",
  inject: ['backendURL'],
  props: [
    'why'
  ],
  emits: [],
  methods: {}
}
</script>

<style scoped>
.why-component {
  margin-top: 12.5rem;
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-left: 1rem;
  margin-right: 1rem;
}

.why-max {
  max-width: 76rem;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.block-title {
}

.block-title h2 {
  position: sticky; /* Add this line */
  top: 8rem;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.flex-row {
  position: relative;
}

h2, h3 {
  color: #212121;
}

.block-left {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  height: 31.75rem;
}

.block-right {
  height: 31.75rem;
  position: absolute;
  right: -14.5rem;
}

.component {
  display: flex;
  width: 33.75rem;
  padding: 1.75rem 3.75rem 1.75rem 7.5rem;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  background: #FFF;
  flex: 1;
  position: relative;
}

.description {
  margin-top: 1rem;
  width: 70%;
}

.icon-block {
  position: absolute;
  top: 5.8125rem;
  left: 0;
  background: #313131;
  width: 3.75rem;
  height: 3.75rem;
}

.icon {
  position: absolute;
  left: 0.9375rem;
  top: 0.9375rem;
}

@media screen and (max-width: 1200px) {
  .description {
    font-size: 1rem;
  }
}

@media screen and (max-width: 990px) {
  .why-component {
    width: auto;
  }

  .why-max {
    flex-direction: column;
    gap: 2rem;
  }

  .block-title {
    text-align: center;
    position: relative;
    top: auto;
  }

  .block-left {
    width: 100%;
  }

  .block-right {
    display: none;
  }

  .component {
    width: auto;
  }
}

@media screen and (max-width: 640px) {
  .component {
    padding: 2rem 3.75rem 2rem 4rem;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
  }

  h3 {
    line-height: 1.3rem;
  }

  .description {
    font-size: 0.875rem;
    line-height: 1.3125rem;
    width: auto;
  }

  .block-left {
    height: auto;
  }

  .icon-block {
    width: 2.625rem;
    height: 2.625rem;
    top: 2rem;
  }

  .icon {
    left: 0.665rem;
    top: 0.665rem;
  }

  svg {
    width: 22px;
    height: 22px;
  }


}

@media screen and (max-width: 360px) {

}
</style>