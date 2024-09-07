<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType } from '@/types/Item'
import useProjectStore from '@/stores/ProjectStore'
import useItemStore from '@/stores/ItemStore'
import PanelEvent from '@/components/panel/PanelEvent.vue'
import PanelFeature from '@/components/panel/PanelFeature.vue'
import PanelStory from '@/components/panel/PanelStory.vue'
import PanelTask from '@/components/panel/PanelTask.vue'
import PanelBug from '@/components/panel/PanelBug.vue'

const route = useRoute()
const store_project = useProjectStore()
const store_item = useItemStore()

onMounted(() => {
  store_project.setSelectedProjectID(Number(route.params.id_project))
})
</script>

<template>
  <v-main>
    <v-sheet class="ma-1 py-1 rounded-lg">
      <template v-for="item in store_item.items" :key="item.rid">
        <PanelEvent
          v-if="item.type <= store_item.type_enabled && item.type == ItemType.EVENT"
          :item="item"
        />
        <PanelFeature
          v-if="item.type <= store_item.type_enabled && item.type == ItemType.FEATURE"
          :item="item"
        />
        <PanelStory
          v-if="item.type <= store_item.type_enabled && item.type == ItemType.STORY"
          :item="item"
        />
        <PanelTask
          v-if="item.type <= store_item.type_enabled && item.type == ItemType.TASK"
          :item="item"
        />
        <PanelBug
          v-if="item.type <= store_item.type_enabled && item.type == ItemType.BUG"
          :item="item"
        />
      </template>
    </v-sheet>
  </v-main>
</template>

<style scoped></style>
