import { defineStore } from 'pinia'

import type { User, UserCreate, UserUpdate, Login } from '@/types/User'
import UserService from '@/services/UserService'
import useProgressStore from '@/stores/ProgressStore'

const service_user = new UserService()

const useUserStore = defineStore('user', {
  state: () => ({
    users: [] as Array<User>,
    login_user: null as User | null
  }),
  actions: {
    async fetchUsers() {
      this.users = await service_user.getUsers()
    },
    async createUser(user: UserCreate, is_admin: boolean = false): Promise<User> {
      const result = await service_user.createUser(user)
      if (is_admin) {
        this.login_user = result
      }
      await this.fetchUsers()
      return result
    },
    async updateUser(user: UserUpdate): Promise<User> {
      return service_user.updateUser(user)
    },
    async deleteUser(rid: number): Promise<void> {
      return service_user.deleteUser(rid)
    },
    async login(user: Login): Promise<User> {
      const result = await service_user.login(user)
      this.login_user = result

      const store_progress = useProgressStore()
      store_progress.setUser(result.rid)
      return result
    }
  }
})

export default useUserStore
