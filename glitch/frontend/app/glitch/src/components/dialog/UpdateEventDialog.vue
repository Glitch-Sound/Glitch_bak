<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType, ItemState, type EventUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog, EVENT_TYPES } from '@/components/dialog/BaseDialog'
import AccountSelect from '@/components/common/AccountSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'

const props = defineProps<{
  showDialog: boolean
  formData: EventUpdate
}>()

const handleItemSelected = (item: User) => {
  formData.value.rid_user = item.rid
}

const handleStateSelected = (state: ItemState) => {
  formData.value.state = state
}

const emits = defineEmits([EVENT_TYPES.UPDATE_SHOW_DIALOG, EVENT_TYPES.SUBMIT])
const { dialog, valid, formData, formRef, rules, submitData } = useDialog(props, emits)
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Event</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <AccountSelect v-model="formData.rid_user" @itemSelected="handleItemSelected" />

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
