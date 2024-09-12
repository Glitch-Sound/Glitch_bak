import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import type { Item, ItemHierarchy } from '@/types/Item'
import type { SummaryUser } from '@/types/Summary'
import ItemService from '@/services/ItemService'
import UserService from '@/services/UserService'
import SummaryService from '@/services/SummaryService'
import useItemStore from '@/stores/ItemStore'

const useAnalyzeStore = defineStore('analyze', {
  state: () => ({
    items: [] as Array<Item>,
    select_date: '2024-09-09' as string
  }),
  actions: {
    async fetchItems(id_project: number | null) {
      const service_item = new ItemService()
      this.items = await service_item.getHogehoge(id_project, this.select_date)
      console.log(this.items)
    },
    setDate(select_date: string) {
      this.select_date = select_date
      console.log(this.select_date)
    }
  }
})

export default useAnalyzeStore
