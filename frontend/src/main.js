import Vue from 'vue'

import App from './App'
import router from './router'
import store from './store/index.js'

Vue.config.productionTip = false

/** ICON LIB BEGIN **/
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
Vue.component('icon', Icon)
/** ICON LIB END **/

/** Notification BEGIN **/
import Toasted from 'vue-toasted';
Vue.use(Toasted)
/** Notification END **/

new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
