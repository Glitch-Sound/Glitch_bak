<script setup lang="ts">
import { ref, watch, defineProps, defineEmits } from 'vue'

const props = defineProps({
  showDialog: Boolean,
  formData: {
    type: Object as () => {
      user: string
      password: string
      name: string
      is_admin: boolean
    },
    default: () => ({ user: '', password: '', name: '', is_admin: false })
  }
})

const emits = defineEmits(['update:showDialog', 'submit'])

const localDialog = ref(props.showDialog)
const valid = ref(false)
const formData = ref({ ...props.formData })
const formRef = ref()

const rules = {
  required: (value: string) => !!value || 'Required field'
}

const submitData = () => {
  if (formRef.value.validate()) {
    emits('submit', formData.value)
    localDialog.value = false
  }
}

watch(
  () => props.showDialog,
  (newValue) => {
    localDialog.value = newValue
  }
)

watch(localDialog, (newValue) => {
  emits('update:showDialog', newValue)
})

watch(
  () => props.formData,
  (newData) => {
    formData.value = { ...newData }
  },
  { immediate: true }
)
</script>

<template>
  <v-dialog v-model="localDialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Submit Data</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <v-text-field
            v-model="formData.user"
            :rules="[rules.required]"
            label="User"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.password"
            :rules="[rules.required]"
            label="Password"
            type="password"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.name"
            :rules="[rules.required]"
            label="Name"
            required
          ></v-text-field>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="localDialog = false">Cancel</v-btn>
        <v-btn text @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
