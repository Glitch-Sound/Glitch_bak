<script setup lang="ts">
import Identicon from 'identicon.js'
import * as CryptoJS from 'crypto-js'

import { defineProps, computed } from 'vue'

const props = defineProps({
  rid_users: Number,
  name: String
})

const hash = computed(() => {
  return CryptoJS.MD5(props.rid_users + props.name || '').toString()
})

const identiconDataUri = computed(() => {
  const options = {
    background: [255, 255, 255, 0],
    format: 'svg'
  }
  return 'data:image/svg+xml;base64,' + new Identicon(hash.value, options).toString()
})
</script>

<template>
  <span class="mr-1 username">
    {{ props.name }}
  </span>

  <v-btn icon size="small">
    <img :src="identiconDataUri" width="25" height="25" />
  </v-btn>
</template>

<style scoped>
.username {
  font-size: 18px;
}
</style>
