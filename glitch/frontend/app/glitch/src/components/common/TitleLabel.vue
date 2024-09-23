<script setup lang="ts">
import { defineProps } from 'vue'
import type { Item } from '@/types/Item'

const props = defineProps<{
  item: Item
}>()
</script>

<template>
  <span class="title">{{ props.item.title }}</span>
</template>

<style scoped>
.title {
  color: #efefef;
}

.title:hover {
  color: #ffffff;
}
</style>
