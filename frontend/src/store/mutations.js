import * as types from './mutation-types'
import * as Cookies from 'js-cookie'

export const mutations = {
  [types.SET_INFO] (state) {
    let uname = Cookies.get('name')
    let utoken = Cookies.get('token')
    state.userInfo = {
      name: uname,
      token: utoken
    }
    state.loggedIn = true
  },
  [types.LOGINOUT] (state) {
    state.userInfo = {
      name: null,
      token: null
    }
    state.loggedIn = false
  }
}

export default mutations
