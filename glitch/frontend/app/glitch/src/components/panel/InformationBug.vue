<script setup lang="ts">
import { defineProps } from 'vue'

import { WorkloadType } from '@/types/Item'

const props = defineProps<{
  risk: number
  bug_workload: number
}>()
</script>

<template>
  <div class="align-baseline">
    <!-- <div class="align-baseline" v-if="props.bug_workload == WorkloadType.WITHIN_AN_HOUR">
      <v-icon icon="$vuetify">mdi-minus</v-icon>
      1 pt
    </div>

    <div class="align-baseline" v-if="props.bug_workload == WorkloadType.WITHIN_HALF_A_DAY">
      <v-icon icon="$vuetify">mdi-menu</v-icon>
      3 pt
    </div>

    <div class="align-baseline" v-if="props.bug_workload == WorkloadType.WITHIN_A_DAY">
      <v-icon icon="$vuetify">mdi-tally-mark-1</v-icon>
      7 pt
    </div>

    <div class="align-baseline" v-if="props.bug_workload == WorkloadType.WITHIN_2_DAYS">
      <v-icon icon="$vuetify">mdi-tally-mark-2</v-icon>
      14 pt
    </div>

    <div class="align-baseline" v-if="props.bug_workload == WorkloadType.WITHIN_3_DAYS">
      <v-icon icon="$vuetify">mdi-tally-mark-3</v-icon>
      21 pt
    </div>

    <div class="align-baseline" v-if="props.bug_workload == WorkloadType.WITHIN_A_WEEK">
      <v-icon icon="$vuetify">mdi-tally-mark-5</v-icon>
      35 pt
    </div> -->

    {{ props.bug_workload }}

    <!-- <v-icon size="x-small" icon="$vuetify">mdi-dots-hexagon</v-icon>
    <v-icon size="x-small" icon="$vuetify">mdi-dots-hexagon</v-icon>
    <v-icon size="x-small" icon="$vuetify">mdi-dots-hexagon</v-icon>
    <v-icon size="x-small" icon="$vuetify">mdi-dots-hexagon</v-icon>
    <v-icon size="x-small" icon="$vuetify">mdi-dots-hexagon</v-icon> -->
  </div>
</template>

<style scoped>
@import '@/components/panel/panel.css';

.v-icon {
  margin: 0 5px;
}
</style>
