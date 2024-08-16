export type EmitSubmit = {
  (e: 'submit'): void
}

export type EmitItemSelected = {
  (e: 'itemSelected', selectedItem: any): void
}

export type EmitDialog = {
  (e: 'update:showDialog', showDialog: boolean): void
  (e: 'submit', data: any): void
}
