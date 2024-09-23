<script setup lang="ts">
import { ref, defineProps, watch } from 'vue'

import { ItemType, ItemState, type StoryUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog, getDateRange } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import UserReviewSelect from '@/components/common/UserReviewSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'
import DeleteButton from '@/components/common/DeleteButton.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
  data_form: StoryUpdate
  rid_parent: number
}>()

const is_review = ref(false)
const date_min = ref('')
const date_max = ref('')

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData, deleteData } = useDialog(props, emit)

watch(
  () => props.dialog_show,
  async (value_new) => {
    if (value_new) {
      const range = await getDateRange(ItemType.STORY, props.rid_parent)
      if (range) {
        ;[date_min.value, date_max.value] = range
      }
    }
  }
)

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

const handleUserSelected = (user: User) => {
  data_form.value.rid_users = user.rid
}

const handleUserReviewSelected = (user: User) => {
  data_form.value.rid_users_review = user.rid
}

const handleStateSelected = (state: ItemState) => {
  data_form.value.state = state
}
</script>

<template>
  <v-dialog v-model="dialog" class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Story</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <UserSelect v-model="data_form.rid_users" @itemSelected="handleUserSelected" />

          <UserReviewSelect
            v-if="is_review"
            :rules="[rules.required]"
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

          <v-textarea v-model="data_form.detail" label="Detail" />
          <v-textarea v-model="data_form.result" label="Result" />

          <v-text-field
            v-model="data_form.datetime_start"
            :rules="[rules.required]"
            label="Start"
            type="date"
            required
            :min="date_min"
            :max="date_max"
          />

          <v-text-field
            v-model="data_form.datetime_end"
            :rules="[rules.required]"
            label="End"
            type="date"
            required
            :min="date_min"
            :max="date_max"
          />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <DeleteButton @delete="deleteData" />
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn color="primary" :disabled="!valid" @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
@import '@/components/dialog/dialog.css';
</style>
