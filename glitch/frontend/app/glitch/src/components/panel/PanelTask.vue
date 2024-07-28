<script setup lang="ts">
import { defineProps } from 'vue'
import PanelBase from '@/components/panel/PanelBase.vue'
import { TaskType } from '@/types/Item'

const props = defineProps({
  rid: Number,
  state: Number,
  risk: Number,
  title: String,
  detail: String,
  result: String,
  datetime_entry: String,
  datetime_update: String,
  name: String,
  task_type: TaskType,
  task_workload: Number,
  task_number_completed: Number,
  task_number_total: Number
})
</script>

<template>
  <PanelBase :baseDiv="'pl-15'">
    <template #title>{{ props.title }}</template>
  </PanelBase>
</template>

<style scoped></style>
