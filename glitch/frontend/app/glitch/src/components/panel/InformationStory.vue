<script setup lang="ts">
import { defineProps } from 'vue'

import { type Item, ItemState } from '@/types/Item'

const props = defineProps<{
  item: Item
}>()
</script>

<template>
  <div class="align-baseline" v-if="props.item.state == ItemState.IDLE">
    <v-icon icon="$vuetify">mdi-menu-right</v-icon>
    {{ props.item.story_datetime_start }}
  </div>

  <div class="align-baseline" v-if="props.item.state != ItemState.IDLE">
    {{ props.item.story_datetime_end }}
    <v-icon icon="$vuetify">mdi-menu-left</v-icon>
  </div>
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
