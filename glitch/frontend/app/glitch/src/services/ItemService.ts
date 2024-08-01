import http from '@/services/ApiClient'

import type {
  Item,
  Project,
  ProjectCreate,
  EventCreate,
  FeatureCreate,
  StoryCreate,
  TaskCreate,
  BugCreate
} from '@/types/Item'

class ItemService {
  public async getItems(rid_items: number): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>('/api/items/' + String(rid_items))
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

  public async createFeature(feature: FeatureCreate): Promise<Item> {
    try {
      const response = await http.post<Item>('/api/feature', feature)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async createStory(story: StoryCreate): Promise<Item> {
    try {
      const response = await http.post<Item>('/api/story', story)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async createTask(task: TaskCreate): Promise<Item> {
    try {
      const response = await http.post<Item>('/api/task', task)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async createBug(bug: BugCreate): Promise<Item> {
    try {
      const response = await http.post<Item>('/api/bug', bug)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default ItemService
