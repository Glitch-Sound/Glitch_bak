import http from '@/services/ApiClient'

import type { User, UserCreate } from '@/types/User'

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
}

export default UserService
