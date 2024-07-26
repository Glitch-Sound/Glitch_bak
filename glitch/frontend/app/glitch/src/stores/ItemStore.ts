import { defineStore } from 'pinia'
import ItemService from '@/services/ItemService'
import type { Project } from '@/types/Item'

const useProjectStore = defineStore('project', {
  state: () => ({
    projects: [] as Array<Project>
  }),
  actions: {
    async fetchProjects() {
      try {
        const service_item = new ItemService()
        this.projects = await service_item.getProjects()
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
})

export default useProjectStore
