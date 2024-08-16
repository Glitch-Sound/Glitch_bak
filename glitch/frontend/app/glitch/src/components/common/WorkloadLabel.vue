<script setup lang="ts">
import { defineProps } from 'vue'

import { WorkloadType } from '@/types/Item'

const props = defineProps<{
  risk: number
  workload: WorkloadType
}>()
</script>

<template>
  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_AN_HOUR"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-hexagon-outline</v-icon>
    </p>
    <p class="workload">1 pt</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_HALF_A_DAY"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-hexagon-multiple-outline</v-icon>
    </p>
    <p class="workload">3 pt</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_A_DAY"
  >
    <p class="icon">
      <v-icon size="x-small" icon="$vuetify">mdi-card</v-icon>
    </p>
    <p class="workload">7 pt</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_2_DAYS"
  >
    <p class="icon">
      <v-icon size="small" icon="$vuetify">mdi-view-stream</v-icon>
    </p>
    <p class="workload">14 pt</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_3_DAYS"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-view-sequential</v-icon>
    </p>
    <p class="workload">21 pt</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_A_WEEK"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-view-gallery</v-icon>
    </p>
    <p class="workload">35 pt</p>
  </div>
</template>

<style scoped>
.icon {
  width: 40px;
  align-items: center;
}

.workload {
  width: 50px;
  text-align: right;
}
</style>
