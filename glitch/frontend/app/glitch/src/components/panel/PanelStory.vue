<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ItemState, type TaskCreate, type BugCreate } from '@/types/Item'
import useItemStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateTaskDialog from '@/components/dialog/CreateTaskDialog.vue'
import CreateBugDialog from '@/components/dialog/CreateBugDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import AccountLabel from '@/components/common/AccountLabel.vue'

const route = useRoute()
const store_item = useItemStore()

const expand = ref(false)
const dialogTask = ref(false)
const dialogBug = ref(false)

const dialogFormDataTask = ref<TaskCreate>({
  rid_items: 0,
  rid_user: 0,
  title: '',
  detail: '',
  type: 0,
  workload: 0,
  number_completed: 0,
  number_total: 0
})

const dialogFormDataBug = ref<BugCreate>({
  rid_items: 0,
  rid_user: 0,
  title: '',
  detail: '',
  workload: 0
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
  story_datetime_start: string
  story_datetime_end: string
}>()

const openTaskDialog = () => {
  const rid_items = props.rid
  dialogFormDataTask.value = { ...dialogFormDataTask.value, rid_items }
  dialogTask.value = true
}

const openBugDialog = () => {
  const rid_items = props.rid
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
  <div class="d-flex flex-column ma-0 py-2 pl-11">
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

<style scoped></style>
