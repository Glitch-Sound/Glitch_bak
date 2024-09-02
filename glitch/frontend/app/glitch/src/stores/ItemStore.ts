import { defineStore } from 'pinia'

import { ItemType, ExtractType, type Item } from '@/types/Item'
import ItemService from '@/services/ItemService'
import useUserStore from '@/stores/UserStore'
import useProjectStore from '@/stores/ProjectStore'

const useItemStore = defineStore('item', {
  state: () => ({
    items: [] as Array<Item>,
    type_extract: ExtractType.INCOMPLETE as ExtractType,
    type_enabled: ItemType.BUG as ItemType,
    rid_item: 0 as number
  }),
  actions: {
    async fetchItems(router: any) {
      try {
        const service_item = new ItemService()
        const store_user = useUserStore()
        const store_project = useProjectStore()

        const path = `/project/${store_project.selected_id_project}`

        switch (this.type_extract) {
          case ExtractType.ALL:
          case ExtractType.INCOMPLETE:
          case ExtractType.HIGH_RISK:
          case ExtractType.ALERT:
            {
              this.items = await service_item.getItems(
                store_project.selected_id_project,
                this.type_extract
              )
              const query = { extruct: this.type_extract }
              router.push({ path, query })
            }
            break
          case ExtractType.ASSIGNMENT:
            {
              this.items = await service_item.getItemsByUser(
                store_project.selected_id_project,
                store_user.login_user?.rid
              )
              const query = { extruct: this.type_extract }
              router.push({ path, query })
            }
            break
          case ExtractType.ITEM:
            break
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setExtractAll() {
      this.type_extract = ExtractType.ALL
    },
    setExtractIncomplete() {
      this.type_extract = ExtractType.INCOMPLETE
    },
    setExtractHighRisk() {
      this.type_extract = ExtractType.HIGH_RISK
    },
    setExtractAlert() {
      this.type_extract = ExtractType.ALERT
    },
    setExtractAssignment() {
      this.type_extract = ExtractType.ASSIGNMENT
    },
    setExtractItem(rid_item: number) {
      this.type_extract = ExtractType.ITEM
      this.rid_item = rid_item
    },
    setEnabledType(type: ItemType) {
      this.type_enabled = type
    }
  }
})

export default useItemStore
