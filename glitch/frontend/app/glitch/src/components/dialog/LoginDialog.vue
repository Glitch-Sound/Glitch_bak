<script setup lang="ts">
import { defineProps } from 'vue'

import type { Login } from '@/types/User'
import { useDialog } from '@/components/dialog/BaseDialog'
import { type EmitDialog } from '@/components/common/events'

const props = defineProps<{
  showDialog: boolean
  formData: Login
}>()

const emit = defineEmits<EmitDialog>()
const { dialog, valid, formData, formRef, rules, submitData } = useDialog(props, emit)
</script>

<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Login</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <v-text-field v-model="formData.user" :rules="[rules.required]" label="User" required />

          <v-text-field
            v-model="formData.password"
            :rules="[rules.required]"
            label="Password"
            type="password"
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

<style scoped></style>
