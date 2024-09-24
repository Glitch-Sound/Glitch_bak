<script setup lang="ts">
import { onMounted, watch, computed } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType } from '@/types/Item'
import useProjectStore from '@/stores/ProjectStore'
import useItemStore from '@/stores/ItemStore'
import useProgressStore from '@/stores/ProgressStore'
import UserHierarchy from '@/components/analyze/UserHierarchy.vue'
import SummaryUserTask from '@/components/analyze/SummaryUserTask.vue'
import SummaryUserBug from '@/components/analyze/SummaryUserBug.vue'
import PanelEvent from '@/components/panel/PanelEvent.vue'
import PanelFeature from '@/components/panel/PanelFeature.vue'
import PanelStory from '@/components/panel/PanelStory.vue'
import PanelTask from '@/components/panel/PanelTask.vue'
import PanelBug from '@/components/panel/PanelBug.vue'

const route = useRoute()
const store_project = useProjectStore()
const store_item = useItemStore()
const store_progress = useProgressStore()

const rid_user = computed(() => route.params.target)

onMounted(async () => {
  store_progress.setUser(Number(rid_user.value))
  if (store_project.selected_id_project) {
    common()
  }
})

watch(
  () => store_item.is_update,
  async (value_new) => {
    if (value_new) {
      common()
    }
  }
)

watch(
  () => store_progress.rid_users,
  (rid_users) => {
    store_progress.setUser(rid_users)
    common()
  }
)

const common = async () => {
  if (store_project.selected_id_project && store_progress.rid_users) {
    await store_progress.fetchSummariesUser(
      store_project.selected_id_project,
      store_progress.rid_users
    )
    await store_progress.fetchItems(store_project.selected_id_project, store_progress.rid_users)
  }
}
</script>

<template>
  <v-main>
    <v-sheet class="ma-1 py-1 rounded-lg">
      <v-row>
        <v-col cols="auto" class="d-flex align-center justify-center">
          <UserHierarchy
            :id_project="store_project.selected_id_project"
            :rid_users="store_progress.rid_users"
          />
        </v-col>

        <v-col cols="auto">
          <div class="title">Summary Item</div>
          <SummaryUserTask :rid_users="store_progress.rid_users" />

          <div class="title">Summary Bug & Alert</div>
          <SummaryUserBug :rid_users="store_progress.rid_users" />
        </v-col>
      </v-row>

      <div class="title">Assignment</div>
      <div class="mx-5">
        <template v-for="item in store_progress.items" :key="item.rid">
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
