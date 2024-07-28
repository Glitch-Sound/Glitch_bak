<script setup lang="ts">
import { defineProps } from 'vue'

import type { UserCreate } from '@/types/User'
import { useDialog, EVENT_TYPES } from '@/components/dialog/BaseDialog'

const props = defineProps({
  showDialog: Boolean,
  formData: {
    type: Object as UserCreate
  }
})

const emits = defineEmits([EVENT_TYPES.UPDATE_SHOW_DIALOG, EVENT_TYPES.SUBMIT])

const { dialog, valid, formData, formRef, rules, submitData } = useDialog(props, emits)
</script>

<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add User</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <v-text-field
            v-model="formData.user"
            :rules="[rules.required]"
            label="User"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.password"
            :rules="[rules.required]"
            label="Password"
            type="password"
            required
          ></v-text-field>

          <v-text-field
            v-model="formData.name"
            :rules="[rules.required]"
            label="Name"
            required
          ></v-text-field>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="dialog = false">Cancel</v-btn>
        <v-btn text @click="submitData">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
