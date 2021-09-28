import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Profile from '../views/Profile.vue'
import Workshop from '../views/Workshop.vue'
import CarOwner from '../views/CarOwner.vue'
import UserForm from '../views/UserForm.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/workshop',
    name: 'Workshop',
    component: Workshop,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/car-owner',
    name: 'CarOwner',
    component: CarOwner,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/user-form',
    name: 'UserForm',
    component: UserForm,
    meta: {
        loginRequired: true,
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.loginRequired)
        && store.state.isAuthenticated === false) {
            next('/log-in')
        } else {
            next()
        }
})

export default router
