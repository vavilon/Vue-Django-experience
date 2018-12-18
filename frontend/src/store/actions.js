import * as types from './mutation-types'

const actions ={

  setInfo({commit}){
    commit(types.SET_INFO);
  },
  userLoginOut({commit}){
    commit(types.LOGINOUT)
  }
}

export default actions
