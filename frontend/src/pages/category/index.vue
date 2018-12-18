<template lang="html">
  <div class="">
    <galHd></galHd>

    <main>
      <div class="inner">
        <section class="main-left">

          <ul>
            <li v-for="(category, index) of categorys">
              <router-link :to="`/?search=${category.text}`">
                {{ category.text }}
              </router-link>
            </li>
          </ul>

        </section>
      </div>
    </main>

    <galFt></galFt>
  </div>
</template>

<script>
import galHd from '../../components/header'
import galFt from '../../components/footer'
import { categoryList } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
  },
  data () {
    return {
      categorys: []
    }
  },
  methods: {
    fetchData () {
      categoryList()
      .then(res => {
        this.categorys = res.data.results
      })
    }
  },
  created () {
    this.fetchData()
  },
}
</script>

<style scoped>
@import '../../assets/css/category.css';
</style>
