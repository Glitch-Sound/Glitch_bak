<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemType, ItemState, TaskType } from '@/types/Item'
import ActivityDialog from '@/components/dialog/ActivityDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import AccountLabel from '@/components/common/AccountLabel.vue'
import InformationTask from '@/components/panel/InformationTask.vue'

const expand = ref(false)
const dialog = ref(false)

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
  task_priority: number
  task_type: TaskType
  task_workload: number
  task_number_completed: number
  task_number_total: number
}>()

const openDialog = () => {
  dialog.value = true
}
</script>

<template>
  <div class="panel-common panel-task">
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
        <AccountLabel :rid_users="props.rid_users" :name="props.name" />
      </v-col>

      <v-col cols="auto" class="information">
        <InformationTask
          :risk="props.risk"
          :task_type="props.task_type"
          :task_workload="props.task_workload"
          :task_number_completed="props.task_number_completed"
          :task_number_total="props.task_number_total"
        />
      </v-col>

      <v-col cols="auto">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <v-expand-transition class="panel-detail-expand">
      <div v-show="expand">
        <v-row class="panel-detail-expand-row">
          <v-col cols="auto">
            <span>Detail :</span>
          </v-col>

          <v-col>
            <span>{{ props.detail }}</span>
          </v-col>

          <v-col cols="auto">
            <span>Result :</span>
          </v-col>

          <v-col>
            <span>{{ props.result }}</span>
          </v-col>

          <v-col cols="auto">
            <v-btn size="small" prepend-icon="mdi-pencil" variant="outlined">UPDATE</v-btn>
          </v-col>
        </v-row>
      </div>
    </v-expand-transition>
  </div>

  <ActivityDialog :showDialog="dialog" />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
