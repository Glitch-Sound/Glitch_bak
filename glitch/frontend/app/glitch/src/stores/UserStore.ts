import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import UserService from '@/services/UserService'

const useUserStore = defineStore('user', {
  state: () => ({
    users: [] as Array<User>
  }),
  actions: {
    async fetchUsers() {
      try {
        const service_user = new UserService()
        this.users = await service_user.getUsers()
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
})

export default useUserStore
