<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ExtractType, type EventCreate } from '@/types/Item'
import useUserStore from '@/stores/UserStore'
import useItemStore from '@/stores/ItemStore'
import CreateEventDialog from '@/components/dialog/CreateEventDialog.vue'

const route = useRoute()
const store_user = useUserStore()
const store_item = useItemStore()

const dialog = ref(false)

const dialog_form_data = ref<EventCreate>({
  id_project: Number(route.params.id_project),
  rid_items: Number(route.params.id_project),
  rid_users: store_user.login_user?.rid ?? 0,
  title: '',
  detail: '',
  datetime_end: ''
})

const openDialog = () => {
  dialog.value = true
}

const setEnabledType = (type: ItemType) => {
  store_item.setEnabledType(type)
}

const handleSubmit = async (data: EventCreate) => {
  await store_item.createEvent(data)
  dialog.value = false
}
</script>

<template>
  <v-navigation-drawer color="background" class="no-border">
    <v-sheet color="#101010" class="rounded-lg mt-1 ml-1 py-3">
      <v-list-item>
        <v-btn width="250px" color="#950531" prepend-icon="mdi-plus-circle" @click="openDialog()">
          Event
        </v-btn>
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.INCOMPLETE,
          'extract-unselected': store_item.type_extract !== ExtractType.INCOMPLETE
        }"
        @click="store_item.setExtractIncomplete()"
      >
        <v-icon icon="mdi-moon-waning-crescent" />Incomplete
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.ALL,
          'extract-unselected': store_item.type_extract !== ExtractType.ALL
        }"
        @click="store_item.setExtractAll()"
      >
        <v-icon icon="mdi-moon-full" />All
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.HIGH_RISK,
          'extract-unselected': store_item.type_extract !== ExtractType.HIGH_RISK
        }"
        @click="store_item.setExtractHighRisk()"
      >
        <v-icon icon="mdi-fire" />High Risk
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.ALERT,
          'extract-unselected': store_item.type_extract !== ExtractType.ALERT
        }"
        @click="store_item.setExtractAlert()"
      >
        <v-icon icon="mdi-alert-box" />Alert
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.ASSIGNMENT,
          'extract-unselected': store_item.type_extract !== ExtractType.ASSIGNMENT
        }"
        @click="store_item.setExtractAssignment()"
      >
        <v-icon icon="mdi-account" />Assignment
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.SEARCH,
          'extract-unselected': store_item.type_extract !== ExtractType.SEARCH
        }"
        @click="store_item.setExtractSearchUpdate()"
        :disabled="store_item.extract_search_target === ''"
      >
        <v-icon icon="mdi-magnify" />Search
      </v-list-item>

      <v-list-item
        :class="{
          'extract-selected': store_item.type_extract === ExtractType.RELATION,
          'extract-unselected': store_item.type_extract !== ExtractType.RELATION
        }"
        @click="store_item.setExtractItemUpdate()"
        :disabled="store_item.extract_rid_item === 0"
      >
        <v-icon icon="mdi-relation-many-to-many" />Relation
      </v-list-item>
    </v-sheet>

    <v-sheet color="#101010" class="rounded-lg mt-1 ml-1 py-3">
      <v-list-item
        @click="setEnabledType(ItemType.EVENT)"
        :variant="ItemType.EVENT <= store_item.type_enabled ? 'text' : 'plain'"
      >
        <v-icon icon="mdi-calendar-arrow-left" />
        Event
      </v-list-item>
      <v-list-item
        @click="setEnabledType(ItemType.FEATURE)"
        :variant="ItemType.FEATURE <= store_item.type_enabled ? 'text' : 'plain'"
      >
        <v-icon icon="mdi-apps" />
        Feature
      </v-list-item>
      <v-list-item
        @click="setEnabledType(ItemType.STORY)"
        :variant="ItemType.STORY <= store_item.type_enabled ? 'text' : 'plain'"
      >
        <v-icon icon="mdi-arrow-expand-horizontal" />
        Story
      </v-list-item>
      <v-list-item
        @click="setEnabledType(ItemType.TASK)"
        :variant="ItemType.TASK <= store_item.type_enabled ? 'text' : 'plain'"
      >
        <v-icon icon="mdi-label" />
        Task
      </v-list-item>
      <v-list-item
        @click="setEnabledType(ItemType.BUG)"
        :variant="ItemType.BUG <= store_item.type_enabled ? 'text' : 'plain'"
      >
        <v-icon icon="mdi-spider" />
        Bug
      </v-list-item>
    </v-sheet>
  </v-navigation-drawer>

  <CreateEventDialog
    :dialog_show="dialog"
    :data_form="dialog_form_data"
    :rid_parent="Number(route.params.id_project)"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/assets/main.css';

.v-icon {
  margin: 0 15px 0 0;
}

.extract-selected {
  border-left: 4px solid #196fb3;
}

.extract-unselected {
  border-left: 4px solid transparent;
}
</style>
