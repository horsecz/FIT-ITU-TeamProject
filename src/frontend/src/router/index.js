import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/Login.vue'
import Trip from '@/components/Trip.vue'
import Settings from '@/components/Settings.vue'
import Register from '@/components/Register.vue'
import NewTrip from '@/components/NewTrip.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: {
        name: 'login'
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/trip',
      name: 'Trip',
      component: Trip
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
      path: '/NewTrip',
      name: 'NewTrip',
      component: NewTrip
    }
  ]
})
