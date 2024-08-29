<script setup lang="ts">
import { defineProps } from 'vue'

import type { FeatureCreate } from '@/types/Item'
import type { User } from '@/types/User'
import type { EmitDialog } from '@/components/common/events'
import { useDialog } from '@/components/dialog/BaseDialog'
import UserSelect from '@/components/common/UserSelect.vue'

const props = defineProps<{
  showDialog: boolean
  formData: FeatureCreate
}>()

const emit = defineEmits<EmitDialog>()
const { dialog, valid, formData, formRef, rules, submitData } = useDialog(props, emit)

const handleUserSelected = (user: User) => {
  formData.value.rid_users = user.rid
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Add Feature</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" v-model="valid" lazy-validation>
          <UserSelect @itemSelected="handleUserSelected" />

          <v-text-field v-model="formData.title" :rules="[rules.required]" label="Title" required />

          <v-textarea v-model="formData.detail" :rules="[rules.required]" label="Detail" required />
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
