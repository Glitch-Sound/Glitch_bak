<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

import type { EventCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateEventDialog from '@/components/dialog/CreateEventDialog.vue'

const route = useRoute()
const store_item = useItemStore()

const dialog = ref(false)

const dialogFormData = ref<EventCreate>({
  rid_items: 0,
  rid_user: 0,
  title: '',
  detail: '',
  datetime_end: ''
})

const openDialog = () => {
  const rid_items = Number(route.params.rid)
  dialogFormData.value.rid_items = rid_items
  dialog.value = true
}

const handleSubmit = async (data: EventCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createEvent(data)
    store_item.fetchItems(Number(route.params.rid))
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <v-navigation-drawer color="background" class="no-border">
    <v-sheet color="#1d1d1d" class="rounded-lg mt-1 ml-1 py-3">
      <v-list-item>
        <v-btn width="250px" color="#9D0B28" prepend-icon="mdi-plus-circle" @click="openDialog()"
          >Event</v-btn
        >
      </v-list-item>
      <v-list-item><v-icon icon="mdi-moon-full" />All</v-list-item>
      <v-list-item><v-icon icon="mdi-moon-waning-crescent" />Incomplete</v-list-item>
      <v-list-item><v-icon icon="mdi-alert" />High Risk</v-list-item>
      <v-list-item><v-icon icon="mdi-alert-box" />Alert</v-list-item>
      <v-list-item><v-icon icon="mdi-account" />Assignment</v-list-item>
    </v-sheet>

    <v-sheet color="#1d1d1d" class="rounded-lg mt-1 ml-1 py-3">
      <v-list-item><v-icon icon="mdi-calendar-arrow-left" />Event</v-list-item>
      <v-list-item><v-icon icon="mdi-apps" />Feature</v-list-item>
      <v-list-item><v-icon icon="mdi-arrow-expand-horizontal" />Story</v-list-item>
      <v-list-item><v-icon icon="mdi-label" />Task</v-list-item>
      <v-list-item><v-icon icon="mdi-spider" />Bug</v-list-item>
    </v-sheet>
  </v-navigation-drawer>

  <CreateEventDialog
    :showDialog="dialog"
    :formData="dialogFormData"
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
