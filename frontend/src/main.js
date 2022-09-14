import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from 'axios'

Vue.config.productionTip = false
// TODO: parametrize API URL (take from ENV)
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
Vue.prototype.$http = axios

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
