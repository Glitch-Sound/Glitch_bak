<script setup lang="ts">
import { ref, defineProps, watch } from 'vue'

import { ItemType, ItemState, type EventUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import UserReviewSelect from '@/components/common/UserReviewSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'
import DeleteButton from '@/components/common/DeleteButton.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  showDialog: boolean
  formData: EventUpdate
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

const handleUserSelected = (user: User) => {
  formData.value.rid_users = user.rid
}

const handleUserReviewSelected = (user: User) => {
  formData.value.rid_users_review = user.rid
}

const handleStateSelected = (state: ItemState) => {
  formData.value.state = state
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Event</span>
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

          <v-text-field
            v-model="formData.datetime_end"
            :rules="[rules.required]"
            label="End"
            type="date"
            required
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
