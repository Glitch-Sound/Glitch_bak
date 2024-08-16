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

export const RISK_1 = 0b00000001
export const RISK_2 = 0b00000010
export const RISK_3 = 0b00000100
export const RISK_4 = 0b00001000
export const RISK_5 = 0b00010000
export const RISK_6 = 0b00100000
export const RISK_7 = 0b01000000
export const RISK_8 = 0b10000000

export enum WorkloadType {
  NONE = 0,
  WITHIN_AN_HOUR = 1,
  WITHIN_HALF_A_DAY = 3,
  WITHIN_A_DAY = 7,
  WITHIN_2_DAYS = 14,
  WITHIN_3_DAYS = 21,
  WITHIN_A_WEEK = 35
}

export interface Item {
  rid: number
  type: ItemType
  state: ItemState
  risk: number
  risk_factors: number
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
  bug_priority: number
  bug_workload: number
}

export interface Project {
  rid: number
  state: number
  risk: number
  risk_factors: number
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
