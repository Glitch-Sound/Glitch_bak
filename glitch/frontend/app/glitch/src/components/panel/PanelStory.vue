<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import { ItemType, ItemState, TaskCreate } from '@/types/Item'
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
  story_datetime_start: String,
  story_datetime_end: String,
  story_workload: Number,
  story_number_completed: Number,
  story_number_total: Number
})

const openTaskDialog = () => {
  const rid_items = props.rid
  dialogFormData.value = { rid_items }
  dialogTask.value = true
}

const openBugDialog = () => {
  const rid_items = props.rid
  dialogFormData.value = { rid_items }
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
  <div class="d-flex flex-column ma-0 pl-10">
    <div class="d-flex flex-row align-baseline">
      <p class="mx-1">
        <TypeLabel :type="props.type" />
      </p>

      <p class="mx-1">
        <StateLabel :state="props.state" />
      </p>

      <p class="mx-1 font-weight-bold" @click="expand = !expand">{{ props.title }}</p>

      <v-spacer></v-spacer>

      <p class="mx-1">
        <AccountLabel :rid_users="props.rid_users" :name="props.name"></AccountLabel>
      </p>

      <p class="mx-2">information</p>

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
        Detail : {{ props.detail }}

        <v-btn icon size="x-small">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </div>
    </v-expand-transition>
  </div>

  <CreateTaskDialog
    :showDialog="dialogTask"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleTaskSubmit"
  />

  <CreateBugDialog
    :showDialog="dialogBug"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleBugSubmit"
  />
</template>

<style scoped></style>
