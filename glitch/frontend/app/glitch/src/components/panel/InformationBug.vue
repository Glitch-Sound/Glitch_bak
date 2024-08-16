<script setup lang="ts">
import { defineProps } from 'vue'

import WorkloadLabel from '@/components/common/WorkloadLabel.vue'

const props = defineProps<{
  risk: number
  bug_workload: number
}>()
</script>

<template>
  <div class="align-baseline">
    <WorkloadLabel :risk="props.risk" :workload="props.bug_workload" />
  </div>
</template>

<style scoped></style>
