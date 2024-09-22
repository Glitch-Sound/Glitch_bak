<script setup lang="ts">
import { defineProps, computed } from 'vue'
import type { Item } from '@/types/Item'

const props = defineProps<{
  item: Item
}>()

const textColor = computed(() => {
  const risk = props.item.risk

  if (0 <= risk && risk < 100) {
    return 'rgb(247, 247, 247)'
  } else if (100 <= risk && risk < 200) {
    return 'rgb(250, 248, 246)'
  } else if (200 <= risk && risk < 300) {
    return 'rgb(252, 250, 245)'
  } else if (300 <= risk && risk < 400) {
    return 'rgb(253, 252, 243)'
  } else if (400 <= risk && risk < 500) {
    return 'rgb(254, 253, 241)'
  } else if (500 <= risk && risk < 600) {
    return 'rgb(254, 249, 238)'
  } else if (600 <= risk && risk < 700) {
    return 'rgb(254, 245, 236)'
  } else if (700 <= risk && risk < 800) {
    return 'rgb(254, 241, 234)'
  } else if (800 <= risk && risk < 900) {
    return 'rgb(254, 237, 232)'
  } else {
    return 'rgb(253, 231, 226)'
  }
})
</script>

<template>
  <span :style="{ color: textColor }">{{ props.item.title }}</span>
</template>

<style scoped></style>
