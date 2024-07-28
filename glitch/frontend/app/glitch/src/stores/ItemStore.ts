import { defineStore } from 'pinia'
import ItemService from '@/services/ItemService'
import type { Item } from '@/types/Item'

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
