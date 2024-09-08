import { defineStore } from 'pinia'

import type { User } from '@/types/User'
import type { SummaryUser } from '@/types/Summary'
import UserService from '@/services/UserService'
import SummaryService from '@/services/SummaryService'

const useProgressStore = defineStore('progress', {
  state: () => ({
    users: [] as Array<User>,
    rid_users: 0 as number,
    summaries_user: new Map<number, Array<SummaryUser>>()
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
    setTarget(rid_users: number) {
      this.rid_users = rid_users
    }
  }
})

export default useProgressStore
