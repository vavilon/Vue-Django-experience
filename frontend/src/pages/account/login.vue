<template lang="html">
  <div class="">
    <galHd></galHd>

    <main>
      <div class="inner">
        <section class="main-left">

          <!-- LOGIN FORM BEGIN -->
          <form @submit.prevent="userLogin()">
            <span>账号</span>
            <input type="text" v-model="user.username">
            </br>
            <span>密码</span>
            <input type="password" v-model="user.password">
            </br>
            <button type="submit">登陆</button>
            </br>
            <span>
              还没有注册?
              <router-link :to="`/account/register/`">点击注册</router-link>
            </span>
          </form>
          <!-- LOGIN FORM END -->

        </section>
      </div>
    </main>

    <galFt></galFt>
  </div>
</template>

<script>
import * as Cookies from 'js-cookie'
import {mapActions} from 'vuex'

import galHd from '../../components/header'
import galFt from '../../components/footer'
import { login } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
  },
  data () {
    return {
      user: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions(['setInfo']),
    userLogin () {
      login(this.user)
      .then(res => {
        Cookies.set('name', this.user['username'], { expires: 7 })
        Cookies.set('token', res.data.token, { expires: 7 })
        this.$store.dispatch('setInfo')
        this.$router.push('/')
        this.$toasted.show(`欢迎回来 ${this.user.username} !`, { duration: 3000, position: "bottom-right", })
      })
      .catch(err => {
        this.$toasted.show(err.response.data.non_field_errors[0], { duration: 5000, position: "top-right", })
      })
    }
  },
}
</script>

<style scoped>
@import '../../assets/css/login.css';
</style>
