<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import type { Item, FeatureCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateFeatureDialog from '@/components/dialog/CreateFeatureDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationEvent from '@/components/panel/InformationEvent.vue'
import DetailEvent from '@/components/panel/DetailEvent.vue'

const props = defineProps<{
  item: Item
}>()

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

const openDialog = () => {
  const rid_items = props.item.rid
  dialogFormData.value = { ...dialogFormData.value, rid_items }
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
  <div class="panel-common panel-event">
    <v-row class="align-baseline">
      <v-col cols="auto" class="state">
        <TypeLabel :type="props.item.type" />
      </v-col>

      <v-col cols="auto">
        <StateLabel :state="props.item.state" />
      </v-col>

      <v-col @click="expand = !expand">
        <span class="title">{{ props.item.title }}</span>
      </v-col>

      <v-col cols="auto">
        <UserLabel :rid_users="props.item.rid_users" :name="props.item.name" />
      </v-col>

      <v-col cols="auto" class="information">
        <InformationEvent :item="props.item" />
      </v-col>

      <v-col cols="auto">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-plus-thick</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <DetailEvent v-bind="{ ...props, expand }" />
  </div>

  <CreateFeatureDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
