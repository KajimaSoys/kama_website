<template>
  <div class="question-popup-component">
    <transition name="fade">
      <div v-if="visible" class="popup-background" @click.self="close">
        <div class="popup">
          <div class="popup-max">
            <div class="popup-content">
              <h2 class="popup-title" v-if="!popup.isSubmitted">
                Задать вопрос
              </h2>
              <h2 v-else class="popup-title">
                Ваша заявка принята!
              </h2>

              <div class="popup-description">
                Мы свяжемся с вами в течение 10 минут и поможем разобраться
              </div>

              <div class="popup-form" v-if="!popup.isSubmitted">

                <div :class="{ 'popup-form-input': true, 'popup-name-error': popup.nameError}">
                  <input
                      v-model="this.popup.name"
                      type="text"
                      name="input1"
                      placeholder="Введите имя"
                      required
                  >
                </div>

                <div :class="{ 'popup-form-input': true, 'popup-phone-error': popup.phoneError}">
                  <input
                      type="text"
                      name="input1"
                      placeholder="+7 (___) ___-__-__"
                      v-mask="'+7 (###) ###-##-##'"
                      required
                      v-model="this.popup.phone"
                  >
                </div>

                <div class="popup-form-input">
                <textarea
                    v-model="this.popup.message"
                    type="text"
                    name="input1"
                    rows="5"
                    placeholder="Ваш вопрос"
                ></textarea>
                </div>

                <div class="popup-form-submit" :class="{ 'pending': pending}" @click="this.sendPopUp(this.popup)">
                  <span>{{ this.sendButton }}</span>
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M3 11.9999H21M21 11.9999L14 5M21 11.9999L14 18.9999" stroke="white" stroke-width="1.5"
                          stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>

                <div class="popup-acceptance">
                  Нажимая кнопку «Отправить» вы даете согласие на обработку персональных данных и принимаете условия
                  <router-link to="policy" class="popup-link">политики
                    конфиденциальности
                  </router-link>
                </div>
              </div>

              <div class="popup-form-submit success" v-else @click="close">
                Закрыть
              </div>
            </div>
          </div>

          <button class="close-btn" @click="close" ref="closePopUp">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M8 24L24 8M8 8L24 24" stroke="#9F9F9F" stroke-width="1.5" stroke-linecap="round"
                    stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import {mask} from "vue-the-mask";
import axios from "axios";

export default {
  name: "QuestionPopup",
  inject: ['backendURL'],
  directives: {mask},
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      popup: {
        name: '',
        phone: '',
        message: '',
        nameError: false,
        phoneError: false,
        isSubmitted: false,
      },
      sendButton: 'Отправить',
      pending: false,
    }
  },

  methods: {
    async sendPopUp(popup) {
      popup.nameError = false;
      popup.phoneError = false;

      if (popup.name.length < 2) {
        popup.nameError = true;
      }

      if (popup.phone.length !== 18) {
        popup.phoneError = true;
      }

      if (!popup.nameError && !popup.phoneError) {
        this.sendButton = 'Пожалуйста, подождите..'
        this.pending = true

        let body = {
          request: {
            name: popup.name,
            number: popup.phone,
            message: popup.message || '',

            project_version: this.$projectVersion,
            user_agent: navigator.userAgent,
            screen_resolution: `${window.screen.width}x${window.screen.height}`,
            browser_language: navigator.language,
            timezone: new Date().getTimezoneOffset(),
            cookie: document.cookie
          }
        }

        await axios
            .post('api/v1/create_order/', body)
            .then(response => {
              this.pending = false
              console.log(response)
            })
            .catch(error => {
              console.log(error)
            })

        popup.isSubmitted = true;
      }

      setTimeout(() => {
        popup.nameError = false
        popup.phoneError = false
      }, 1500)
    },

    close() {
      this.$emit('close');
    },
  },
}
</script>


<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.popup-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 101;
}

.popup {
  background-color: white;
  padding: 4rem 2rem;
  position: relative;
  z-index: 101;
}

.close-btn {
  position: absolute;
  z-index: 101;
  top: 1rem;
  right: 1rem;
  background: transparent;
  border: none;
  font-size: 3rem;
  cursor: pointer;
}

.close-btn path {
  transition: all 0.1s ease-in-out;
}

.close-btn:hover path {
  stroke: #000;
}

.popup-content {
  max-width: 33.5rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  align-items: center;
}

.popup-title {
  color: #212121;
  text-align: center;
  letter-spacing: -0.0525rem;
  margin-bottom: 0.5rem;
}

.popup-description {
  color: #212121;
  text-align: center;
  font-size: 1.125rem;
  line-height: normal;
  margin-bottom: 4rem;
  width: 65%;
}

.popup-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
}

input[type="text"], input[type="tel"] {
  border: 1px solid #ccc;
  padding: 1rem;
  outline: none;
  font-family: OnestRegular, Inter, sans-serif;
  width: 92%;
}

input[type="text"]:focus, input[type="tel"]:focus {
  border-color: #212121;
}

textarea {
  border: 1px solid #ccc;
  padding: 1rem;
  outline: none;
  font-family: OnestRegular, Inter, sans-serif;
  width: 92%;
  resize: none;
}

.popup-form-submit {
  display: flex;
  padding: 1rem 1.25rem;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;
  cursor: pointer;
  background: #212121;
  color: #fff;
  font-size: 1rem;
  position: relative;
  transition: background-color 0.5s ease;
}

.popup-form-submit:hover {
  background: #21212100;
}

.popup-form-submit:before {
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

.popup-form-submit:hover:before {
  clip-path: inset(-10% 0 0 -10%);
}

.popup-form-submit span {
  color: #ffffff;
  text-align: left;
  font-size: 1.125rem;
  position: relative;
  background: linear-gradient(to right, #212121, #212121 50%, #ffffff 50%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-size: 500% 100%;
  background-position: 200px;
  transition: background-position .3s ease-in-out;
}

.popup-form-submit:hover span {
  background-position: 0 100%;
}

.popup-form-submit svg {
  z-index: 1;
}

.popup-form-submit path {
  transition: stroke 0.4s ease;
}

.popup-form-submit:hover path {
  stroke: #212121;
}

.success {
  justify-content: center
}

.pending {
  pointer-events: none;
}

@keyframes highlight {
  0% {
    border-color: #DD1D1D;
    color: #DD1D1D;
  }
  100% {
    border-color: #ccc;
    color: #a8a9aa;
  }
}

.popup-name-error input, .popup-phone-error input {
  animation: highlight 1.5s ease-out forwards;
  border: 1px solid;
}

.popup-name-error input::placeholder, .popup-phone-error input::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  animation: highlight 1.5s ease-out forwards;
  color: inherit;
  opacity: 1;
}

.popup-name-error input:-ms-input-placeholder, .popup-phone-error input:-ms-input-placeholder {
  color: #DD1D1D;
}

.popup-name-error input::-ms-input-placeholder, .popup-phone-error input::-ms-input-placeholder {
  color: #DD1D1D;
}

input[type="text"]:focus::placeholder, input[type="tel"]:focus::placeholder {
  color: #888888;
}

.popup-acceptance {
  color: #BBB;
  font-family: Inter, serif;
  font-size: 0.75rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
}

.popup-acceptance a {
  color: #000000;
  position: relative;
  text-decoration: underline;
  transition: opacity 0.2s ease-in-out;
  opacity: 1;

}

.popup-acceptance a:hover {
  opacity: 0.5;
}

:deep(.el-input__wrapper) {
  padding: 10px 21px !important;
  border-radius: 13px !important;
}

@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 990px) {
  .popup-content {
    max-width: 27.5rem;
  }
}

@media screen and (max-width: 640px) {
  .popup-content {
    max-width: 19.5rem;
  }
}

@media screen and (max-width: 360px) {

}
</style>