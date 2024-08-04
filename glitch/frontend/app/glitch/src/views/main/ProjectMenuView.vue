<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import type { EventCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import useUserStore from '@/stores/UserStore'
import ItemService from '@/services/ItemService'
import CreateEventDialog from '@/components/dialog/CreateEventDialog.vue'

const route = useRoute()
const store_item = useItemStore()
const store_user = useUserStore()

const dialog = ref(false)
const dialogFormData = ref({ rid_items: 0 })

onMounted(() => {
  store_user.fetchUsers()
})

const openDialog = () => {
  const rid_items = Number(route.params.rid)
  dialogFormData.value = { rid_items }
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
  <v-navigation-drawer>
    <v-sheet>
      <v-btn prepend-icon="mdi-plus-circle" @click="openDialog()">Event</v-btn>

      <p><v-icon icon="mdi-moon-full" />All</p>
      <p><v-icon icon="mdi-moon-waning-crescent" />Incomplete</p>
      <p><v-icon icon="mdi-alert" />High Risk</p>
      <p><v-icon icon="mdi-alert-box" />Alert</p>
      <p><v-icon icon="mdi-account" />Assignment</p>
    </v-sheet>

    <v-divider :thickness="3"></v-divider>

    <v-sheet>
      <p><v-icon icon="mdi-calendar-arrow-left" />Event</p>
      <p><v-icon icon="mdi-apps" />Feature</p>
      <p><v-icon icon="mdi-arrow-expand-horizontal" />Story</p>
      <p><v-icon icon="mdi-label" />Task</p>
      <p><v-icon icon="mdi-spider" />Bug</p>
    </v-sheet>

    <v-divider :thickness="3"></v-divider>

    <v-sheet>
      <p><v-icon icon="mdi-circle-outline" />IDLE</p>
      <p><v-icon icon="mdi-circle" />RUN</p>
      <p><v-icon icon="mdi-circle-multiple" />REVIEW</p>
      <p><v-icon icon="mdi-circle-slice-8" />COMPLETE</p>
    </v-sheet>

    <v-divider :thickness="3"></v-divider>

    <v-sheet>
      <ul v-if="store_user.users.length">
        <li v-for="user in store_user.users" :key="user.rid">
          {{ user.name }}
        </li>
      </ul>
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
