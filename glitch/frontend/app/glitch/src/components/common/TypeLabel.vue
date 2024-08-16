<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType } from '@/types/Item'

const props = defineProps<{
  type: ItemType
}>()
</script>

<template>
  <v-icon size="small" v-if="props.type == ItemType.EVENT" icon="mdi-calendar-arrow-left" />
  <v-icon size="small" v-if="props.type == ItemType.FEATURE" icon="mdi-apps" />
  <v-icon size="small" v-if="props.type == ItemType.STORY" icon="mdi-arrow-expand-horizontal" />
  <v-icon size="small" v-if="props.type == ItemType.TASK" icon="mdi-label" />
  <v-icon size="small" v-if="props.type == ItemType.BUG" icon="mdi-spider" />
</template>

<style scoped>
.v-icon {
  margin-left: 4px;
}
</style>
