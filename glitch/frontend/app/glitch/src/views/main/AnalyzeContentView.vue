<script setup lang="ts">
import { onMounted, watch } from 'vue'

import useProjectStore from '@/stores/ProjectStore'
import useItemStore from '@/stores/ItemStore'
import useProgressStore from '@/stores/ProgressStore'
import GanttCharts from '@/components/analyze/GanttCharts.vue'
import SummaryHierarchy from '@/components/progress/SummaryHierarchy.vue'
import SummaryUserTask from '@/components/progress/SummaryUserTask.vue'
import SummaryUserBug from '@/components/progress/SummaryUserBug.vue'

const store_project = useProjectStore()
const store_item = useItemStore()
const store_progress = useProgressStore()

onMounted(async () => {
  // BOP
})
</script>

<template>
  <v-main>
    <v-sheet class="ma-1 py-1 rounded-lg">
      <div class="title">Gantt Chart</div>
      <GanttCharts />

      <!-- <v-row>
        <v-col cols="auto" class="d-flex align-center justify-center">
          <SummaryHierarchy :id_project="store_project.selected_id_project" :rid_users="null" />
        </v-col>

        <v-col cols="auto">
          <div class="title">Summary Item</div>
          <SummaryUserTask :rid_users="store_progress.rid_users" />

          <div class="title">Summary Bug & Alert</div>
          <SummaryUserBug :rid_users="store_progress.rid_users" />
        </v-col>
      </v-row> -->
    </v-sheet>
  </v-main>
</template>

<style scoped>
.title {
  margin: 10px 20px 5px;
  color: #dfdfdf;
  font-size: 20px;
  font-weight: bold;
}
</style>
