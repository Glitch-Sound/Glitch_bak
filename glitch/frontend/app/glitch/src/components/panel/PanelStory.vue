<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import type { Item, TaskCreate, BugCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateTaskDialog from '@/components/dialog/CreateTaskDialog.vue'
import CreateBugDialog from '@/components/dialog/CreateBugDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationStory from '@/components/panel/InformationStory.vue'
import DetailStory from '@/components/panel/DetailStory.vue'

const props = defineProps<{
  item: Item
}>()

const route = useRoute()
const store_item = useItemStore()

const expand = ref(false)
const dialogTask = ref(false)
const dialogBug = ref(false)

const dialogFormDataTask = ref<TaskCreate>({
  rid_items: 0,
  rid_users: 0,
  title: '',
  detail: '',
  type: 0,
  workload: 0,
  number_completed: 0,
  number_total: 0
})

const dialogFormDataBug = ref<BugCreate>({
  rid_items: 0,
  rid_users: 0,
  title: '',
  detail: '',
  workload: 0
})

const openTaskDialog = () => {
  const rid_items = props.item.rid
  dialogFormDataTask.value = { ...dialogFormDataTask.value, rid_items }
  dialogTask.value = true
}

const openBugDialog = () => {
  const rid_items = props.item.rid
  dialogFormDataBug.value = { ...dialogFormDataBug.value, rid_items }
  dialogBug.value = true
}

const handleTaskSubmit = async (data: TaskCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createTask(data)
    store_item.fetchItems(Number(route.params.rid))
    dialogTask.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}

const handleBugSubmit = async (data: BugCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createBug(data)
    store_item.fetchItems(Number(route.params.rid))
    dialogBug.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <div class="panel-common panel-story">
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
        <InformationStory :item="props.item" />
      </v-col>

      <v-col cols="auto">
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn icon size="x-small" v-bind="props">
              <v-icon>mdi-plus-thick</v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item-title
              ><v-btn prepend-icon="mdi-label" @click="openTaskDialog()">Task</v-btn>
            </v-list-item-title>
            <v-list-item-title
              ><v-btn prepend-icon="mdi-spider" @click="openBugDialog()">Bug</v-btn>
            </v-list-item-title>
          </v-list>
        </v-menu>
      </v-col>
    </v-row>

    <DetailStory v-bind="{ ...props, expand }" />
  </div>

  <CreateTaskDialog
    :showDialog="dialogTask"
    :formData="dialogFormDataTask"
    @update:showDialog="dialogTask = $event"
    @submit="handleTaskSubmit"
  />

  <CreateBugDialog
    :showDialog="dialogBug"
    :formData="dialogFormDataBug"
    @update:showDialog="dialogBug = $event"
    @submit="handleBugSubmit"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
