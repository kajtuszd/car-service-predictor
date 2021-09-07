import Vue from 'vue'
import App from './App.vue'
// import axios from 'axios'

Vue.config.productionTip = false

// axios.defaults.baseURL = 'http://0.0.0.0:8000/'

new Vue({
  render: h => h(App),
}).$mount('#app')
