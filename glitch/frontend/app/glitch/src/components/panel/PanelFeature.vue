<script setup lang="ts">
import { defineProps } from 'vue'
import PanelBase from '@/components/panel/PanelBase.vue'

const props = defineProps({
  rid: Number,
  state: Number,
  risk: Number,
  title: String,
  detail: String,
  result: String,
  datetime_entry: String,
  datetime_update: String,
  name: String
})
</script>

<template>
  <PanelBase :baseDiv="'pl-5'">
    <template #title>{{ props.title }}</template>
  </PanelBase>
</template>

<style scoped></style>
