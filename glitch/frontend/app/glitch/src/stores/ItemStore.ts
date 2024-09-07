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
    extract_rid_item: 0 as number,
    extract_search_target: '' as string
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
            {
              this.items = await service_item.getItemsAll(store_project.selected_id_project)

              const query = { extruct: this.type_extract }
              router.push({ path, query })
            }
            break

          case ExtractType.INCOMPLETE:
            {
              this.items = await service_item.getItemsIncomplete(store_project.selected_id_project)

              const query = { extruct: this.type_extract }
              router.push({ path, query })
            }
            break

          case ExtractType.HIGH_RISK:
            {
              this.items = await service_item.getItemsHighRisk(store_project.selected_id_project)

              const query = { extruct: this.type_extract }
              router.push({ path, query })
            }
            break

          case ExtractType.ALERT:
            {
              this.items = await service_item.getItemsAlert(store_project.selected_id_project)

              const query = { extruct: this.type_extract }
              router.push({ path, query })
            }
            break

          case ExtractType.ASSIGNMENT:
            {
              this.items = await service_item.getItemsAssignment(
                store_project.selected_id_project,
                store_user.login_user?.rid
              )

              const query = { extruct: this.type_extract, target: store_user.login_user?.rid }
              router.push({ path, query })
            }
            break

          case ExtractType.RELATION:
            {
              this.items = await service_item.getItemsRelation(
                store_project.selected_id_project,
                this.extract_rid_item
              )

              const query = { extruct: this.type_extract, target: this.extract_rid_item }
              router.push({ path, query })
            }
            break

          case ExtractType.SEARCH:
            {
              this.items = await service_item.getItemsSearch(
                store_project.selected_id_project,
                this.extract_search_target
              )

              const query = { extruct: this.type_extract, target: this.extract_search_target }
              router.push({ path, query })
            }
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
      this.type_extract = ExtractType.RELATION
      this.extract_rid_item = rid_item
    },
    setExtractSearch(target: string) {
      this.type_extract = ExtractType.SEARCH
      this.extract_search_target = target
    },

    setEnabledType(type: ItemType) {
      this.type_enabled = type
    }
  }
})

export default useItemStore
