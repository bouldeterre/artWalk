import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing-page',
      component: require('@/components/LandingPage').default
    },
    {
      path: '/informations',
      name: 'informations',
      component: require('@/components/InfoPage').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
