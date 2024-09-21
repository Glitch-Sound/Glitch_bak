import { defineStore } from 'pinia'

import type { Project, ProjectCreate, ProjectUpdate, Item, ItemRange } from '@/types/Item'
import ItemService from '@/services/ItemService'
import { STORAGE_EXPIRATION_TIME } from '@/stores/common'

const STORAGE_KEY_SELECTED_ID_PROJECT = 'selected_id_project'

const service_item = new ItemService()

const useProjectStore = defineStore('project', {
  state: () => ({
    projects: [] as Array<Project>,
    selected_id_project: loadFromLocalStorage() as number | null,
    items_range: [] as Array<ItemRange>
  }),
  actions: {
    async fetchProjects() {
      this.projects = await service_item.getProjects()
    },
    async fetchItemRange() {
      this.items_range = await service_item.getItemRange(this.selected_id_project)
    },
    setSelectedProjectID(id_project: number | null) {
      this.selected_id_project = id_project
      saveToLocalStorage(id_project)
    },
    async createProject(project: ProjectCreate): Promise<Item> {
      const result = await service_item.createProject(project)
      await this.fetchProjects()
      return result
    },
    async updateProject(project: ProjectUpdate): Promise<Item> {
      const result = await service_item.updateProject(project)
      await this.fetchProjects()
      return result
    },
    async deleteProject(rid: number): Promise<void> {
      await service_item.deleteProject(rid)
      await this.fetchProjects()
    }
  }
})

function saveToLocalStorage(selected_id_project: number | null) {
  if (selected_id_project) {
    const data = {
      selected_id_project,
      timestamp: new Date().getTime()
    }
    localStorage.setItem(STORAGE_KEY_SELECTED_ID_PROJECT, JSON.stringify(data))
  } else {
    localStorage.removeItem(STORAGE_KEY_SELECTED_ID_PROJECT)
  }
}

function loadFromLocalStorage(): number | null {
  const dataString = localStorage.getItem(STORAGE_KEY_SELECTED_ID_PROJECT)
  if (dataString) {
    const data = JSON.parse(dataString)
    const currentTime = new Date().getTime()

    if (currentTime - data.timestamp > STORAGE_EXPIRATION_TIME) {
      localStorage.removeItem(STORAGE_KEY_SELECTED_ID_PROJECT)
      return null
    }
    return data.selected_id_project as number
  }
  return null
}

export default useProjectStore
