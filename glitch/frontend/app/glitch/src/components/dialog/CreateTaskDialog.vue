<script setup lang="ts">
import { defineProps, onBeforeUpdate } from 'vue'

import { TaskType, type TaskCreate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import WorkloadSelect from '@/components/common/WorkloadSelect.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  showDialog: boolean
  formData: TaskCreate
}>()

onBeforeUpdate(() => {
  formData.value.type = TaskType.WORKLOAD
})

const handleUserSelected = (user: User) => {
  formData.value.rid_users = user.rid
}

const handleWorkloadSelect = (workload: number) => {
  formData.value.workload = workload
}

const emit = defineEmits<EmitDialog>()
const { dialog, valid, formData, formRef, rules, submitData } = useDialog(props, emit)
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add Task</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <UserSelect @itemSelected="handleUserSelected" />

          <v-text-field v-model="formData.title" :rules="[rules.required]" label="Title" required />

          <v-textarea v-model="formData.detail" :rules="[rules.required]" label="Detail" required />

          <div class="mb-4 text-center">
            <v-btn-toggle v-model="formData.type" mandatory>
              <v-btn :value="TaskType.WORKLOAD">Workload</v-btn>
              <v-btn :value="TaskType.NUMBER">Number</v-btn>
            </v-btn-toggle>
          </div>

          <WorkloadSelect
            v-if="formData.type == TaskType.WORKLOAD"
            :workload="null"
            @itemSelected="handleWorkloadSelect"
          />

          <v-text-field
            v-if="formData.type == TaskType.NUMBER"
            v-model="formData.number_completed"
            :rules="[rules.required]"
            label="Number completed"
          />

          <v-text-field
            v-if="formData.type == TaskType.NUMBER"
            v-model="formData.number_total"
            :rules="[rules.required]"
            label="Number total"
          />
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

<style scoped>
@import '@/components/dialog/dialog.css';
</style>
