<script setup lang="ts">
import { ref, defineProps } from 'vue'

import { ItemType, ItemState } from '@/types/Item'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import AccountLabel from '@/components/common/AccountLabel.vue'

const expand = ref(false)
const dialog = ref(false)

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
  bug_priority: Number,
  bug_workload: Number
})

const openDialog = () => {
  dialog.value = true
}
</script>

<template>
  <div class="d-flex flex-column ma-0 pl-15">
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
        <v-btn icon size="x-small" @click="openDialog()">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
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

  <v-dialog v-model="dialog" width="auto">
    <v-card max-width="1000" title="Activity" text="・・・・・・・・・・・・・・・・・・・・・">
      <template v-slot:actions>
        <v-btn class="ms-auto" text="Ok" @click="dialog = false"></v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
