import { defineStore } from 'pinia'

import type { SummaryProject, SummaryItem } from '@/types/Summary'
import SummaryService from '@/services/SummaryService'

const useSummaryStore = defineStore('summary', {
  state: () => ({
    summaries_project: [] as Array<SummaryProject>,
    summaries_item: new Map<number, Array<SummaryItem>>()
  }),
  actions: {
    async fetchSummaryProject(id_project: number | null) {
      try {
        if (id_project) {
          const service_summary = new SummaryService()
          this.summaries_project = await service_summary.getSummariesProject(id_project)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    async fetchSummaryItem(rid: number) {
      try {
        const service_summary = new SummaryService()
        const items = await service_summary.getSummariesItem(rid)

        if (items) {
          this.summaries_item.set(rid, items)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    async updateTaskBug(rid: number) {
      try {
        const service_summary = new SummaryService()
        const ancestors_item = await service_summary.getAncestorsItem(rid)

        for (const item of ancestors_item) {
          this.fetchSummaryItem(item.rid)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
})

export default useSummaryStore
