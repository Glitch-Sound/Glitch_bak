import { createRouter, createWebHistory } from 'vue-router'

import useUserStore from '@/stores/UserStore'
import MainView from '@/views/MainView.vue'
import ProjectView from '@/views/main/ProjectView.vue'
import ProgressView from '@/views/main/ProgressView.vue'
import AnalyzeView from '@/views/main/AnalyzeView.vue'
import SettingMainView from '@/views/setting/SettingMainView.vue'
import SettingUserView from '@/views/setting/SettingUserView.vue'
import SettingProjectView from '@/views/setting/SettingProjectView.vue'

const base = import.meta.env.VITE_APP_BASE_URL || '/'

const router = createRouter({
  history: createWebHistory(base),
  routes: [
    {
      path: '/',
      component: MainView
    },
    {
      path: '/project/:id_project/:extruct?/:target?',
      component: ProjectView,
      meta: { requiresAuth: true }
    },
    {
      path: '/progress/:id_project/:target',
      component: ProgressView,
      meta: { requiresAuth: true }
    },
    {
      path: '/analyze/:id_project',
      component: AnalyzeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/setting',
      children: [
        {
          path: 'main',
          component: SettingMainView
        },
        {
          path: 'user',
          component: SettingUserView
        },
        {
          path: 'project',
          component: SettingProjectView
        }
      ],
      meta: { requiresAuth: true }
    }
  ]
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)

  if (requiresAuth && !userStore.login_user) {
    next('/')
  } else {
    next()
  }
})

export default router
