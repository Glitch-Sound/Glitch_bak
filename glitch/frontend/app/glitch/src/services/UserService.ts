import http from '@/services/ApiClient'

import type { User, UserCreate, UserUpdate } from '@/types/User'

class UserService {
  public async getUsers(): Promise<User[]> {
    try {
      const response = await http.get<User[]>('/api/users')
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async createUser(user: UserCreate): Promise<User> {
    try {
      const response = await http.post<User>('/api/user', user)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async updateUser(user: UserUpdate): Promise<User> {
    try {
      const response = await http.put<User>('/api/user', user)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteUser(rid: number): Promise<void> {
    try {
      await http.delete(`/api/user/${rid}`)
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default UserService
