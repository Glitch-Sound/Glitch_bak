<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps<{
  risk: number
  event_datetime_end: string
}>()
</script>

<template>
  <div class="align-baseline">
    {{ props.event_datetime_end }}
    <v-icon icon="$vuetify">mdi-menu-left</v-icon>
  </div>
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
