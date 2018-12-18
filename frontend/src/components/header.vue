<template>

  <!-- GLOBAL HEADER BEGIN -->
  <header>
    <div class="inner">
      <a class="logo">Blog</a>
      <nav>
        <router-link :to="`/`">首页</router-link>
        <router-link :to="`/categorys/`">分类</router-link>
      </nav>
      <form class="">
        <input type="text" placeholder="搜索...">
        <button type="submit">
          <icon name="search" scale="1"></icon>
        </button>
      </form>
      <div class="user">
        <router-link v-if="loginState === true" :to="`/account/userinfo/`">
          <icon name="user" scale="1.3"></icon>
        </router-link>
        <router-link v-if="loginState === false" :to="`/account/login/`">
          <icon name="sign-in" scale="1"></icon>
        </router-link>
      </div>
    </div>
  </header>
  <!-- GLOBAL HEADER END -->

</template>

<script>
export default {
  computed: {
    loginState () {
      return this.$store.state.loggedIn
    },
    userName () {
      return this.$store.state.userInfo['name']
    }
  },
}
</script>

<style scoped>
@import '../assets/css/header.css';
</style>
