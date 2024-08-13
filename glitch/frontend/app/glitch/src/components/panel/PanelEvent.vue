<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ItemState, type FeatureCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateFeatureDialog from '@/components/dialog/CreateFeatureDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import AccountLabel from '@/components/common/AccountLabel.vue'

const route = useRoute()
const store_item = useItemStore()

const expand = ref(false)
const dialog = ref(false)

const dialogFormData = ref<FeatureCreate>({
  rid_items: 0,
  rid_user: 0,
  title: '',
  detail: ''
})

const props = defineProps<{
  rid: number
  type: ItemType
  state: ItemState
  risk: number
  title: string
  detail: string
  result: string
  datetime_entry: string
  datetime_update: string
  rid_users: number
  name: string
  rid_users_review: number | null
  name_review: string | null
  event_datetime_end: string
}>()

const openDialog = () => {
  const rid_items = props.rid
  dialogFormData.value.rid_items = rid_items
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
  <div class="d-flex flex-column ma-0 py-2 pl-1">
    <div class="d-flex flex-row align-baseline">
      <p class="mx-1">
        <TypeLabel :type="props.type" />
      </p>

      <p class="mx-1" style="width: 100px; text-align: center">
        <StateLabel :state="props.state" />
      </p>

      <p class="mx-1 font-weight-bold" @click="expand = !expand">{{ props.title }}</p>

      <v-spacer></v-spacer>

      <p class="mx-1">
        <AccountLabel :rid_users="props.rid_users" :name="props.name" />
      </p>

      <p class="mx-6">information</p>

      <p class="mx-1">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-plus-thick</v-icon>
        </v-btn>
      </p>
    </div>
    <v-expand-transition>
      <div class="ml-6" v-show="expand">
        <p>Detail : {{ props.detail }}</p>
        <p>Result : {{ props.result }}</p>

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
