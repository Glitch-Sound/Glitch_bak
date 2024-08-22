import { defineStore } from 'pinia'

import { ItemType, type Item } from '@/types/Item'
import ItemService from '@/services/ItemService'

const userItemStore = defineStore('item', {
  state: () => ({
    items: [] as Array<Item>,
    type_enabled: ItemType.BUG as ItemType
  }),
  actions: {
    async fetchItems(rid_items: number) {
      try {
        const service_item = new ItemService()
        this.items = await service_item.getItems(rid_items)
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setEnabledType(type: ItemType) {
      this.type_enabled = type
    }
  }
})

export default userItemStore
