<template lang="html">
  <div class="">
    <galHd></galHd>

    <main>
      <div class="inner">
        <section class="main-left">
          <form @submit.prevent="postArticle">
            <span>标题</span>
            <input type="text" v-model="post.title"></br>
            <span>内容</span></br>
            <textarea name="name" rows="8" cols="80" v-model="post.body"></textarea></br>
            <span>种类</span>
            <input type="text" v-model="post.category"></br>
            <button type="submit">发布</button>
          </form>
        </section>
      </div>
    </main>

    <galFt></galFt>
  </div>
</template>

<script>
import galHd from '../../components/header'
import galFt from '../../components/footer'
import { articlePost } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
  },
  data () {
    return {
      post: {
        title: "",
        body: "",
        category: null
      }
    }
  },
  methods: {
    postArticle (){
      articlePost (this.post)
      .then (res => {
        this.$router.push('/')
        this.$toasted.show(`发布文章成功!`, { duration: 5000, position: "bottom-right", })
      })
      .catch (err => {
        this.$toasted.show(`发布文章失败!`, { duration: 5000, position: "bottom-right", })
      })
    },
  },
}
</script>

<style scoped>
@import '../../assets/css/postarticle.css';
</style>
