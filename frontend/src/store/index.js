import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex);

const state = {
    userInfo: {
      name: null,
      token: null,
    },
    loggedIn: false,
}

export default new Vuex.Store({
    state,
    mutations,
    actions
})
