import { defineStore } from 'pinia'

import type { Item, ItemFrequency } from '@/types/Item'
import ItemService from '@/services/ItemService'

const useAnalyzeStore = defineStore('analyze', {
  state: () => ({
    items_notice: [] as Array<Item>,
    items_frequency: [] as Array<ItemFrequency>,
    select_date: '' as string
  }),
  actions: {
    async fetchItems(id_project: number | null) {
      this.setDate(this.select_date)

      const service_item = new ItemService()
      this.items_notice = await service_item.getItemsNotice(id_project, this.select_date)
    },
    async fetchItemsFrequency(id_project: number | null) {
      this.setDate(this.select_date)

      const service_item = new ItemService()
      this.items_frequency = await service_item.getFrequency(id_project, this.select_date)
    },
    setDate(select_date: string) {
      if (select_date) {
        this.select_date = select_date
      } else {
        this.select_date = new Date().toISOString().split('T')[0]
      }
    }
  }
})

export default useAnalyzeStore
