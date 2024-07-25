import http from '@/services/ApiClient'
import type { User } from '@/types/User'

export const getUsers = async (): Promise<User[]> => {
  try {
    const response = await http.get<User[]>('/api/users')
    return response.data
  } catch (error) {
    console.error('Error fetching users:', error)
    throw new Error('Failed to fetch users')
  }
}
