<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemState, FeatureCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateFeatureDialog from '@/components/dialog/CreateFeatureDialog.vue'
import AccountSimple from '@/components/common/AccountSimple.vue'

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
  rid_users: Number,
  name: String,
  event_datetime_end: String
})

const openDialog = () => {
  const rid_items = props.rid
  dialogFormData.value = { rid_items }
  dialog.value = true
}

const handleSubmit = async (data: FeatureCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createFeature(data)
    store_item.fetchItems(Number(route.params.rid))
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <div class="d-flex flex-column ma-0 pl-0">
    <div class="d-flex flex-row align-baseline">
      <p class="mx-1">{{ props.rid }}</p>
      <p class="mx-1">state:{{ props.state }}</p>
      <p class="mx-1 font-weight-bold" @click="expand = !expand">{{ props.title }}</p>

      <v-spacer></v-spacer>

      <p class="mx-1">
        <AccountSimple :rid_users="props.rid_users" :name="props.name"></AccountSimple>
      </p>

      <p class="mx-2">information</p>

      <p class="mx-1">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-plus-thick</v-icon>
        </v-btn>
      </p>
    </div>
    <v-expand-transition>
      <div class="ml-6" v-show="expand">
        Detail : {{ props.detail }}

        <v-btn icon size="x-small">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </div>
    </v-expand-transition>
  </div>

  <CreateFeatureDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped></style>
