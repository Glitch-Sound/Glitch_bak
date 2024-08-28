<script setup lang="ts">
import { defineProps } from 'vue'

import type { Summary } from '@/types/Summary'

const props = defineProps<{
  title: string
  summary: Summary
}>()
</script>

<template>
  <v-table class="table">
    <tr class="state-idle">
      <td rowspan="6" class="title">{{ props.title }}</td>
      <td>IDLE</td>
      <td class="value">{{ props.summary.idle }}</td>
    </tr>
    <tr class="state-run">
      <td>RUN</td>
      <td class="value">{{ props.summary.run }}</td>
    </tr>
    <tr class="state-alert">
      <td>ALERT</td>
      <td class="value">{{ props.summary.alert }}</td>
    </tr>
    <tr class="state-review">
      <td>REVIEW</td>
      <td class="value">{{ props.summary.review }}</td>
    </tr>
    <tr class="state-complete">
      <td>COMPLETE</td>
      <td class="value">{{ props.summary.complete }}</td>
    </tr>
    <tr class="state-total">
      <td>TOTAL</td>
      <td class="value">{{ props.summary.total }}</td>
    </tr>
  </v-table>
</template>

<style scoped>
.table {
  margin-left: 20px;
}

.table td {
  padding: 0 10px;
}

.title {
  width: 60px;
  vertical-align: top;
  color: #e0e0e0;
  font-weight: bold;
}

.state-idle {
  color: #b0e0e6;
  opacity: 0.7;
}

.state-run {
  color: #84c69b;
  opacity: 0.7;
}

.state-alert {
  color: #e94560;
  opacity: 0.7;
}

.state-review {
  color: #dece9c;
  opacity: 0.7;
}

.state-complete {
  color: #a9a9a9;
  opacity: 0.7;
}

.state-total {
  color: #f0f0f0;
  opacity: 0.7;
}

.value {
  width: 50px;
  text-align: right;
}
</style>
