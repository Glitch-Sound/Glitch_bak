import { defineStore } from 'pinia'

import type { Project } from '@/types/Item'
import ItemService from '@/services/ItemService'

const useProjectStore = defineStore('project', {
  state: () => ({
    projects: [] as Array<Project>,
    selected_id_project: null as number | null
  }),
  actions: {
    async fetchProjects() {
      try {
        const service_item = new ItemService()
        this.projects = await service_item.getProjects()
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setSelectedProjectID(id_project: number | null) {
      this.selected_id_project = id_project
    }
  }
})

export default useProjectStore
