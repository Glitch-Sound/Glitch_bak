<script setup lang="ts">
import { ref, defineProps, onBeforeUpdate, watch } from 'vue'

import { TaskType, ItemType, ItemState, type TaskUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import UserReviewSelect from '@/components/common/UserReviewSelect.vue'
import WorkloadSelect from '@/components/common/WorkloadSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'
import DeleteButton from '@/components/common/DeleteButton.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  showDialog: boolean
  formData: TaskUpdate
}>()

const is_review = ref(false)

const emit = defineEmits<EmitDialog>()
const { dialog, valid, formData, formRef, rules, submitData, deleteData } = useDialog(props, emit)

watch(
  () => formData.value.state,
  (state_new) => {
    if (state_new == ItemState.REVIEW) {
      is_review.value = true
    } else {
      is_review.value = false
    }
  }
)

onBeforeUpdate(() => {
  formData.value.type = TaskType.WORKLOAD
})

const handleUserSelected = (user: User) => {
  formData.value.rid_users = user.rid
}

const handleUserReviewSelected = (user: User) => {
  formData.value.rid_users_review = user.rid
}

const handleStateSelected = (state: ItemState) => {
  formData.value.state = state
}

const handleWorkloadSelect = (workload: number) => {
  formData.value.workload = workload
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Task</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <UserSelect v-model="formData.rid_users" @itemSelected="handleUserSelected" />

          <UserReviewSelect
            v-if="is_review"
            v-model="formData.rid_users_review"
            @itemSelected="handleUserReviewSelected"
          />

          <StateSelect
            :type="ItemType.EVENT"
            :state="formData.state"
            @itemSelected="handleStateSelected"
          />

          <v-text-field v-model="formData.title" :rules="[rules.required]" label="Title" required />

          <v-textarea v-model="formData.detail" :rules="[rules.required]" label="Detail" required />

          <v-textarea v-model="formData.result" :rules="[rules.required]" label="Result" required />

          <div class="mb-4 text-center">
            <v-btn-toggle v-model="formData.type" mandatory>
              <v-btn :value="TaskType.WORKLOAD">Workload</v-btn>
              <v-btn :value="TaskType.NUMBER">Number</v-btn>
            </v-btn-toggle>
          </div>

          <WorkloadSelect
            v-if="formData.type == TaskType.WORKLOAD"
            :workload="formData.workload"
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
