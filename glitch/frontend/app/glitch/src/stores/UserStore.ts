import { defineStore } from 'pinia'

import type { User, UserCreate, UserUpdate, Login } from '@/types/User'
import UserService from '@/services/UserService'
import useProgressStore from '@/stores/ProgressStore'

const service_user = new UserService()

const STORAGE_KEY = 'login_user'
const STORAGE_EXPIRATION_TIME = 12 * 60 * 60 * 1000

const useUserStore = defineStore('user', {
  state: () => ({
    users: [] as Array<User>,
    login_user: loadFromLocalStorage() as User | null
  }),
  actions: {
    async fetchUsers() {
      this.users = await service_user.getUsers()
    },
    async createUser(user: UserCreate, is_admin: boolean = false): Promise<User> {
      const result = await service_user.createUser(user)
      if (is_admin) {
        this.login_user = result
        saveToLocalStorage(result)
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
      saveToLocalStorage(result)

      const store_progress = useProgressStore()
      store_progress.setUser(result.rid)
      return result
    }
  }
})

function saveToLocalStorage(user: User | null) {
  if (user) {
    const data = {
      user,
      timestamp: new Date().getTime()
    }
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data))
  } else {
    localStorage.removeItem(STORAGE_KEY)
  }
}

function loadFromLocalStorage(): User | null {
  const dataString = localStorage.getItem(STORAGE_KEY)
  if (dataString) {
    const data = JSON.parse(dataString)
    const currentTime = new Date().getTime()

    if (currentTime - data.timestamp > STORAGE_EXPIRATION_TIME) {
      localStorage.removeItem(STORAGE_KEY)
      return null
    }
    return data.user as User
  }
  return null
}

export default useUserStore
