<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType, ItemState, type BugUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import type { EmitDialog } from '@/components/common/events'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import WorkloadSelect from '@/components/common/WorkloadSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'
import DeleteButton from '@/components/common/DeleteButton.vue'

const props = defineProps<{
  showDialog: boolean
  formData: BugUpdate
}>()

const handleUserSelected = (user: User) => {
  formData.value.rid_users = user.rid
}

const handleStateSelected = (state: ItemState) => {
  formData.value.state = state
}

const handleWorkloadSelect = (workload: number) => {
  formData.value.workload = workload
}

const emit = defineEmits<EmitDialog>()
const { dialog, valid, formData, formRef, rules, submitData, deleteData } = useDialog(props, emit)
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Bug</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <UserSelect v-model="formData.rid_users" @itemSelected="handleUserSelected" />

          <StateSelect
            :type="ItemType.EVENT"
            :state="formData.state"
            @itemSelected="handleStateSelected"
          />

          <v-text-field v-model="formData.title" :rules="[rules.required]" label="Title" required />

          <v-textarea v-model="formData.detail" :rules="[rules.required]" label="Detail" required />

          <v-textarea v-model="formData.result" :rules="[rules.required]" label="Result" required />

          <WorkloadSelect :workload="formData.workload" @itemSelected="handleWorkloadSelect" />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <DeleteButton @delete="deleteData" />
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
