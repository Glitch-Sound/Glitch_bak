<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemState, TaskType } from '@/types/Item'
import AccountSimple from '@/components/common/AccountSimple.vue'

const expand = ref(false)

const props = defineProps({
  rid: Number,
  state: ItemState,
  risk: Number,
  title: String,
  detail: String,
  result: String,
  datetime_entry: String,
  datetime_update: String,
  name: String,
  task_priority: Number,
  task_type: TaskType,
  task_workload: Number,
  task_number_completed: Number,
  task_number_total: Number
})
</script>

<template>
  <div class="d-flex flex-column ma-0 pl-15">
    <div class="d-flex flex-row align-baseline">
      <p class="mx-1">{{ props.rid }}</p>
      <p class="mx-1">[{{ props.risk }}]</p>
      <p class="mx-1">state:{{ props.state }}</p>
      <p class="mx-1 font-weight-bold" @click="expand = !expand">{{ props.title }}</p>

      <v-spacer></v-spacer>

      <p class="mx-1">
        <AccountSimple :rid="props.rid" :name="props.name"></AccountSimple>
      </p>

      <p class="mx-2">information</p>

      <p class="mx-1">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
      </p>
    </div>
    <v-expand-transition>
      <div class="ml-1" v-show="expand">
        Detail : {{ props.detail }}

        <v-btn icon size="x-small">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </div>
    </v-expand-transition>
  </div>
</template>

<style scoped></style>
