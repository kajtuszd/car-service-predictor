import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Profile from '../views/Profile.vue'
import Workshop from '../views/Workshop.vue'
import WorkshopList from '../components/views/WorkshopList.vue'
import CarDetail from '../components/views/CarDetail.vue'
import CarOwner from '../views/CarOwner.vue'
import UserForm from '../views/UserForm.vue'
import UpdateCar from '../views/UpdateCar.vue'
import UpdateService from '../views/UpdateService.vue'
import UpdateCarPart from '../views/UpdateCarPart.vue'
import CarForm from '../views/CarForm.vue'
import CarPartForm from '../views/CarPartForm.vue'
import WorkshopForm from '../views/WorkshopForm.vue'
import ServiceForm from '../views/ServiceForm.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
    path: '/profile/car-form',
    name: 'CarForm',
    component: CarForm,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/service-form',
    name: 'ServiceForm',
    component: ServiceForm,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/car-owner/:slug',
    name: 'CarDetail',
    component: CarDetail,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/car-owner/:slug/update-part/:part_slug',
    name: 'UpdateCarPart',
    component: UpdateCarPart,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/car-owner/:slug/update',
    name: 'UpdateCar',
    component: UpdateCar,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/workshop/update-service/:slug',
    name: 'UpdateService',
    component: UpdateService,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/profile/car-owner/:slug/car-part-form',
    name: 'CarPartForm',
    component: CarPartForm,
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
  {
    path: '/profile/workshop-form',
    name: 'WorkshopForm',
    component: WorkshopForm,
    meta: {
        loginRequired: true,
    }
  },
  {
    path: '/workshop-list',
    name: 'WorkshopList',
    component: WorkshopList,
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
