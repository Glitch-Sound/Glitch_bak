import { defineStore } from 'pinia'

import type { Item, ItemFrequency } from '@/types/Item'
import ItemService from '@/services/ItemService'

const service_item = new ItemService()

const useAnalyzeStore = defineStore('analyze', {
  state: () => ({
    items_notice: [] as Array<Item>,
    items_frequency: [] as Array<ItemFrequency>,
    date_selected: '' as string
  }),
  actions: {
    async fetchItems(id_project: number | null) {
      this.items_notice = await service_item.getItemsNotice(id_project, this.date_selected)
    },
    async fetchItemsFrequency(id_project: number | null) {
      this.items_frequency = await service_item.getFrequency(id_project)
    },
    setDateSelected(date_selected: string) {
      if (date_selected != '') {
        this.date_selected = date_selected
      } else {
        this.date_selected = new Date().toISOString().split('T')[0]
      }
    }
  }
})

export default useAnalyzeStore
