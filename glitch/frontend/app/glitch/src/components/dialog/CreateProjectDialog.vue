<script setup lang="ts">
import { defineProps, watch } from 'vue'

import type { ProjectCreate } from '@/types/Item'
import type { User } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
  data_form: ProjectCreate
}>()

watch(
  () => props.dialog_show,
  async (value_new) => {
    if (value_new) {
      data_form.value.title = ''
      data_form.value.detail = ''
    }
  }
)

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData } = useDialog(props, emit)

const handleUserSelected = (user: User) => {
  data_form.value.rid_users = user.rid
}
</script>

<template>
  <v-dialog v-model="dialog" class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add Project</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <UserSelect v-model="data_form.rid_users" @itemSelected="handleUserSelected" />

          <v-text-field
            v-model="data_form.title"
            :rules="[rules.required]"
            label="Title"
            required
          />

          <v-textarea v-model="data_form.detail" label="Detail" />

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
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn :disabled="!valid" @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
@import '@/components/dialog/dialog.css';
</style>
