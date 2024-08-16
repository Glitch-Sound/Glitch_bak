<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemType, ItemState, type EventUpdate } from '@/types/Item'
import UpdateEventDialog from '@/components/dialog/UpdateEventDialog.vue'

import MarkedText from '@/components/common/MarkedText.vue'

const props = defineProps<{
  expand: boolean
  rid: number
  type: ItemType
  state: ItemState
  risk: number
  risk_factors: number
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

const dialog = ref(false)

const dialogFormData = ref<EventUpdate>({
  rid: 0,
  state: 0,
  rid_user: 0,
  rid_users_review: null,
  title: '',
  detail: '',
  result: '',
  datetime_end: ''
})

const openDialog = () => {
  dialogFormData.value = {
    rid: props.rid,
    state: props.state,
    rid_user: props.rid_users,
    rid_users_review: props.rid_users_review,
    title: props.title,
    detail: props.detail,
    result: props.result,
    datetime_end: props.event_datetime_end
  }

  dialog.value = true
}

const handleSubmit = async (data: EventUpdate) => {
  try {
    console.log(data)
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
          <MarkedText :src="props.detail" />
        </v-col>

        <v-col cols="auto">
          <span class="detail-title">Result :</span>
        </v-col>

        <v-col>
          <MarkedText :src="props.result" />
        </v-col>

        <v-col cols="auto">
          <v-btn size="small" prepend-icon="mdi-pencil" variant="outlined" @click="openDialog()">
            UPDATE
          </v-btn>
        </v-col>
      </v-row>
    </div>
  </v-expand-transition>

  <UpdateEventDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
