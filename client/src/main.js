import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/style.css'
import axios from "axios";

// import ElementPlus from "element-plus";
// import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(router, axios)

// app.use(ElementPlus)

let backendURL = import.meta.env.VITE_BACKEND_HOST;
axios.defaults.baseURL = backendURL

app.mount('#app')
// router.isReady().then(() => {
//   app.mount('#app')
//
//   window.ym = window.ym || function() {
//     (window.ym.a = window.ym.a || []).push(arguments)
//   }
//   window.ym.l = 1 * new Date()
//   ym(93839626, 'init', {
//     clickmap: true,
//     trackLinks: true,
//     accurateTrackBounce: true,
//     // webvisor: true,
//   })
//
//   let script = document.createElement('script')
//   script.type = 'text/javascript'
//   script.async = true
//   script.src = 'https://mc.yandex.ru/metrika/tag.js'
//   let firstScript = document.getElementsByTagName('script')[0]
//   firstScript.parentNode.insertBefore(script, firstScript)
// })

app.provide('backendURL', backendURL)

app.config.globalProperties.$projectVersion = '0.7'
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:5173'; // Set the allowed origin
// axios.defaults.headers.post['Content-Type'] = 'application/json'; // Set the Content-Type header for POST requests
