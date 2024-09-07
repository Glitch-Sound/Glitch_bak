import { ref, watch } from 'vue'

export const useDialog = (props: any, emits: any) => {
  const dialog = ref(props.dialog_show)
  const valid = ref(false)
  const data_form = ref({ ...props.data_form })
  const ref_form = ref()

  const rules = {
    required: (value: string) => !!value || 'Required field'
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
