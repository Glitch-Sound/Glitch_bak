<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemType, ItemState, TaskType, type TaskUpdate } from '@/types/Item'
import UpdateTaskDialog from '@/components/dialog/UpdateTaskDialog.vue'

import MarkedText from '@/components/common/MarkedText.vue'

const props = defineProps<{
  expand: boolean
  rid: number
  type: ItemType
  state: ItemState
  risk: number
  risk_factors: number
  title: string
  detail: string
  result: string
  datetime_entry: string
  datetime_update: string
  rid_users: number
  name: string
  rid_users_review: number | null
  name_review: string | null
  task_priority: number
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
}>()

const dialog = ref(false)

const dialogFormData = ref<TaskUpdate>({
  rid: 0,
  state: 0,
  rid_user: 0,
  rid_users_review: null,
  title: '',
  detail: '',
  result: '',
  type: 0,
  workload: 0,
  number_completed: 0,
  number_total: 0
})

const openDialog = () => {
  dialogFormData.value = {
    rid: props.rid,
    state: props.state,
    rid_user: props.rid_users,
    rid_users_review: props.rid_users_review,
    title: props.title,
    detail: props.detail,
    result: props.result,
    type: props.task_type,
    workload: props.task_workload,
    number_completed: props.task_number_completed,
    number_total: props.task_number_total
  }
  dialog.value = true
}

const handleSubmit = async (data: TaskUpdate) => {
  try {
    console.log(data)
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <v-expand-transition class="panel-detail-expand">
    <div v-show="props.expand">
      <v-row class="panel-detail-expand-row">
        <v-col cols="auto">
          <span class="detail-title">Detail :</span>
        </v-col>

        <v-col>
          <MarkedText :src="props.detail" />
        </v-col>

        <v-col cols="auto">
          <span class="detail-title">Result :</span>
        </v-col>

        <v-col>
          <MarkedText :src="props.result" />
        </v-col>

        <v-col cols="auto">
          <v-btn size="small" prepend-icon="mdi-pencil" variant="outlined" @click="openDialog()">
            UPDATE
          </v-btn>
        </v-col>
      </v-row>
    </div>
  </v-expand-transition>

  <UpdateTaskDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
