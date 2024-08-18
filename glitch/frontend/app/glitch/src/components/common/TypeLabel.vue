<script setup lang="ts">
import { defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, type Item, type TaskPriorityUpdate, type BugPriorityUpdate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'

const props = defineProps<{
  item: Item
}>()

const route = useRoute()
const store_item = useItemStore()

const copyLink = () => {}

const jumpRelation = () => {}

const setTaskPriorityHigh = async () => {
  const data: TaskPriorityUpdate = {
    rid: props.item.rid,
    priority: 1
  }
  const service_item = new ItemService()
  await service_item.updatePriorityTask(data)
  store_item.fetchItems(Number(route.params.rid))
}

const setTaskPriorityLow = async () => {
  const data: TaskPriorityUpdate = {
    rid: props.item.rid,
    priority: 0
  }
  const service_item = new ItemService()
  await service_item.updatePriorityTask(data)
  store_item.fetchItems(Number(route.params.rid))
}

const setBugPriorityHigh = async () => {
  const data: BugPriorityUpdate = {
    rid: props.item.rid,
    priority: 1
  }
  const service_item = new ItemService()
  await service_item.updatePriorityBug(data)
  store_item.fetchItems(Number(route.params.rid))
}

const setBugPriorityLow = async () => {
  const data: BugPriorityUpdate = {
    rid: props.item.rid,
    priority: 0
  }
  const service_item = new ItemService()
  await service_item.updatePriorityBug(data)
  store_item.fetchItems(Number(route.params.rid))
}
</script>

<template>
  <v-menu>
    <template v-slot:activator="{ props: panelMenuProps }">
      <v-icon
        size="small"
        v-if="props.item.type == ItemType.EVENT"
        icon="mdi-calendar-arrow-left"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.item.type == ItemType.FEATURE"
        icon="mdi-apps"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.item.type == ItemType.STORY"
        icon="mdi-arrow-expand-horizontal"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.item.type == ItemType.TASK"
        icon="mdi-label"
        v-bind="panelMenuProps"
        :color="props.item.priority ? '#e94560' : ''"
      />

      <v-icon
        size="small"
        v-if="props.item.type == ItemType.BUG"
        icon="mdi-spider"
        v-bind="panelMenuProps"
        :color="props.item.priority ? '#e94560' : ''"
      />
    </template>

    <v-list>
      <v-list-item-title>
        <v-btn prepend-icon="mdi-content-copy" @click="copyLink()">Copy link</v-btn>
      </v-list-item-title>
      <v-list-item-title>
        <v-btn prepend-icon="mdi-relation-one-to-zero-or-many" @click="jumpRelation()">
          Jump relation
        </v-btn>
      </v-list-item-title>

      <template v-if="props.item.type == ItemType.TASK">
        <v-list-item-title v-if="props.item.priority == 0">
          <v-btn prepend-icon="mdi-priority-high" @click="setTaskPriorityHigh()">
            Priority high
          </v-btn>
        </v-list-item-title>
        <v-list-item-title v-else>
          <v-btn prepend-icon="mdi-priority-low" @click="setTaskPriorityLow()">Priority low</v-btn>
        </v-list-item-title>
      </template>

      <template v-if="props.item.type == ItemType.BUG">
        <v-list-item-title v-if="props.item.priority == 0">
          <v-btn prepend-icon="mdi-priority-high" @click="setBugPriorityHigh()">
            Priority high
          </v-btn>
        </v-list-item-title>
        <v-list-item-title v-else>
          <v-btn prepend-icon="mdi-priority-low" @click="setBugPriorityLow()">Priority low</v-btn>
        </v-list-item-title>
      </template>
    </v-list>
  </v-menu>
</template>

<style scoped>
.v-icon {
  margin-left: 4px;
}
</style>
