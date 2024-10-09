<script setup lang="ts">
import { ref, defineProps } from 'vue'

import type { Item } from '@/types/Item'
import ActivityDialog from '@/components/dialog/ActivityDialog.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import FireLabel from '@/components/common/FireLabel.vue'
import TitleLabel from '@/components/common/TitleLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationBug from '@/components/panel/InformationBug.vue'
import DetailBug from '@/components/panel/DetailBug.vue'
import { RISK_LOW } from '@/components/common/common'

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
  <div class="panel-common">
    <v-row class="align-baseline">
      <v-col class="state" cols="auto">
        <StateLabel :state="props.item.state" />
      </v-col>

      <v-col class="type type-bug" cols="auto">
        <TypeLabel :item="props.item" />
      </v-col>

      <v-col class="fire" cols="auto">
        <FireLabel :item="props.item" />
      </v-col>

      <template v-if="props.item.risk < RISK_LOW">
        <v-col class="title-bug" @click="expand = !expand">
          <TitleLabel :item="props.item" />
        </v-col>
      </template>
      <template v-else>
        <v-col class="title-bug-fire" @click="expand = !expand">
          <TitleLabel :item="props.item" />
        </v-col>
      </template>

      <v-col cols="auto">
        <UserLabel :item="props.item" />
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

  <ActivityDialog :item="props.item" :dialog_show="dialog" @update:showDialog="dialog = $event" />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
