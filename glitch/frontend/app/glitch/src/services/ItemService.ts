import http from '@/services/ApiClient'

import { ExtractType } from '@/types/Item'
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
  TaskPriorityUpdate,
  BugCreate,
  BugUpdate,
  BugPriorityUpdate,
  ItemHierarchy,
  SummaryProject
} from '@/types/Item'

class ItemService {
  public async getItemsParent(rid_items: number | null): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/parent/${rid_items}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsAll(id_project: number | null): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/all/${id_project}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsIncomplete(id_project: number | null): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/incomplete/${id_project}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsHighRisk(id_project: number | null): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/high-risk/${id_project}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsAlert(id_project: number | null): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/alert/${id_project}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsAssignment(
    id_project: number | null,
    rid_users: number | undefined
  ): Promise<Item[]> {
    try {
      if (rid_users === undefined) {
        return []
      }
      const response = await http.get<Item[]>(`/api/items/assignment/${id_project}/${rid_users}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsRelation(
    id_project: number | null,
    rid_items: number | null
  ): Promise<Item[]> {
    try {
      if (rid_items == null || isNaN(rid_items)) {
        return []
      }
      const response = await http.get<Item[]>(`/api/items/relation/${id_project}/${rid_items}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsSearch(id_project: number | null, target: string | null): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/search/${id_project}/${target}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsSummaryUser(
    id_project: number | null,
    target: number | null
  ): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/summary-user/${id_project}/${target}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsByUser(
    id_project: number | null,
    rid_users: number | undefined
  ): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/${id_project}`, {
        params: {
          type_extract: ExtractType.ASSIGNMENT,
          rid_users: rid_users
        }
      })
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsByItem(
    id_project: number | null,
    rid_items: number | undefined
  ): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/${id_project}`, {
        params: {
          type_extract: ExtractType.RELATION,
          rid_items: rid_items
        }
      })
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getItemsBySearch(
    id_project: number | null,
    search: string | undefined
  ): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/${id_project}`, {
        params: {
          type_extract: ExtractType.SEARCH,
          search: search
        }
      })
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

  public async deleteProject(rid: number): Promise<void> {
    try {
      await http.delete(`/api/project/${rid}`)
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

  public async deleteFeature(rid: number): Promise<void> {
    try {
      await http.delete(`/api/feature/${rid}`)
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

  public async deleteStory(rid: number): Promise<void> {
    try {
      await http.delete(`/api/story/${rid}`)
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

  public async deleteTask(rid: number): Promise<void> {
    try {
      await http.delete(`/api/task/${rid}`)
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async updatePriorityTask(task_priority: TaskPriorityUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/task/priority', task_priority)
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

  public async deleteBug(rid: number): Promise<void> {
    try {
      await http.delete(`/api/bug/${rid}`)
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async updatePriorityBug(bug_priority: BugPriorityUpdate): Promise<Item> {
    try {
      const response = await http.put<Item>('/api/bug/priority', bug_priority)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getHierarchy(id_project: number | null): Promise<ItemHierarchy> {
    try {
      const response = await http.get<ItemHierarchy>(`/api/items/hierarchy/${id_project}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getProjectSummary(id_project: number | null): Promise<SummaryProject[]> {
    try {
      const response = await http.get<SummaryProject[]>(`/api/items/summary-project/${id_project}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getHogehoge(id_project: number | null, select_date: string): Promise<Item[]> {
    try {
      const response = await http.get<Item[]>(`/api/items/hogehoge/${id_project}/${select_date}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default ItemService
