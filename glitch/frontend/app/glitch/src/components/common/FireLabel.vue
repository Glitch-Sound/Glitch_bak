<script setup lang="ts">
import { defineProps } from 'vue'

import type { Item } from '@/types/Item'
import { RISK_LOW, RISK_HIGH } from '@/components/common/common'

const props = defineProps<{
  item: Item
}>()
</script>

<template>
  <v-icon size="small" class="risk-high" v-if="RISK_HIGH <= props.item.risk" icon="mdi-fire" />
  <v-icon size="small" class="risk-low" v-else-if="RISK_LOW <= props.item.risk" icon="mdi-fire" />
</template>

<style scoped>
.risk-low {
  color: #b1a47c;
}

.risk-high {
  color: #ba374c;
}
</style>
