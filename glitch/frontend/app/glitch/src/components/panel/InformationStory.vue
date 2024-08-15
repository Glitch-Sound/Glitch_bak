<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemState } from '@/types/Item'

const props = defineProps<{
  state: ItemState
  risk: number
  story_datetime_start: string
  story_datetime_end: string
}>()
</script>

<template>
  <div class="align-baseline" v-if="props.state == ItemState.IDLE">
    <v-icon icon="$vuetify">mdi-menu-right</v-icon>
    {{ props.story_datetime_start }}
  </div>

  <div class="align-baseline" v-if="props.state != ItemState.IDLE">
    {{ props.story_datetime_end }}
    <v-icon icon="$vuetify">mdi-menu-left</v-icon>
  </div>
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
