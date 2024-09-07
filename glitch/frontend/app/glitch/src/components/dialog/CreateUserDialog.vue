<script setup lang="ts">
import { defineProps } from 'vue'

import type { UserCreate } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
  data_form: UserCreate
  is_startup: boolean
}>()

const emit = defineEmits<EmitDialog>()
const { dialog, valid, data_form, ref_form, rules, submitData } = useDialog(props, emit)
</script>

<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title v-if="props.is_startup == true">
        <span class="text-h5">Add Administrator</span>
      </v-card-title>
      <v-card-title v-else>
        <span class="text-h5">Add User</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="ref_form" v-model="valid" lazy-validation>
          <v-text-field v-model="data_form.user" :rules="[rules.required]" label="User" required />

          <v-text-field
            v-model="data_form.password"
            :rules="[rules.required]"
            label="Password"
            type="password"
            required
          />

          <v-text-field v-model="data_form.name" :rules="[rules.required]" label="Name" required />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn @click="dialog = false" v-if="props.is_startup == false">Cancel</v-btn>
        <v-btn @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
