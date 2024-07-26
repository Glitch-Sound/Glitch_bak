export enum TaskType {
  WORKLOAD = 1,
  NUMBER
}

export interface Item {
  rid: number
  type: number
  state: number
  title: string
  detail: string
  result: string
  datetime_entry: string
  datetime_update: string
  user_name: string
  project_datetime_start: string
  project_datetime_end: string
  event_datetime_end: string
  story_datetime_start: string
  story_datetime_end: string
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
}

export interface ProjectCreate {
  rid_user: number
  title: string
  detail: string
  datetime_start: string
  datetime_end: string
}

// // 文字列から Date へ変換
// const dateString = '2024-07-26T12:34:56Z'
// const dateObject = new Date(dateString)

// // Date から文字列へ変換
// const formattedDateString = dateObject.toISOString()
