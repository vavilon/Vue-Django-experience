<template lang="html">
  <div class="">
    <galHd></galHd>

    <main>
      <div class="inner">
        <section class="main-left">
          <span>用户名: {{ userName }}</span></br>
          <span>个人积分: {{ points }}</span></br>
          <router-link class="p" tag="span" :to="`/account/postarticle/`">
            发布文章
          </router-link></br>
          <span @click="loginOut">注销</span>
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
import { userInfo } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
  },
  data () {
    return {
      points: 0,
    }
  },
  computed: {
    userName () {
      return this.$store.state.userInfo['name']
    }
  },
  methods: {
    ...mapActions(['setInfo']),
    fetchData () {
      userInfo(this.userName)
      .then(res => {
        this.points = res.data.point
      })
    },
    loginOut () {
      Cookies.remove('nmae')
      Cookies.remove('token')
      Cookies.remove('csrftoken')
      Cookies.remove('tabstyle')
      this.$store.dispatch('userLoginOut')
      this.$router.push('/account/login/')
    }
  },
  created () {
    this.fetchData()
  }
}
</script>

<style scoped>
@import '../../assets/css/userinfo.css';
</style>
