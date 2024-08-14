<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemType, ItemState } from '@/types/Item'
import ActivityDialog from '@/components/dialog/ActivityDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import AccountLabel from '@/components/common/AccountLabel.vue'

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
  bug_priority: number
  bug_workload: number
}>()

const openDialog = () => {
  dialog.value = true
}
</script>

<template>
  <div class="panel-common panel-bug">
    <v-row class="align-baseline">
      <v-col cols="auto">
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

      <v-col cols="auto"> information </v-col>

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
