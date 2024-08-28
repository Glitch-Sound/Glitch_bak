import { defineStore } from 'pinia'

import type { SummaryItem } from '@/types/Summary'
import SummaryService from '@/services/SummaryService'

const useSummaryStore = defineStore('summary', {
  state: () => ({
    summaries_item: new Map<number, Array<SummaryItem>>()
  }),
  actions: {
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
    async updateTask(rid: number) {
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
