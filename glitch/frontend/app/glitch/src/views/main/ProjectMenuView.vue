<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ExtractType, type EventCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateEventDialog from '@/components/dialog/CreateEventDialog.vue'

const route = useRoute()
const store_item = useItemStore()

const dialog = ref(false)

const dialog_form_data = ref<EventCreate>({
  id_project: Number(route.params.id_project),
  rid_items: Number(route.params.id_project),
  rid_users: 0,
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

const setExtractType = (type: ExtractType) => {
  store_item.setExtractType(type)
  store_item.fetchItems()
}

const handleSubmit = async (data: EventCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createEvent(data)
    store_item.fetchItems()
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <v-navigation-drawer color="background" class="no-border">
    <v-sheet color="#101010" class="rounded-lg mt-1 ml-1 py-3">
      <v-list-item>
        <v-btn width="250px" color="#9D0B28" prepend-icon="mdi-plus-circle" @click="openDialog()">
          Event
        </v-btn>
      </v-list-item>

      <v-list-item @click="setExtractType(ExtractType.ALL)">
        <v-icon icon="mdi-moon-full" />All
      </v-list-item>
      <v-list-item @click="setExtractType(ExtractType.INCOMPLETE)">
        <v-icon icon="mdi-moon-waning-crescent" />Incomplete
      </v-list-item>
      <v-list-item disabled @click="setExtractType(ExtractType.HIGH_RISK)">
        <v-icon icon="mdi-fire" />High Risk
      </v-list-item>
      <v-list-item @click="setExtractType(ExtractType.ALERT)">
        <v-icon icon="mdi-alert-box" />Alert
      </v-list-item>
      <v-list-item @click="setExtractType(ExtractType.ASSIGNMENT)">
        <v-icon icon="mdi-account" />Assignment
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
    :showDialog="dialog"
    :formData="dialog_form_data"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/assets/main.css';

.v-icon {
  margin: 0 15px 0 0;
}
</style>
