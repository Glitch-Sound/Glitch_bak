<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ItemState, StoryCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateStoryDialog from '@/components/dialog/CreateStoryDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import AccountLabel from '@/components/common/AccountLabel.vue'

const route = useRoute()
const store_item = useItemStore()

const expand = ref(false)
const dialog = ref(false)
const dialogFormData = ref({ rid_items: 0 })

const props = defineProps({
  rid: Number,
  type: ItemType,
  state: ItemState,
  risk: Number,
  title: String,
  detail: String,
  result: String,
  datetime_entry: String,
  datetime_update: String,
  rid_users: Number,
  name: String,
  rid_users_review: Number,
  name_review: String,
  feature_workload: Number,
  feature_number_completed: Number,
  feature_number_total: Number
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
  <div class="d-flex flex-column ma-0 py-2 pl-6">
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
        <AccountLabel :rid_users="props.rid_users" :name="props.name"></AccountLabel>
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

  <CreateStoryDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped></style>
