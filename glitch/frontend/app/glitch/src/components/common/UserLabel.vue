<script setup lang="ts">
import Identicon from 'identicon.js'
import * as CryptoJS from 'crypto-js'

import { defineProps, computed } from 'vue'

import { ItemState, type Item } from '@/types/Item'

const props = defineProps<{
  item: Item
}>()

const hash_user = computed(() => {
  return CryptoJS.MD5(props.item.rid_users + props.item.name || '').toString()
})

const hash_user_review = computed(() => {
  if (props.item.rid_users_review && props.item.name_review) {
    return CryptoJS.MD5(props.item.rid_users_review + props.item.name_review || '').toString()
  } else {
    return ''
  }
})

const identicon_user = computed(() => {
  const options = {
    background: [255, 255, 255, 0] as [number, number, number, number],
    format: 'svg' as 'svg'
  }
  return 'data:image/svg+xml;base64,' + new Identicon(hash_user.value, options).toString()
})

const identicon_user_review = computed(() => {
  const options = {
    background: [255, 255, 255, 0] as [number, number, number, number],
    format: 'svg' as 'svg'
  }
  return 'data:image/svg+xml;base64,' + new Identicon(hash_user_review.value, options).toString()
})
</script>

<template>
  <span class="mr-1"> {{ props.item.name }} </span>

  <v-btn icon size="x-small">
    <img :src="identicon_user" width="20" height="20" />
  </v-btn>

  <v-btn icon size="x-small" v-if="props.item.state == ItemState.REVIEW">
    <img :src="identicon_user_review" width="20" height="20" />

    <v-tooltip activator="parent">Review : {{ props.item.name_review }}</v-tooltip>
  </v-btn>
  <span v-else class="mr-8" />
</template>

<style scoped></style>
