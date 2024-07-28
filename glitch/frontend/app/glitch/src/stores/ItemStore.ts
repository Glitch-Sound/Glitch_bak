import { defineStore } from 'pinia'

import type { Item } from '@/types/Item'
import ItemService from '@/services/ItemService'

const userItemStore = defineStore('item', {
  state: () => ({
    items: [] as Array<Item>
  }),
  actions: {
    async fetchItems(rid_items: number) {
      try {
        const service_item = new ItemService()
        this.items = await service_item.getItems(rid_items)
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
})

export default userItemStore
