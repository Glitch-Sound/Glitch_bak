import http from '@/services/ApiClient'

import type { SummaryItem, SummaryUser, Ancestor } from '@/types/Summary'

class SummaryService {
  public async getSummariesItem(rid_items: number): Promise<SummaryItem[]> {
    try {
      const response = await http.get<SummaryItem[]>(`/api/summaries/item/${rid_items}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getSummariesUser(id_project: number, rid_users: number): Promise<SummaryUser[]> {
    try {
      const response = await http.get<SummaryUser[]>(
        `/api/summaries/user/${id_project}/${rid_users}`
      )
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }

  public async getAncestorsItem(rid_items: number): Promise<Ancestor[]> {
    try {
      const response = await http.get<Ancestor[]>(`/api/ancestors/item/${rid_items}`)
      return response.data
    } catch (error) {
      throw new Error('error: ${error}')
    }
  }
}

export default SummaryService
