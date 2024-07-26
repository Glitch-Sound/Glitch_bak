import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/main/MainView.vue'
import ProjectView from '@/views/main/ProjectView.vue'
import SettingMainView from '@/views/setting/SettingMainView.vue'
import SettingUserView from '@/views/setting/SettingUserView.vue'
import SettingProjectView from '@/views/setting/SettingProjectView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: MainView
    },
    {
      path: '/project/:rid',
      component: ProjectView
    },
    {
      path: '/setting',
      children: [
        {
          path: '',
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
      ]
    }
  ]
})

export default router
