import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import { type Item } from '@/types/Item'
import type { SummaryUser } from '@/types/Summary'
import ItemService from '@/services/ItemService'
import UserService from '@/services/UserService'
import SummaryService from '@/services/SummaryService'

const useProgressStore = defineStore('progress', {
  state: () => ({
    users: [] as Array<User>,
    rid_users: 0 as number,
    summaries_user: new Map<number, Array<SummaryUser>>(),
    items: [] as Array<Item>
  }),
  actions: {
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

    async fetchItems(id_project: number, rid_users: number) {
      const service_item = new ItemService()
      this.items = await service_item.getItemsSummaryUser(id_project, rid_users)
    },
    setTarget(rid_users: number) {
      this.rid_users = rid_users
    }
  }
})

export default useProgressStore
