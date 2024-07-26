import http from '@/services/ApiClient'
import type { Item, ProjectCreate } from '@/types/Item'

class ItemService {
  public async getItems(): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>('/api/items')
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async createProject(project: ProjectCreate): Promise<Item> {
    try {
      const response = await http.post<Item>('/api/project', project)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default ItemService
