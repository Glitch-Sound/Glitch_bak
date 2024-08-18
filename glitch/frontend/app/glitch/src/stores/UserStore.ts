import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import UserService from '@/services/UserService'

const useUserStore = defineStore('user', {
  state: () => ({
    users: [] as Array<User>,
    login_user: null as User | null
  }),
  actions: {
    async fetchUsers() {
      try {
        const service_user = new UserService()
        this.users = await service_user.getUsers()
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setLoginUser(user: User | null) {
      this.login_user = user
    }
  }
})

export default useUserStore
