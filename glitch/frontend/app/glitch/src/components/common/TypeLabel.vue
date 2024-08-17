<script setup lang="ts">
import { defineProps } from 'vue'
import { ItemType } from '@/types/Item'

const props = defineProps<{
  type: ItemType
}>()

const copyLink = () => {}

const jumpRelation = () => {}
</script>

<template>
  <v-menu>
    <template v-slot:activator="{ props: panelMenuProps }">
      <v-icon
        size="small"
        v-if="props.type == ItemType.EVENT"
        icon="mdi-calendar-arrow-left"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.type == ItemType.FEATURE"
        icon="mdi-apps"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.type == ItemType.STORY"
        icon="mdi-arrow-expand-horizontal"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.type == ItemType.TASK"
        icon="mdi-label"
        v-bind="panelMenuProps"
      />

      <v-icon
        size="small"
        v-if="props.type == ItemType.BUG"
        icon="mdi-spider"
        v-bind="panelMenuProps"
      />
    </template>

    <v-list>
      <v-list-item @click="copyLink()">Copy link</v-list-item>
      <v-list-item @click="jumpRelation()">Jump relation</v-list-item>
    </v-list>
  </v-menu>
</template>

<style scoped>
.v-icon {
  margin-left: 4px;
}
</style>
