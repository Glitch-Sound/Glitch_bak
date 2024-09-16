import { ref, watch } from 'vue'

import { ItemType } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'

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
    (value_new) => {
      dialog.value = value_new
    }
  )

  watch(dialog, (value_new) => {
    emits('update:showDialog', value_new)
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

  const store_item = useItemStore()
  const ancestors = await store_item.getItemsAncestor(rid_parent)
  if (ancestors.length == 0) {
    return null
  }

  let result: [string, string] = ['', '']
  switch (type) {
    case ItemType.EVENT:
      result = [ancestors[0].project_datetime_start, ancestors[0].project_datetime_end]
      break
    case ItemType.STORY:
      result = [ancestors[0].project_datetime_start, ancestors[1].event_datetime_end]
      break
  }
  return result
}
