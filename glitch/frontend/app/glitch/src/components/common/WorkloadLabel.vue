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
    <p class="workload">1 hour</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_HALF_A_DAY"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-hexagon-multiple-outline</v-icon>
    </p>
    <p class="workload">Half day</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_A_DAY"
  >
    <p class="icon">
      <v-icon size="x-small" icon="$vuetify">mdi-card</v-icon>
    </p>
    <p class="workload">1 day</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_2_DAYS"
  >
    <p class="icon">
      <v-icon size="small" icon="$vuetify">mdi-view-stream</v-icon>
    </p>
    <p class="workload">2 day</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_3_DAYS"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-view-sequential</v-icon>
    </p>
    <p class="workload">3 day</p>
  </div>

  <div
    class="d-flex flex-row align-baseline justify-center"
    v-if="props.workload == WorkloadType.WITHIN_A_WEEK"
  >
    <p class="icon">
      <v-icon icon="$vuetify">mdi-view-gallery</v-icon>
    </p>
    <p class="workload">1 week</p>
  </div>
</template>

<style scoped>
.icon {
  width: 50px;
  margin-left: 15px;
  align-items: center;
}

.workload {
  width: 70px;
  margin-left: 5px;
  text-align: left;
}
</style>
