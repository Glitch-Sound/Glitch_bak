<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType, ItemState, type ProjectUpdate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import StateSelect from '@/components/common/StateSelect.vue'
import DeleteButton from '@/components/common/DeleteButton.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
  data_form: ProjectUpdate
}>()

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData, deleteData } = useDialog(props, emit)

const handleUserSelected = (user: User) => {
  data_form.value.rid_users = user.rid
}

const handleStateSelected = (state: ItemState) => {
  data_form.value.state = state
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update Project</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <UserSelect v-model="data_form.rid_users" @itemSelected="handleUserSelected" />

          <StateSelect
            :type="ItemType.PROJECT"
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

          <v-text-field
            v-model="data_form.datetime_start"
            :rules="[rules.required]"
            label="Start"
            type="date"
            required
          />

          <v-text-field
            v-model="data_form.datetime_end"
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
