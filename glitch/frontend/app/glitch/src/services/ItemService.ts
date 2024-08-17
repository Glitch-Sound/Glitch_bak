import http from '@/services/ApiClient'

import type {
  Item,
  Project,
  ProjectCreate,
  ProjectUpdate,
  EventCreate,
  EventUpdate,
  FeatureCreate,
  FeatureUpdate,
  StoryCreate,
  StoryUpdate,
  TaskCreate,
  TaskUpdate,
  BugCreate,
  BugUpdate
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

  public async updateProject(project: ProjectUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/project', project)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteProject(rid: number) {
    try {
      const response = await http.delete<Item>('/api/project', { data: { rid: rid } })
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

  public async updateEvent(event: EventUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/event', event)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteEvent(rid: number): Promise<void> {
    try {
      await http.delete(`/api/event/${rid}`)
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

  public async updateFeature(feature: FeatureUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/feature', feature)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteFeature(rid: number): Promise<Item> {
    try {
      const response = await http.delete<Item>('/api/feature', { data: { rid: rid } })
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

  public async updateStory(story: StoryUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/story', story)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteStory(rid: number): Promise<Item> {
    try {
      const response = await http.delete<Item>('/api/story', { data: { rid: rid } })
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

  public async updateTask(task: TaskUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/task', task)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteTask(rid: number): Promise<Item> {
    try {
      const response = await http.delete<Item>('/api/task', { data: { rid: rid } })
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

  public async updateBug(bug: BugUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/bug', bug)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async deleteBug(rid: number): Promise<Item> {
    try {
      const response = await http.delete<Item>('/api/bug', { data: { rid: rid } })
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default ItemService
