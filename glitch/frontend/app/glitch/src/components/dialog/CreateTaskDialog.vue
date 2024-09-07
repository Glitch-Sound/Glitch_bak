<script setup lang="ts">
import { defineProps, onBeforeUpdate } from 'vue'

import { TaskType, type TaskCreate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import WorkloadSelect from '@/components/common/WorkloadSelect.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
  data_form: TaskCreate
}>()

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData } = useDialog(props, emit)

onBeforeUpdate(() => {
  data_form.value.type = TaskType.WORKLOAD
})

const handleUserSelected = (user: User) => {
  data_form.value.rid_users = user.rid
}

const handleWorkloadSelect = (workload: number) => {
  data_form.value.workload = workload
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add Task</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <UserSelect @itemSelected="handleUserSelected" />

          <v-text-field
            v-model="data_form.title"
            :rules="[rules.required]"
            label="Title"
            required
          />

          <v-textarea
            v-model="data_form.detail"
            :rules="[rules.required]"
            label="Detail"
            required
          />

          <div class="mb-4 text-center">
            <v-btn-toggle v-model="data_form.type" mandatory>
              <v-btn :value="TaskType.WORKLOAD">Workload</v-btn>
              <v-btn :value="TaskType.NUMBER">Number</v-btn>
            </v-btn-toggle>
          </div>

          <WorkloadSelect
            v-if="data_form.type == TaskType.WORKLOAD"
            :workload="null"
            @itemSelected="handleWorkloadSelect"
          />

          <v-text-field
            v-if="data_form.type == TaskType.NUMBER"
            v-model="data_form.number_completed"
            :rules="[rules.required]"
            label="Number completed"
          />

          <v-text-field
            v-if="data_form.type == TaskType.NUMBER"
            v-model="data_form.number_total"
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
