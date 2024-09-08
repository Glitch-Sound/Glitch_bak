<script setup lang="ts">
import { onMounted, watch } from 'vue'

import useProjectStore from '@/stores/ProjectStore'
import useProgressStore from '@/stores/ProgressStore'
import SummaryUser from '@/components/progress/SummaryUser.vue'

const store_project = useProjectStore()
const store_progress = useProgressStore()

onMounted(async () => {
  if (store_project.selected_id_project) {
    await store_progress.fetchSummariesUser(
      store_project.selected_id_project,
      store_progress.rid_users
    )
  }
})

watch(
  () => store_progress.rid_users,
  async (value_new) => {
    if (value_new && store_project.selected_id_project) {
      await store_progress.fetchSummariesUser(store_project.selected_id_project, value_new)
    }
  }
)
</script>

<template>
  <v-main>
    <v-sheet class="ma-1 py-1 rounded-lg">
      <SummaryUser :rid_users="store_progress.rid_users" />
      <!-- Item -->
    </v-sheet>
  </v-main>
</template>

<style scoped></style>
