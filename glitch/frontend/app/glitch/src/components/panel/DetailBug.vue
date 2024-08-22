<script setup lang="ts">
import { ref, defineProps } from 'vue'

import type { Item, BugUpdate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import UpdateBugDialog from '@/components/dialog/UpdateBugDialog.vue'

import MarkedText from '@/components/common/MarkedText.vue'

const props = defineProps<{
  expand: boolean
  item: Item
}>()

const store_item = useItemStore()

const dialog = ref(false)

const dialog_form_data = ref<BugUpdate>({
  rid: 0,
  state: 0,
  rid_users: 0,
  rid_users_review: null,
  title: '',
  detail: '',
  result: '',
  workload: 0
})

const openDialog = () => {
  dialog_form_data.value = {
    rid: props.item.rid,
    state: props.item.state,
    rid_users: props.item.rid_users,
    rid_users_review: props.item.rid_users_review,
    title: props.item.title,
    detail: props.item.detail,
    result: props.item.result,
    workload: props.item.bug_workload
  }
  dialog.value = true
}

const handleSubmit = async (data: BugUpdate) => {
  try {
    const service_item = new ItemService()
    await service_item.updateBug(data)
    store_item.fetchItems()
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}

const handleDelete = async () => {
  try {
    const service_item = new ItemService()
    await service_item.deleteBug(props.item.rid)
    store_item.fetchItems()
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <v-expand-transition class="panel-detail-expand">
    <div v-show="props.expand">
      <v-row class="panel-detail-expand-row">
        <v-col cols="auto">
          <span class="detail-title">Detail :</span>
        </v-col>

        <v-col>
          <MarkedText :src="props.item.detail" />
        </v-col>

        <v-col cols="auto">
          <span class="detail-title">Result :</span>
        </v-col>

        <v-col>
          <MarkedText :src="props.item.result" />
        </v-col>

        <v-col cols="auto">
          <v-btn size="small" prepend-icon="mdi-pencil" variant="outlined" @click="openDialog()">
            UPDATE
          </v-btn>
        </v-col>
      </v-row>
    </div>
  </v-expand-transition>

  <UpdateBugDialog
    :showDialog="dialog"
    :formData="dialog_form_data"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
    @delete="handleDelete"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
