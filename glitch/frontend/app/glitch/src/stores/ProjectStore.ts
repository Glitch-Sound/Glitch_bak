import { defineStore } from 'pinia'

import type { Project } from '@/types/Item'
import ItemService from '@/services/ItemService'

const useProjectStore = defineStore('project', {
  state: () => ({
    projects: [] as Array<Project>,
    selected_rid_project: null as number | null
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
    setSelectedProjectRID(rid_project: number | null) {
      this.selected_rid_project = rid_project
    }
  }
})

export default useProjectStore
