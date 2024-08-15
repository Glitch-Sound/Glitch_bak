<script setup lang="ts">
import { defineProps } from 'vue'

import { TaskType } from '@/types/Item'

const props = defineProps<{
  risk: number
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
}>()
</script>

<template>
  <div class="align-baseline" v-if="props.task_type == TaskType.WORKLOAD">
    {{ props.task_workload }}
  </div>

  <div class="align-baseline" v-if="props.task_type != TaskType.WORKLOAD">
    {{ props.task_number_completed }} / {{ props.task_number_total }}
  </div>
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
