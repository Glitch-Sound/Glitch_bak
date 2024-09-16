<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType, ExtractType } from '@/types/Item'
import type { Item, TaskPriorityUpdate, BugPriorityUpdate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'

const props = defineProps<{
  item: Item
}>()

const store_item = useItemStore()

const copyLink = () => {
  const url = new URL(window.location.href)
  url.searchParams.set('extruct', String(ExtractType.RELATION))
  url.searchParams.set('target', props.item.rid.toString())
  navigator.clipboard.writeText(url.toString())
}

const jumpRelation = () => {
  store_item.setExtractItem(props.item.rid)
}

const setTaskPriorityHigh = () => {
  const data: TaskPriorityUpdate = {
    rid: props.item.rid,
    priority: 1
  }
  store_item.updatePriorityTask(data)
}

const setTaskPriorityLow = () => {
  const data: TaskPriorityUpdate = {
    rid: props.item.rid,
    priority: 0
  }
  store_item.updatePriorityTask(data)
}

const setBugPriorityHigh = async () => {
  const data: BugPriorityUpdate = {
    rid: props.item.rid,
    priority: 1
  }
  store_item.updatePriorityBug(data)
}

const setBugPriorityLow = async () => {
  const data: BugPriorityUpdate = {
    rid: props.item.rid,
    priority: 0
  }
  store_item.updatePriorityBug(data)
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
        :color="props.item.priority ? '#a11530' : ''"
      />

      <v-icon
        size="small"
        v-if="props.item.type == ItemType.BUG"
        icon="mdi-spider"
        v-bind="panelMenuProps"
        :color="props.item.priority ? '#a11530' : ''"
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
  margin-left: 10px;
}
</style>
