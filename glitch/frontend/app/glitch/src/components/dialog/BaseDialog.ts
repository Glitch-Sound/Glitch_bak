import { ref, watch } from 'vue'

import { ItemType } from '@/types/Item'
import ItemService from '@/services/ItemService'

export const useDialog = (props: any, emits: any) => {
  const dialog = ref(props.dialog_show)
  const valid = ref(false)
  const data_form = ref({ ...props.data_form })
  const ref_form = ref()

  const rules = {
    required: (value: string) => !!value || 'Required field',
    alphanumeric: (value: string) =>
      /^[a-zA-Z0-9]+$/.test(value) || 'Please use alphanumeric characters only',
    numeric: (value: string) => /^[0-9]+$/.test(value) || 'Please use numbers only'
  }

  const submitData = () => {
    if (ref_form.value?.validate()) {
      emits('submit', data_form.value)
      dialog.value = false
    }
  }

  const deleteData = () => {
    emits('delete')
    dialog.value = false
  }

  watch(
    () => props.dialog_show,
    (newValue) => {
      dialog.value = newValue
    }
  )

  watch(dialog, (newValue) => {
    emits('update:showDialog', newValue)
  })

  watch(
    () => props.data_form,
    (newData) => {
      data_form.value = { ...newData }
    },
    { immediate: true, deep: true }
  )

  return {
    dialog,
    valid,
    data_form,
    ref_form,
    rules,
    submitData,
    deleteData
  }
}

export const getDateRange = async (type: ItemType, rid_parent: number) => {
  if (rid_parent == undefined) {
    return null
  }

  const service_item = new ItemService()
  const parents = await service_item.getItemsParent(rid_parent)
  if (parents.length == 0) {
    return null
  }

  let result: [string, string] = ['', '']
  switch (type) {
    case ItemType.EVENT:
      result = [parents[0].project_datetime_start, parents[0].project_datetime_end]
      break
    case ItemType.STORY:
      result = [parents[0].project_datetime_start, parents[1].event_datetime_end]
      break
  }
  return result
}
