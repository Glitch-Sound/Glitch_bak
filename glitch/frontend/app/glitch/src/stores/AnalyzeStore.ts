import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import type { Item, ItemHierarchy, ItemFrequency } from '@/types/Item'
import type { SummaryUser } from '@/types/Summary'
import ItemService from '@/services/ItemService'
import UserService from '@/services/UserService'
import SummaryService from '@/services/SummaryService'
import useItemStore from '@/stores/ItemStore'

const useAnalyzeStore = defineStore('analyze', {
  state: () => ({
    items: [] as Array<Item>,
    items_frequency: [] as Array<ItemFrequency>,
    select_date: '' as string
  }),
  actions: {
    async fetchItems(id_project: number | null) {
      this.setDate(this.select_date)

      const service_item = new ItemService()
      this.items = await service_item.getHogehoge(id_project, this.select_date)
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
