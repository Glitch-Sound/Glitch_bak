export enum ItemType {
  NONE = 0,
  PROJECT,
  EVENT,
  FEATURE,
  STORY,
  TASK,
  BUG
}

export enum ItemState {
  NONE = 0,
  IDLE,
  RUN,
  ALERT,
  REVIEW,
  COMPLETE
}

export enum TaskType {
  NONE = 0,
  WORKLOAD,
  NUMBER
}

export interface Item {
  rid: number
  type: ItemType
  state: ItemState
  risk: number
  title: string
  detail: string
  result: string
  datetime_entry: string
  datetime_update: string
  rid_users: number
  name: string
  rid_users_review: number | null
  name_review: string | null
  project_datetime_start: string
  project_datetime_end: string
  event_datetime_end: string
  story_datetime_start: string
  story_datetime_end: string
  task_priority: number
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
  bug_workload: number
}

export interface Project {
  rid: number
  state: number
  risk: number
  title: string
  detail: string
  result: string
  datetime_entry: string
  datetime_update: string
  rid_users: number
  name: string
  project_datetime_start: string
  project_datetime_end: string
  project_task_count_completed: number
  project_task_count_total: number
  project_task_workload_completed: number
  project_task_workload_total: number
  project_task_number_completed: number
  project_task_number_total: number
  project_bug_count_completed: number
  project_bug_count_total: number
  project_bug_workload_completed: number
  project_bug_workload_total: number
}

export interface ProjectCreate {
  rid_user: number
  title: string
  detail: string
  datetime_start: string
  datetime_end: string
}

export interface EventCreate {
  rid_items: number
  rid_user: number
  title: string
  detail: string
  datetime_end: string
}

export interface FeatureCreate {
  rid_items: number
  rid_user: number
  title: string
  detail: string
}

export interface StoryCreate {
  rid_items: number
  rid_user: number
  title: string
  detail: string
  datetime_start: string
  datetime_end: string
}

export interface TaskCreate {
  rid_items: number
  rid_user: number
  title: string
  detail: string
  type: number
  workload: number
  number_completed: number
  number_total: number
}

export interface BugCreate {
  rid_items: number
  rid_user: number
  title: string
  detail: string
  workload: number
}
