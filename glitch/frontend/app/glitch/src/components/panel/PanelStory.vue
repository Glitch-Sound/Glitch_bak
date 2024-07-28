<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { ItemState } from '@/types/Item'

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
  story_datetime_start: String,
  story_datetime_end: String
})

const expand = ref(false)
</script>

<template>
  <div class="d-flex flex-column ma-0 pl-10">
    <div class="d-flex flex-row align-baseline">
      <div>ID[{{ props.rid }}]</div>

      <div>RISK[{{ props.risk }}]</div>

      <div>STATE[{{ props.state }}]</div>

      <div @click="expand = !expand">TITLE[{{ props.title }}]</div>

      <v-spacer></v-spacer>

      {{ props.name }}
      <v-btn icon size="x-small">
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <div>&nbsp;information&nbsp;</div>

      <v-btn icon size="x-small">
        <v-icon>mdi-plus-thick</v-icon>
      </v-btn>
    </div>
    <v-expand-transition>
      <div v-show="expand">
        Detail : {{ props.detail }}

        <v-btn icon size="x-small">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>

        <v-btn icon size="x-small">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
      </div>
    </v-expand-transition>
  </div>
</template>

<style scoped></style>
