<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemType, ItemState } from '@/types/Item'
import ActivityDialog from '@/components/dialog/ActivityDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationBug from '@/components/panel/InformationBug.vue'
import DetailBug from '@/components/panel/DetailBug.vue'

const expand = ref(false)
const dialog = ref(false)

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
        <InformationBug :risk="props.risk" :bug_workload="props.bug_workload" />
      </v-col>

      <v-col cols="auto">
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <DetailBug
      :expand="expand"
      :risk="props.risk"
      :risk_factors="props.risk_factors"
      :detail="props.detail"
      :result="props.result"
    />
  </div>

  <ActivityDialog :showDialog="dialog" />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
