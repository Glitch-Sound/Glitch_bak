<script setup lang="ts">
import { defineProps } from 'vue'

import { ItemType, type Item } from '@/types/Item'

const props = defineProps<{
  item: Item
}>()

const copyLink = () => {}

const jumpRelation = () => {}

const setTaskPriorityHigh = () => {}

const setTaskPriorityLow = () => {}

const setBugPriorityHigh = () => {}

const setBugPriorityLow = () => {}
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
      />

      <v-icon
        size="small"
        v-if="props.item.type == ItemType.BUG"
        icon="mdi-spider"
        v-bind="panelMenuProps"
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
        <v-list-item-title v-if="props.item.task_priority == 0">
          <v-btn prepend-icon="mdi-priority-high" @click="setTaskPriorityHigh()">
            Priority high
          </v-btn>
        </v-list-item-title>
        <v-list-item-title v-else>
          <v-btn prepend-icon="mdi-priority-low" @click="setTaskPriorityLow()">Priority low</v-btn>
        </v-list-item-title>
      </template>

      <template v-if="props.item.type == ItemType.BUG">
        <v-list-item-title v-if="props.item.bug_priority == 0">
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
