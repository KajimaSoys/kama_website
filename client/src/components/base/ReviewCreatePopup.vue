<template>
  <div class="question-popup-component">
    <transition name="fade">
      <div v-if="visible" class="popup-background" @click.self="close">
        <div class="popup">
          <div class="popup-max">
            <div class="popup-content">
              <h2 class="popup-title" v-if="!popup.isSubmitted">
                Оставьте свой отзыв
              </h2>
              <h2 v-else class="popup-title">
                Ваш отзыв принят!
              </h2>

              <div class="popup-description" v-if="!popup.isSubmitted">
                Расскажите что думаете о нашей компании
              </div>

              <div class="popup-description" v-else>
                <br>
                Он будет размещен после проверки
              </div>

              <div class="popup-form" v-if="!popup.isSubmitted">

                <div :class="{ 'popup-form-input': true, 'popup-name-error': popup.authorError}">
                  <input
                      v-model="this.popup.author"
                      type="text"
                      name="input1"
                      placeholder="Введите имя"
                      required
                  >
                </div>

                <div :class="{ 'popup-form-input': true, 'popup-message-error': popup.messageError}">
                <textarea
                    v-model="this.popup.message"
                    type="text"
                    name="input1"
                    rows="3"
                    required
                    placeholder="Ваш отзыв"
                ></textarea>
                </div>

                <el-upload
                    class="photo-upload-form"
                    drag
                    multiple
                    :limit="5"
                    ref="upload"
                    :file-list="fileList"
                    :on-change="handlePhotosChange"
                    :on-exceed="handleExceed"
                    :before-upload="beforePhotoUpload"
                    :http-request="customUploader"
                >
                  <el-icon class="el-icon--upload">
                    <UploadFilled/>
                  </el-icon>
                  <div class="el-upload__text">
                    Перетащите файлы сюда или <em>нажмите, чтобы загрузить</em>
                  </div>
                  <template #tip>
                    <div class="el-upload__tip">
                      Принимаются файлы размером до 3мб формата jpg/png. Максимум 5 фотографий.
                    </div>
                  </template>
                </el-upload>

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
                <span>Закрыть</span>
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
import axios from "axios";
import crypto from 'crypto-js';
import {UploadFilled} from '@element-plus/icons-vue'
import {ElMessage, ElMessageBox} from 'element-plus'


export default {
  name: "ReviewCreatePopup",
  inject: ['backendURL', 'hmac_key'],
  components: {
    UploadFilled
  },
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      fileList: [],
      popup: {
        author: '',
        message: '',
        authorError: false,
        messageError: false,
        isSubmitted: false,
      },
      sendButton: 'Отправить',
      pending: false,
    }
  },

  methods: {
    async sendPopUp(popup) {
      popup.authorError = false;
      popup.messageError = false;

      if (popup.author.length < 2) {
        popup.authorError = true;
      }

      if (popup.message.length < 3) {
        popup.messageError = true;
      }

      if (!popup.authorError && !popup.messageError) {
        this.sendButton = 'Пожалуйста, подождите..'
        this.pending = true

        let formData = new FormData();
        for (const [index, file] of this.fileList.entries()) {
          formData.append('photos', file.raw);
        }
        formData.append('author', popup.author);
        formData.append('review', popup.message || '');

        await axios
            .post('api/v1/create_review/', formData, {
              headers: {
                'Content-Type': 'multipart/form-data',
              }
            })
            .then(response => {
              this.pending = false
            })
            .catch(error => {
              console.log(error)
            })

        popup.isSubmitted = true;
      }

      setTimeout(() => {
        popup.authorError = false
        popup.messageError = false
      }, 1500)
    },

    close() {
      this.$emit('close');
    },

    handlePhotosChange(file, fileList) {
      this.fileList = fileList;
    },
    handleExceed(files, uploadFiles) {
      ElMessage.warning(
          `Лимит 5 изображений, вы выбрали ${files.length} фото, что превысило лимит`
      )
    },
    beforePhotoUpload(rawFile) {
      const validTypes = ['image/jpeg', 'image/png'];
      if (!validTypes.includes(rawFile.type)) {
        ElMessage.error('Фото должно быть в формате .jpg или .png!');
        return false;
      }
      if (rawFile.size / 1024 / 1024 > 3) {
        ElMessage.error('Изображение должно быть размером до 3мб');
        return false;
      }
      return true;
    },
    customUploader(uploadData) {
      console.log('dummy upload for', uploadData)
    }

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

input[type="text"] {
  border: 1px solid #ccc;
  padding: 1rem;
  outline: none;
  font-family: OnestRegular, Inter, sans-serif;
  width: 94%;
}

input[type="text"]:focus, textarea[type="text"]:focus {
  border-color: #212121;
}

textarea {
  border: 1px solid #ccc;
  padding: 1rem;
  outline: none;
  font-family: OnestRegular, Inter, sans-serif;
  width: 94%;
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

.popup-form-submit.success span {
  width: 100%;
  text-align: center;
  background-position: 270px;
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

.popup-name-error input, .popup-message-error textarea {
  animation: highlight 1.5s ease-out forwards;
  border: 1px solid;
}

.popup-name-error input::placeholder, .popup-message-error textarea::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  animation: highlight 1.5s ease-out forwards;
  color: inherit;
  opacity: 1;
}

.popup-name-error input:-ms-input-placeholder, .popup-message-error textarea:-ms-input-placeholder {
  color: #DD1D1D;
}

.popup-name-error input::-ms-input-placeholder, .popup-message-error textarea::-ms-input-placeholder {
  color: #DD1D1D;
}

input[type="text"]:focus::placeholder, textarea:focus::placeholder {
  color: #888888;
}

.popup-acceptance {
  color: #BBB;
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

:deep(.el-upload-dragger) {
  padding: 1rem 1rem;
}

:deep(.el-upload-dragger:hover) {
  border-color: #212121;
}

.el-upload__tip {
  line-height: 1.4rem;
}

@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 990px) {
  .popup-content {
    max-width: 27.5rem;
  }

  input[type="text"], textarea {
    width: 92%;
  }

  .popup-description {
    margin-bottom: 1rem;
  }
}

@media screen and (max-width: 640px) {
  .popup-content {
    max-width: 19.5rem;
  }

  input[type="text"], textarea {
    width: 90%;
  }

  .el-icon svg {
    height: 0.5em;
    width: 0.5em;
  }

  :deep(i.el-icon.el-icon--upload) {
    margin-bottom: 0;
  }

  :deep(.el-upload-dragger) {
    padding: 0rem 1rem 0.5rem 1rem
  }
}

@media screen and (max-width: 360px) {

}
</style>