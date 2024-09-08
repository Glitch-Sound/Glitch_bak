import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import UserService from '@/services/UserService'

const useProgressStore = defineStore('progress', {
  state: () => ({
    users: [] as Array<User>,
    rid_users: 0 as number
  }),
  actions: {
    async fetchUsers(id_project: number) {
      try {
        const service_user = new UserService()
        this.users = await service_user.getUsersProject(id_project)
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setTarget(rid_users: number) {
      this.rid_users = rid_users
    }
  }
})

export default useProgressStore
