import axios from 'axios'
import * as Cookies from 'js-cookie'

const baseUrl = "http://localhost:8000/api/v1/"
axios.defaults.headers.common['Authorization'] = 'JWT ' + Cookies.get('token')

// 文章列表
export const articleList = (page, order, search) => {
  return axios.get(`${baseUrl}posts/?page=${page}${order}${search}`)
}

// 文章详情
export const articleDetail = params => {
  return axios.get(`${baseUrl}posts/${params}/`)
}

// 评论列表
export const commentList = params => {
  return axios.get(`${baseUrl}comments/?search=${params}`)
}

// 种类列表
export const categoryList = () => {
  return axios.get(`${baseUrl}categorys/`)
}

// 用户登陆
export const login = params => {
  return axios.post(`${baseUrl}login/`, params)
}

// 用户资料
export const userInfo = params => {
  return axios.get(`${baseUrl}users/${params}/`)
}

// 用户注册
export const userRegister = params => {
  return axios.post(`${baseUrl}register/`, params)
}

// 添加评论
export const commentPost = params => {
  return axios.post(`${baseUrl}comments/`, params)
}

// 发布文章
export const articlePost = params => {
  return axios.post(`${baseUrl}posts/`, params)
}
