<script setup lang="ts">
import { onMounted, watch } from 'vue'

import { ItemType } from '@/types/Item'
import useProjectStore from '@/stores/ProjectStore'
import useItemStore from '@/stores/ItemStore'
import useAnalyzeStore from '@/stores/AnalyzeStore'
import GanttCharts from '@/components/analyze/GanttCharts.vue'
import ProjectHierarchy from '@/components/analyze/ProjectHierarchy.vue'
import ProjectTask from '@/components/analyze/ProjectTask.vue'
import ProjectBug from '@/components/analyze/ProjectBug.vue'
import ItemFrequency from '@/components/analyze/ItemFrequency.vue'

import PanelEvent from '@/components/panel/PanelEvent.vue'
import PanelFeature from '@/components/panel/PanelFeature.vue'
import PanelStory from '@/components/panel/PanelStory.vue'
import PanelTask from '@/components/panel/PanelTask.vue'
import PanelBug from '@/components/panel/PanelBug.vue'

const store_project = useProjectStore()
const store_item = useItemStore()
const store_analyze = useAnalyzeStore()

onMounted(async () => {
  store_analyze.fetchItems(store_project.selected_id_project)
})

watch(
  () => store_analyze.select_date,
  () => {
    store_analyze.fetchItems(store_project.selected_id_project)
  }
)
</script>

<template>
  <v-main>
    <v-sheet class="ma-1 py-1 rounded-lg">
      <v-row>
        <v-col cols="auto" class="d-flex align-center justify-center">
          <ProjectHierarchy :id_project="store_project.selected_id_project" />
        </v-col>

        <v-col cols="auto">
          <div class="title">Summary Item</div>
          <ProjectTask :id_project="store_project.selected_id_project" />

          <div class="title">Summary Bug & Alert</div>
          <ProjectBug :id_project="store_project.selected_id_project" />
        </v-col>
      </v-row>

      <div class="title">Gantt Chart</div>
      <GanttCharts />

      <div class="title">Frequency</div>
      <ItemFrequency :id_project="store_project.selected_id_project" />

      <div class="title">Item</div>
      <div class="mx-5">
        <template v-for="item in store_analyze.items" :key="item.rid">
          <PanelEvent v-if="item.type == ItemType.EVENT" :item="item" />
          <PanelFeature v-if="item.type == ItemType.FEATURE" :item="item" />
          <PanelStory v-if="item.type == ItemType.STORY" :item="item" />
          <PanelTask v-if="item.type == ItemType.TASK" :item="item" />
          <PanelBug v-if="item.type == ItemType.BUG" :item="item" />
        </template>
      </div>
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
