<script setup lang="ts">
import { defineProps } from 'vue'

import type { UserUpdate } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import DeleteButton from '@/components/common/DeleteButton.vue'

import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
  data_form: UserUpdate
}>()

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData, deleteData } = useDialog(props, emit)
</script>

<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Update User</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="data_form.user"
            :rules="[rules.required, rules.alphanumeric]"
            label="User"
            required
          />

          <v-text-field
            v-model="data_form.password"
            :rules="[rules.required, rules.alphanumeric]"
            label="Password"
            type="password"
            required
          />

          <v-text-field
            v-model="data_form.name"
            :rules="[rules.required, rules.alphanumeric]"
            label="Name"
            required
          />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <DeleteButton @delete="deleteData" />
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn :disabled="!valid" @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
