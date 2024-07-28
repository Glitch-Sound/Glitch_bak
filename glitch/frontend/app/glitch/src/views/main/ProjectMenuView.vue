<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateEventDialog from '@/components/dialog/CreateEventDialog.vue'
import type { EventCreate } from '@/types/Item'

const dialog = ref(false)
const dialogFormData = ref({ rid_items: 0 })

const route = useRoute()
const openDialog = () => {
  const rid_items = Number(route.params.rid)
  dialogFormData.value = { rid_items }
  dialog.value = true
}

const store_item = useItemStore()

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
  <v-navigation-drawer>
    <v-sheet>
      <v-btn prepend-icon="mdi-plus-circle" @click="openDialog()">Event</v-btn>

      <p>xxx</p>
      <p>xxx</p>
      <p>xxx</p>
    </v-sheet>

    <v-divider :thickness="3"></v-divider>

    <v-sheet>
      <v-btn prepend-icon="mdi-plus-circle">Filter</v-btn>

      <p>xxx</p>
      <p>xxx</p>
      <p>xxx</p>
    </v-sheet>
  </v-navigation-drawer>

  <CreateEventDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped></style>
