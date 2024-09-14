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

export enum ExtractType {
  NONE = 0,
  ALL,
  INCOMPLETE,
  HIGH_RISK,
  ALERT,
  ASSIGNMENT,
  RELATION,
  SEARCH
}

export interface Item {
  rid: number
  id_project: number
  type: ItemType
  state: ItemState
  risk: number
  risk_factors: number
  priority: number
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
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
  bug_workload: number
}

export interface Project {
  rid: number
  id_project: number
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
}

export interface ProjectCreate {
  rid_users: number
  title: string
  detail: string
  datetime_start: string
  datetime_end: string
}

export interface ProjectUpdate {
  rid: number
  state: number
  rid_users: number
  rid_users_review: number | null
  title: string
  detail: string
  result: string
  datetime_start: string
  datetime_end: string
}

export interface EventCreate {
  id_project: number
  rid_items: number
  rid_users: number
  title: string
  detail: string
  datetime_end: string
}

export interface EventUpdate {
  rid: number
  state: number
  rid_users: number
  rid_users_review: number | null
  title: string
  detail: string
  result: string
  datetime_end: string
}

export interface FeatureCreate {
  id_project: number
  rid_items: number
  rid_users: number
  title: string
  detail: string
}

export interface FeatureUpdate {
  rid: number
  state: number
  rid_users: number
  rid_users_review: number | null
  title: string
  detail: string
  result: string
}

export interface StoryCreate {
  id_project: number
  rid_items: number
  rid_users: number
  title: string
  detail: string
  datetime_start: string
  datetime_end: string
}

export interface StoryUpdate {
  rid: number
  state: number
  rid_users: number
  rid_users_review: number | null
  title: string
  detail: string
  result: string
  datetime_start: string
  datetime_end: string
}

export interface TaskCreate {
  id_project: number
  rid_items: number
  rid_users: number
  title: string
  detail: string
  type: number
  workload: number
  number_completed: number
  number_total: number
}

export interface TaskUpdate {
  rid: number
  state: number
  rid_users: number
  rid_users_review: number | null
  title: string
  detail: string
  result: string
  type: number
  workload: number
  number_completed: number
  number_total: number
}

export interface TaskPriorityUpdate {
  rid: number
  priority: number
}

export interface BugCreate {
  id_project: number
  rid_items: number
  rid_users: number
  title: string
  detail: string
  workload: number
}

export interface BugUpdate {
  rid: number
  state: number
  rid_users: number
  rid_users_review: number | null
  title: string
  detail: string
  result: string
  workload: number
}

export interface BugPriorityUpdate {
  rid: number
  priority: number
}

export interface ItemHierarchy {
  rid: number
  rid_users: number
  name: string
  title: string
  workload_task?: number
  workload_bug?: number
  children?: ItemHierarchy[]
}

export interface SummaryProject {
  rid: number
  type: number
  state: number
  title: string
  datetime_start: string
  datetime_end: string
}

export interface ItemFrequency {
  datetime_entry: string
  task_count: number
  task_count_idle: number
  task_count_run: number
  task_count_alert: number
  task_count_review: number
  task_count_complete: number
  bug_count: number
  bug_count_idle: number
  bug_count_run: number
  bug_count_alert: number
  bug_count_review: number
  bug_count_complete: number
}
