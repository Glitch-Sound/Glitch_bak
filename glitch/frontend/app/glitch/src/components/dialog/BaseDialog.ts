import { ref, watch } from 'vue'

export const EVENT_TYPES = {
  UPDATE_SHOW_DIALOG: 'update:showDialog',
  SUBMIT: 'submit'
} as const

export const useDialog = (props: any, emits: any) => {
  const dialog = ref(props.showDialog)
  const valid = ref(false)
  const formData = ref({ ...props.formData })
  const formRef = ref()

  const rules = {
    required: (value: string) => !!value || 'Required field'
  }

  const submitData = () => {
    if (formRef.value?.validate()) {
      emits(EVENT_TYPES.SUBMIT, formData.value)
      dialog.value = false
    }
  }

  watch(
    () => props.showDialog,
    (newValue) => {
      dialog.value = newValue
    }
  )

  watch(dialog, (newValue) => {
    emits(EVENT_TYPES.UPDATE_SHOW_DIALOG, newValue)
  })

  watch(
    () => props.formData,
    (newData) => {
      formData.value = { ...newData }
    },
    { immediate: true, deep: true }
  )

  return {
    dialog,
    valid,
    formData,
    formRef,
    rules,
    submitData
  }
}
