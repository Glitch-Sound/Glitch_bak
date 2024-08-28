<script setup lang="ts">
import { ref, defineProps, onMounted, watch } from 'vue'

import type { Item } from '@/types/Item'
import type { Summary } from '@/types/Summary'
import useSummaryStore from '@/stores/SummaryStore'
import StateSummary from '@/components/common/StateSummary.vue'

const props = defineProps<{
  item: Item
}>()

const store_summary = useSummaryStore()

const summary = ref<Summary>({
  idle: 0,
  run: 0,
  alert: 0,
  review: 0,
  complete: 0,
  total: 0
})

onMounted(async () => {
  await store_summary.fetchSummaryItem(props.item.rid)
})

watch(
  store_summary.summaries_item,
  (items_new) => {
    const items = items_new.get(props.item.rid)
    if (items && items.length > 0) {
      const lastItem = items[items.length - 1]
      summary.value.idle = lastItem.task_count_idle
      summary.value.run = lastItem.task_count_run
      summary.value.alert = lastItem.task_count_alert
      summary.value.review = lastItem.task_count_review
      summary.value.complete = lastItem.task_count_complete
      summary.value.total = lastItem.task_count_total
    }

    console.log(items)
  },
  { immediate: true }
)
</script>

<template>
  <StateSummary title="Task" :summary="summary" />
</template>

<style scoped></style>
