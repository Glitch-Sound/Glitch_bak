<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType, ItemState, type EventUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'
import DeleteButton from '@/components/common/DeleteButton.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  showDialog: boolean
  formData: EventUpdate
}>()

const handleUserSelected = (user: User) => {
  formData.value.rid_user = user.rid
}

const handleStateSelected = (state: ItemState) => {
  formData.value.state = state
}

const emit = defineEmits<EmitDialog>()
const { dialog, valid, formData, formRef, rules, submitData, deleteData } = useDialog(props, emit)
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Event</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <UserSelect v-model="formData.rid_user" @itemSelected="handleUserSelected" />

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
