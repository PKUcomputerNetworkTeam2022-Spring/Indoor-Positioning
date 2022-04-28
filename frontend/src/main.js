import Vue from 'vue'
import App from './App.vue'
import store from './store'
import VueKonva from 'vue-konva'
import axios from 'axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueVega from 'vue-vega'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueKonva)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueVega)

window.axios = require('axios');

Vue.config.productionTip = false


new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
