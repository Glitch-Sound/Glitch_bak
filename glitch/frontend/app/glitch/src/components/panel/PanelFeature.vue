<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemState, StoryCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateStoryDialog from '@/components/dialog/CreateStoryDialog.vue'

const route = useRoute()
const store_item = useItemStore()

const expand = ref(false)
const dialog = ref(false)
const dialogFormData = ref({ rid_items: 0 })

const props = defineProps({
  rid: Number,
  state: ItemState,
  risk: Number,
  title: String,
  detail: String,
  result: String,
  datetime_entry: String,
  datetime_update: String,
  name: String
})

const openDialog = () => {
  const rid_items = props.rid
  dialogFormData.value = { rid_items }
  dialog.value = true
}

const handleSubmit = async (data: StoryCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createStory(data)
    store_item.fetchItems(Number(route.params.rid))
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <div class="d-flex flex-column ma-0 pl-5">
    <div class="d-flex flex-row align-baseline">
      <div>ID[{{ props.rid }}]</div>

      <div>RISK[{{ props.risk }}]</div>

      <div>STATE[{{ props.state }}]</div>

      <div @click="expand = !expand">TITLE[{{ props.title }}]</div>

      <v-spacer></v-spacer>

      {{ props.name }}
      <v-btn icon size="x-small">
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <div>&nbsp;information&nbsp;</div>

      <v-btn icon size="x-small" @click="openDialog()">
        <v-icon>mdi-plus-thick</v-icon>
      </v-btn>
    </div>
    <v-expand-transition>
      <div v-show="expand">
        Detail : {{ props.detail }}

        <v-btn icon size="x-small">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </div>
    </v-expand-transition>
  </div>

  <CreateStoryDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped></style>
