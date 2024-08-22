import { defineStore } from 'pinia'

import { ItemType, ExtractType, type Item } from '@/types/Item'
import ItemService from '@/services/ItemService'
import useUserStore from '@/stores/UserStore'
import useProjectStore from '@/stores/ProjectStore'

const useItemStore = defineStore('item', {
  state: () => ({
    items: [] as Array<Item>,
    type_Extract: ExtractType.ALL as ExtractType,
    type_enabled: ItemType.BUG as ItemType
  }),
  actions: {
    async fetchItems() {
      try {
        const service_item = new ItemService()
        const store_user = useUserStore()
        const store_project = useProjectStore()

        switch (this.type_Extract) {
          case ExtractType.ALL:
          case ExtractType.INCOMPLETE:
          case ExtractType.HIGH_RISK:
          case ExtractType.ALERT:
            this.items = await service_item.getItems(
              store_project.selected_id_project,
              this.type_Extract
            )
            break
          case ExtractType.ASSIGNMENT:
            this.items = await service_item.getItemsByUser(
              store_project.selected_id_project,
              store_user.login_user?.rid
            )
            break
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setExtractType(type: ExtractType) {
      this.type_Extract = type
    },
    setEnabledType(type: ItemType) {
      this.type_enabled = type
    }
  }
})

export default useItemStore
