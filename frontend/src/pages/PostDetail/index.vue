<template lang="html">
  <div class="">
    <galHd></galHd>
    <main>
      <div class="inner">
        <!-- POST DETAIL BEGIN -->
        <section class="main-left">
          <h1 class="post-title">{{ article.title }}</h1>
          <div class="post-header">
            <span>{{ article.created|moment }}</span>
            <span>{{ article.views }} 阅读</span>
            <span>{{ article.comment_count }} 评论</span>
          </div>
          <div class="post-body">
            <vue-markdown :source="article.body"></vue-markdown>
          </div>
          <div class="post-comment">
            <section v-if="!(comments && comments.length)">还没有评论!</section>
            <div class="add-comment" v-if="loginState === true">
              <input type="text" v-model="newComment.content">
              <span @click="addComment">添加评论</span>
            </div>
            <router-link :to="`/account/login/`" class="add-comment" v-if="!loginState === true">
              <span>登陆后才可以评论!</span>
            </router-link>
            <section v-for="(comment, index) of comments">
              <span>{{ comment.author_name }}</span>
              <span>{{ comment.created|moment }}</span>
              <p>{{ comment.content }}</p>
            </section>
          </div>
        </section>
        <!-- POST DETAIL END -->
      </div>
    </main>
    <galFt></galFt>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'

import '../../filter/moment.js'
import galHd from '../../components/header'
import galFt from '../../components/footer'
import { articleDetail, commentList, commentPost } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
    VueMarkdown,
  },
  computed: {
    loginState () {
      return this.$store.state.loggedIn
    },
  },
  data () {
    return {
      article: [],
      comments: [],
      newComment: {
        content: '',
        article: this.$route.params.id
      },
    }
  },
  methods: {
    addComment () {
      commentPost (this.newComment)
      .then (res => {
        this.$toasted.show(`添加评论成功!`, { duration: 5000, position: "bottom-right", })
        this.$router.go(0)
      })
      .catch (err => {
        this.$toasted.show(`添加评论失败,请刷新后再试!`, { duration: 3000, position: "bottom-right", })
      })
    }
  },
  created () {
    // 获取文章列表
    articleDetail(this.$route.params.id)
    .then( res => {
      this.article = res.data
    })
    // 获取评论列表
    commentList(this.$route.params.id)
    .then( res => {
      this.comments = res.data.results
    })
  }
}

</script>

<style scoped>
@import '../../assets/css/github-markdown.css';
@import '../../assets/css/post_detail.css';
</style>
