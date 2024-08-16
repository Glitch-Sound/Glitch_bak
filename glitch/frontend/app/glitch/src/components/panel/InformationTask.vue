<script setup lang="ts">
import { defineProps } from 'vue'

import { TaskType, WorkloadType } from '@/types/Item'
import WorkloadLabel from '@/components/common/WorkloadLabel.vue'

const props = defineProps<{
  risk: number
  task_type: TaskType
  task_workload: WorkloadType
  task_number_completed: number
  task_number_total: number
}>()
</script>

<template>
  <div class="align-baseline" v-if="props.task_type == TaskType.WORKLOAD">
    <WorkloadLabel :risk="props.risk" :workload="props.task_workload" />
  </div>

  <div class="align-baseline" v-if="props.task_type != TaskType.WORKLOAD">
    {{ props.task_number_completed }} / {{ props.task_number_total }}
  </div>
</template>

<style scoped></style>
