<script setup lang="ts">
import { ref, defineProps } from 'vue'

import type { Item, StoryUpdate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import SummaryItem from '@/components/panel/SummaryItem.vue'
import UpdateStoryDialog from '@/components/dialog/UpdateStoryDialog.vue'

import MarkedText from '@/components/common/MarkedText.vue'

const props = defineProps<{
  expand: boolean
  item: Item
}>()

const store_item = useItemStore()

const dialog = ref(false)

const dialog_form_data = ref<StoryUpdate>({
  rid: 0,
  state: 0,
  rid_users: 0,
  rid_users_review: null,
  title: '',
  detail: '',
  result: '',
  datetime_start: '',
  datetime_end: ''
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
    datetime_start: props.item.story_datetime_start,
    datetime_end: props.item.story_datetime_end
  }
  dialog.value = true
}

const handleSubmit = (data: StoryUpdate) => {
  store_item.updateStory(data)
  dialog.value = false
}

const handleDelete = () => {
  store_item.deleteStory(props.item.rid)
  dialog.value = false
}
</script>

<template>
  <v-expand-transition class="panel-detail-expand">
    <div v-show="props.expand">
      <v-row class="panel-detail-expand-detail">
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

      <v-row class="panel-detail-expand-summary" v-if="props.expand">
        <SummaryItem :item="props.item" />
      </v-row>
    </div>
  </v-expand-transition>

  <UpdateStoryDialog
    :dialog_show="dialog"
    :data_form="dialog_form_data"
    :rid_parent="props.item.rid"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
    @delete="handleDelete"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
