import { defineStore } from 'pinia'

import type { Project, ProjectCreate, ProjectUpdate, Item, ItemRange } from '@/types/Item'
import ItemService from '@/services/ItemService'

const service_item = new ItemService()

const useProjectStore = defineStore('project', {
  state: () => ({
    projects: [] as Array<Project>,
    selected_id_project: null as number | null,
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

export default useProjectStore
