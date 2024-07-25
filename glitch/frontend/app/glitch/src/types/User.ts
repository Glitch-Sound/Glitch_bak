export interface User {
  rid: number
  user: string
  name: string
  is_admin: boolean
}

export interface UserCreate {
  user: string
  password: string
  name: string
  is_admin: boolean
}
