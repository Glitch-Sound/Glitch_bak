<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemState } from '@/types/Item'

const props = defineProps({
  state: ItemState
})
</script>

<template>
  <v-icon size="small" v-if="props.state == ItemState.IDLE" icon="mdi-circle-outline" />
  <v-icon size="small" v-if="props.state == ItemState.RUN" icon="mdi-circle" />
  <v-icon size="small" v-if="props.state == ItemState.REVIEW" icon="mdi-circle-multiple" />
  <v-icon size="small" v-if="props.state == ItemState.COMPLETE" icon="mdi-circle-slice-8" />
</template>

<style scoped></style>
