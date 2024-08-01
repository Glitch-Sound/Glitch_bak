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
import PanelBug from '@/components/panel/PanelBug.vue'

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
          :type="item.type"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_users="item.rid_users"
          :name="item.name"
          :event_datetime_end="item.event_datetime_end"
          :event_workload="item.event_workload"
          :event_number_completed="item.event_number_completed"
          :event_number_total="item.event_number_total"
        />

        <PanelFeature
          v-if="item.type == ItemType.FEATURE"
          :rid="item.rid"
          :type="item.type"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_users="item.rid_users"
          :name="item.name"
          :feature_workload="item.feature_workload"
          :feature_number_completed="item.feature_number_completed"
          :feature_number_total="item.feature_number_total"
        />

        <PanelStory
          v-if="item.type == ItemType.STORY"
          :rid="item.rid"
          :type="item.type"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_users="item.rid_users"
          :name="item.name"
          :story_datetime_start="item.story_datetime_start"
          :story_datetime_end="item.story_datetime_end"
          :story_workload="item.story_workload"
          :story_number_completed="item.story_number_completed"
          :story_number_total="item.story_number_total"
        />

        <PanelTask
          v-if="item.type == ItemType.TASK"
          :rid="item.rid"
          :type="item.type"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_users="item.rid_users"
          :name="item.name"
          :task_priority="item.task_priority"
          :task_type="item.task_type"
          :task_workload="item.task_workload"
          :task_number_completed="item.task_number_completed"
          :task_number_total="item.task_number_total"
        />

        <PanelBug
          v-if="item.type == ItemType.BUG"
          :rid="item.rid"
          :type="item.type"
          :state="item.state"
          :risk="item.risk"
          :title="item.title"
          :detail="item.detail"
          :result="item.result"
          :datetime_entry="item.datetime_entry"
          :datetime_update="item.datetime_update"
          :rid_users="item.rid_users"
          :name="item.name"
          :bug_priority="item.task_priority"
          :bug_workload="item.task_workload"
        />
      </template>
    </v-sheet>
  </v-main>
</template>

<style scoped></style>
