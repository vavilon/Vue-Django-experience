<template lang="html">
  <div class="">
    <galHd></galHd>

    <main>
      <div class="inner">
        <section class="main-left">

          <!-- REGISTER FORM BEGIN -->
          <form @submit.prevent="register">
            <span>用户名</span>
            <input v-model="user.username" type="text" required>
            </br>
            <span>邮箱</span>
            <input v-model="user.email" type="email" required>
            </br>
            <span>密码</span>
            <input v-model="user.password" type="password" required>
            </br>
            <button type="submit">注册</button>
            </br>
            <span>
              已有账号?
              <router-link :to="`/account/login/`">点击登陆</router-link>
            </span>
          </form>
          <!-- REGISTER FORM END -->

        </section>
      </div>
    </main>

    <galFt></galFt>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import * as Cookies from 'js-cookie'

import galHd from '../../components/header'
import galFt from '../../components/footer'
import { userRegister } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
  },
  data () {
    return {
      user: {
        username: '',
        email: '',
        password: '',
      },
      error: {
        username: '',
        email: ''
      },
    }
  },
  methods: {
    ...mapActions(['setInfo']),
    register () {
      userRegister(this.user)
      .then(res => {
        Cookies.set('name', this.user.username, { expires: 7 })
        Cookies.set('token', res.data.token, { expires: 7 })
        this.$store.dispatch('setInfo')
        this.$router.push('/')
        this.$toasted.show(`注册成功 ${this.user.username} !`, { duration: 3000, position: "bottom-right", })
      })
      .catch(err => {
        this.error.username = err.response.data.username ? err.response.data.username[0] : ''
        this.error.email = err.response.data.email ? err.response.data.email[0] : ''
        this.$toasted.show(`用户名:${this.error.username} 密码:${this.error.email}`, { duration: 5000, position: "top-right", })
      })
    }
  }
}
</script>

<style scoped>
@import '../../assets/css/register.css';
</style>
