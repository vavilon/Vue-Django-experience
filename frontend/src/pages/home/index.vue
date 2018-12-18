<template>
  <div class="">
    <galHd></galHd>
    <main>
      <div class="inner">
        <!-- POSTLIST BEGIN -->
        <section class="main-left">

          <!-- POSTLIST HEADER -->
          <div class="post-filter">
            <a @click="isFilter('created')">最新</a>
            <a @click="isFilter('views')">热门</a>
          </div>

          <!-- POSTLIST MAIN -->
          <div v-if="articles && articles.length">
            <article class="post-list" v-for="(art, index) of articles">
              <div class="post-list-header">
                <span>{{ art.author_name }}</span>
                <span>{{ art.updated|moment }}</span>
              </div>
              <h2 class="post-list-title">
                <router-link :to="`/post/${art.id}/`">
                  {{ art.title }}
                </router-link>
              </h2>
              <vue-markdown :source="cutBody(art.body)" class="post-list-body">
              </vue-markdown>
              <div class="post-list-footer">
                <span>
                  <icon name="eye" scale="0.8"></icon>
                  {{ art.views }}
                </span>
                <span>
                  <icon name="comments" scale="0.8"></icon>
                  {{ art.comment_count }}
                </span>
              </div>
            </article>
          </div>

          <div v-if="!(articles && articles.length)">
            还没有文章发布!
          </div>
          <div class="post-footer">
            <nav class="pagination">
              <router-link v-for="p of pageCount"
              :class="{'current': isSelect(p+1)}"
              :to="`?page=${p+1}`" :key="p">
                {{ p+1 }}
              </router-link>
            </nav>
          </div>
        </section>
        <!-- POSTLIST END -->
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
import { articleList } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
    VueMarkdown,
  },
  data () {
    return {
      articles: [],
      pageCount: 1,
      pageCurrent: 1,
      orderByCreated: false,
      orderByViews: false,
    }
  },
  methods: {
    isFilter (order) {
      if (order === 'created') {
        this.orderByCreated = !this.orderByCreated
        this.fetchData()
      } else if (order === 'views') {
        this.orderByViews = !this.orderByViews
        this.fetchData()
      }
    },
    // 问题文本截取
    cutBody (value) {
      if (value.length > 150) {
        return value.slice(0, 150) + '...';
      } else {
        return value;
      }
    },
    isSelect (p) {
      let x = p === this.pageCurrent ? true : false
      return x
    },
    // 获取数据
    fetchData () {
      if (this.$route.query.page) {
        this.pageCurrent = this.$route.query.page
      }
      let views = this.orderByViews ? '&ordering=-views': ''
      let created = this.orderByCreated ? '&ordering=-created': ''
      if (this.$route.query.search) {
        var search = `&search=${this.$route.query.search}`
      } else {
        var search = ''
      }
      let order = views + created
      articleList(this.pageCurrent, order, search)
      .then( res => {
        this.articles = res.data.results
        this.pageCount = [...Array(Math.ceil(res.data.count / 10)).keys()]
      })
    }
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
}
</script>

<style scoped>
@import '../../assets/css/github-markdown.css';
@import '../../assets/css/home.css';
</style>
