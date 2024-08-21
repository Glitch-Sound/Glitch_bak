<script setup lang="ts">
import { ref, defineProps } from 'vue'

import type { Item } from '@/types/Item'
import ActivityDialog from '@/components/dialog/ActivityDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationBug from '@/components/panel/InformationBug.vue'
import DetailBug from '@/components/panel/DetailBug.vue'

const props = defineProps<{
  item: Item
}>()

const expand = ref(false)
const dialog = ref(false)

const openDialog = () => {
  dialog.value = true
}
</script>

<template>
  <div class="panel-common panel-bug">
    <v-row class="align-baseline">
      <v-col class="type" cols="auto">
        <TypeLabel :item="props.item" />
      </v-col>

      <v-col class="state" cols="auto">
        <StateLabel :state="props.item.state" />
      </v-col>

      <v-col class="title" @click="expand = !expand">
        {{ props.item.title }}
      </v-col>

      <v-col cols="auto">
        <UserLabel :rid_users="props.item.rid_users" :name="props.item.name" />
      </v-col>

      <v-col class="information" cols="auto">
        <InformationBug :item="props.item" />
      </v-col>

      <v-col cols="auto">
        <v-btn icon variant="text" size="x-small" @click="openDialog()">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <DetailBug v-bind="{ ...props, expand }" />
  </div>

  <ActivityDialog :showDialog="dialog" />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
