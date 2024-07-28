<script setup lang="ts">
import { watch } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import useProjectStore from '@/stores/ProjectStore'
import PanelEvent from '@/components/panel/PanelEvent.vue'
import PanelFeature from '@/components/panel/PanelFeature.vue'
import PanelStory from '@/components/panel/PanelStory.vue'
import PanelTask from '@/components/panel/PanelTask.vue'

const route = useRoute()
const store_item = useItemStore()
const store_project = useProjectStore()

watch([() => store_project.projects.length], () => {
  store_item.fetchItems(Number(route.params.rid))
})
</script>

<template>
  <v-main>
    <v-sheet>
      <template v-for="item in store_item.items" :key="item.rid">
        <PanelEvent
          v-if="item.type == ItemType.EVENT"
          :rid="item.rid"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_user="item.rid_user"
          :name="item.name"
          :event_datetime_end="item.event_datetime_end"
        />

        <PanelFeature
          v-if="item.type == ItemType.FEATURE"
          :rid="item.rid"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_user="item.rid_user"
          :name="item.name"
        />

        <PanelStory
          v-if="item.type == ItemType.STORY"
          :rid="item.rid"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_user="item.rid_user"
          :name="item.name"
          :story_datetime_start="item.story_datetime_start"
          :story_datetime_end="item.story_datetime_end"
        />

        <PanelTask
          v-if="item.type == ItemType.TASK"
          :rid="item.rid"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_user="item.rid_user"
          :name="item.name"
          :task_priority="item.task_priority"
          :task_type="item.task_type"
          :task_workload="item.task_workload"
          :task_number_completed="item.task_number_completed"
          :task_number_total="item.task_number_total"
        />
      </template>
    </v-sheet>
  </v-main>
</template>

<style scoped></style>
