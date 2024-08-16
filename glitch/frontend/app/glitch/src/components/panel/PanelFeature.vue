<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ItemState, type StoryCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateStoryDialog from '@/components/dialog/CreateStoryDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationFeature from '@/components/panel/InformationFeature.vue'
import DetailFeature from '@/components/panel/DetailFeature.vue'

const props = defineProps<{
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
}>()

const route = useRoute()
const store_item = useItemStore()

const expand = ref(false)
const dialog = ref(false)

const dialogFormData = ref<StoryCreate>({
  rid_items: 0,
  rid_user: 0,
  title: '',
  detail: '',
  datetime_start: '',
  datetime_end: ''
})

const openDialog = () => {
  const rid_items = props.rid
  dialogFormData.value = { ...dialogFormData.value, rid_items }
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
  <div class="panel-common panel-feature">
    <v-row class="align-baseline">
      <v-col cols="auto" class="state">
        <TypeLabel :type="props.type" />
      </v-col>

      <v-col cols="auto">
        <StateLabel :state="props.state" />
      </v-col>

      <v-col>
        <span class="title" @click="expand = !expand">{{ props.title }}</span>
      </v-col>

      <v-col cols="auto">
        <UserLabel :rid_users="props.rid_users" :name="props.name" />
      </v-col>

      <v-col cols="auto" class="information">
        <InformationFeature />
      </v-col>

      <v-col cols="auto">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-plus-thick</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <DetailFeature
      :expand="expand"
      :risk="props.risk"
      :risk_factors="props.risk_factors"
      :detail="props.detail"
      :result="props.result"
    />
  </div>

  <CreateStoryDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
