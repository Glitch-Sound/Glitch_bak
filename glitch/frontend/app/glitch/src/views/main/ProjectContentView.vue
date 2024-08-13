<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import PanelEvent from '@/components/panel/PanelEvent.vue'
import PanelFeature from '@/components/panel/PanelFeature.vue'
import PanelStory from '@/components/panel/PanelStory.vue'
import PanelTask from '@/components/panel/PanelTask.vue'
import PanelBug from '@/components/panel/PanelBug.vue'

const route = useRoute()
const store_item = useItemStore()

onMounted(() => {
  store_item.fetchItems(Number(route.params.rid))
})
</script>

<template>
  <v-main>
    <v-sheet class="mt-1 ml-1 pa-3 rounded-lg">
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
          :rid_users_review="item.rid_users_review"
          :name_review="item.name_review"
          :event_datetime_end="item.event_datetime_end"
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
          :rid_users_review="item.rid_users_review"
          :name_review="item.name_review"
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
          :rid_users_review="item.rid_users_review"
          :name_review="item.name_review"
          :story_datetime_start="item.story_datetime_start"
          :story_datetime_end="item.story_datetime_end"
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
          :rid_users_review="item.rid_users_review"
          :name_review="item.name_review"
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
          :rid_users_review="item.rid_users_review"
          :name_review="item.name_review"
          :bug_priority="item.task_priority"
          :bug_workload="item.task_workload"
        />
      </template>
    </v-sheet>
  </v-main>
</template>

<style scoped></style>
