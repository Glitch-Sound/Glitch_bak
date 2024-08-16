<script setup lang="ts">
import { defineProps } from 'vue'

import MarkedText from '@/components/common/MarkedText.vue'

const props = defineProps<{
  expand: boolean
  risk: number
  risk_factors: number
  detail: string
  result: string
}>()
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
          <v-btn size="small" prepend-icon="mdi-pencil" variant="outlined">UPDATE</v-btn>
        </v-col>
      </v-row>
    </div>
  </v-expand-transition>
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
