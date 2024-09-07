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
  dialog_show: boolean
  data_form: TaskUpdate
}>()

const is_review = ref(false)

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData, deleteData } = useDialog(props, emit)

watch(
  () => data_form.value.state,
  (state_new) => {
    if (state_new == ItemState.REVIEW) {
      is_review.value = true
    } else {
      is_review.value = false
    }
  }
)

onBeforeUpdate(() => {
  data_form.value.type = TaskType.WORKLOAD
})

const handleUserSelected = (user: User) => {
  data_form.value.rid_users = user.rid
}

const handleUserReviewSelected = (user: User) => {
  data_form.value.rid_users_review = user.rid
}

const handleStateSelected = (state: ItemState) => {
  data_form.value.state = state
}

const handleWorkloadSelect = (workload: number) => {
  data_form.value.workload = workload
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Task</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <UserSelect v-model="data_form.rid_users" @itemSelected="handleUserSelected" />

          <UserReviewSelect
            v-if="is_review"
            v-model="data_form.rid_users_review"
            @itemSelected="handleUserReviewSelected"
          />

          <StateSelect
            :type="ItemType.EVENT"
            :state="data_form.state"
            @itemSelected="handleStateSelected"
          />

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

          <v-textarea
            v-model="data_form.result"
            :rules="[rules.required]"
            label="Result"
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
            :workload="data_form.workload"
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
