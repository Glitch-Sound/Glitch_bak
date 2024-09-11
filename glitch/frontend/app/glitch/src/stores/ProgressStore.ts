import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import type { Item, ItemHierarchy } from '@/types/Item'
import type { SummaryUser } from '@/types/Summary'
import ItemService from '@/services/ItemService'
import UserService from '@/services/UserService'
import SummaryService from '@/services/SummaryService'
import useItemStore from '@/stores/ItemStore'

const useProgressStore = defineStore('progress', {
  state: () => ({
    items: [] as Array<Item>,
    hierarchy: null as ItemHierarchy | null,
    users: [] as Array<User>,
    rid_users: 0 as number,
    summaries_user: new Map<number, Array<SummaryUser>>()
  }),
  actions: {
    async fetchItems(id_project: number, rid_users: number) {
      const store_item = useItemStore()
      store_item.updated()

      const service_item = new ItemService()
      this.items = await service_item.getItemsSummaryUser(id_project, rid_users)
    },
    async fetchHierarchy(id_project: number | null) {
      try {
        const service_item = new ItemService()
        this.hierarchy = await service_item.getHierarchy(id_project)
      } catch (error) {
        console.error('Error fetching hierarchy:', error)
      }
    },
    async fetchUsers(id_project: number) {
      try {
        const service_user = new UserService()
        this.users = await service_user.getUsersProject(id_project)
      } catch (error) {
        console.error('Error:', error)
      }
    },
    async fetchSummariesUser(id_project: number, rid_users: number) {
      try {
        const service_summary = new SummaryService()
        const summaries = await service_summary.getSummariesUser(id_project, rid_users)

        if (summaries) {
          this.summaries_user.set(rid_users, summaries)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    setTarget(rid_users: number) {
      this.rid_users = rid_users
    }
  }
})

export default useProgressStore
