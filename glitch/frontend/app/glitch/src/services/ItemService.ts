import http from '@/services/ApiClient'
import type { Item, Project, ProjectCreate, EventCreate } from '@/types/Item'

class ItemService {
  public async getItems(): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>('/api/items')
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getProjects(): Promise<Project[]> {
    try {
      const response = await http.get<Project[]>('/api/projects')
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

  public async createEvent(event: EventCreate): Promise<Item> {
    try {
      const response = await http.post<Item>('/api/event', event)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default ItemService
