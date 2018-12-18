import Vue from 'vue'
import Router from 'vue-router'
import * as Cookies from 'js-cookie'

import Home from '../pages/home/index'
import PostDetail from '../pages/postdetail/index'
import Category from '../pages/category/index'
import Login from '../pages/account/login'
import Register from '../pages/account/register'
import UserInfo from '../pages/account/userInfo'
import PostArticle from '../pages/account/postArticle'

import store from '../store/index.js'
import * as types from '../store/mutation-types'

Vue.use(Router)

const routes = [
    {
      /** 首页 **/
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        title: '首页 - Blog',
        requireAuth: false,
      }
    },
    {
      /** 文章详情页 **/
      path: '/post/:id/',
      name: 'PostDetail',
      component: PostDetail,
      meta: {
        requireAuth: false,
      }
    },
    {
      /** 文章分类页 **/
      path: '/categorys/',
      name: 'Category',
      component: Category,
      meta: {
        requireAuth: false,
      }
    },
    {
      /** 登陆页 **/
      path: '/account/login/',
      name: 'login',
      component: Login,
      meta: {
        requireAuth: false,
      }
    },
    {
      /** 注册页 **/
      path: '/account/register/',
      name: 'register',
      component: Register,
      meta: {
        requireAuth: false,
      }
    },
    {
      /** 个人资料 **/
      path: '/account/userinfo/',
      name: 'userinfo',
      component: UserInfo,
      meta: {
        requireAuth: true,
      }
    },
    {
      /** 个人资料 **/
      path: '/account/postarticle/',
      name: 'PostArticle',
      component: PostArticle,
      meta: {
        requireAuth: true,
      }
    },
]


if (Cookies.get('token')) {
  store.commit(types.SET_INFO)
}

const router = new Router({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(r => r.meta.requireAuth)) {
    if (store.state.userInfo['token']) {
      next();
    } else {
      next({
        path: '/account/login/',
      })
    }
  } else {
      next();
  }
})

export default router;
