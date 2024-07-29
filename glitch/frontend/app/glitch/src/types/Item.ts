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
  IDLE = 0,
  WAIT,
  RUN,
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
  project_datetime_start: string
  project_datetime_end: string
  project_workload: number
  project_number_completed: number
  project_number_total: number
  event_datetime_end: string
  event_workload: number
  event_number_completed: number
  event_number_total: number
  feature_workload: number
  feature_number_completed: number
  feature_number_total: number
  story_datetime_start: string
  story_datetime_end: string
  story_workload: number
  story_number_completed: number
  story_number_total: number
  task_priority: number
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
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
  project_workload: number
  project_number_completed: number
  project_number_total: number
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
