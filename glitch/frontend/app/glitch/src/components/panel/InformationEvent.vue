<script setup lang="ts">
import { defineProps } from 'vue'

import type { Item } from '@/types/Item'

const props = defineProps<{
  item: Item
}>()
</script>

<template>
  <div class="align-baseline">
    {{ props.item.event_datetime_end }}
    <v-icon icon="$vuetify">mdi-menu-left</v-icon>
  </div>
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
