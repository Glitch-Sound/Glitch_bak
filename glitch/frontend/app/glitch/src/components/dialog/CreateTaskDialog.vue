<script setup lang="ts">
import { defineProps } from 'vue'

import type { TaskCreate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog, EVENT_TYPES } from '@/components/dialog/BaseDialog'
import AccountSelect from '@/components/common/AccountSelect.vue'

const props = defineProps<{
  showDialog: boolean
  formData: TaskCreate
}>()

const handleItemSelected = (item: User) => {
  formData.value.rid_user = item.rid
}

const emits = defineEmits([EVENT_TYPES.UPDATE_SHOW_DIALOG, EVENT_TYPES.SUBMIT])
const { dialog, valid, formData, formRef, rules, submitData } = useDialog(props, emits)
</script>

<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add Task</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <AccountSelect @itemSelected="handleItemSelected"></AccountSelect>

          <v-text-field
            v-model="formData.title"
            :rules="[rules.required]"
            label="Title"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.detail"
            :rules="[rules.required]"
            label="Detail"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.type"
            :rules="[rules.required]"
            label="Type"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.workload"
            :rules="[rules.required]"
            label="Workload"
          ></v-text-field>

          <v-text-field
            v-model="formData.number_completed"
            :rules="[rules.required]"
            label="Number completed"
          ></v-text-field>

          <v-text-field
            v-model="formData.number_total"
            :rules="[rules.required]"
            label="Number total"
          ></v-text-field>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
