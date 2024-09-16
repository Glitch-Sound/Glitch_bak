import { defineStore } from 'pinia'

import type { SummaryItem } from '@/types/Summary'
import SummaryService from '@/services/SummaryService'
import ItemService from '@/services/ItemService'

const useSummaryStore = defineStore('summary', {
  state: () => ({
    summaries_project: [] as Array<SummaryItem>,
    summaries_item: new Map<number, Array<SummaryItem>>()
  }),
  actions: {
    async fetchSummaryProject(id_project: number | null) {
      if (id_project) {
        const service_summary = new SummaryService()
        this.summaries_project = await service_summary.getSummariesProject(id_project)
      }
    },
    async fetchSummaryItem(rid: number) {
      const service_summary = new SummaryService()
      const items = await service_summary.getSummariesItem(rid)

      if (items) {
        this.summaries_item.set(rid, items)
      }
    },
    async updateTaskBug(rid: number) {
      const service_summary = new ItemService()
      const ancestors_item = await service_summary.getAncestorsItemsRID(rid)

      for (const item of ancestors_item) {
        this.fetchSummaryItem(item.rid)
      }
    }
  }
})

export default useSummaryStore
