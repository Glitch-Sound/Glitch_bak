<script setup lang="ts">
import { ref } from 'vue'

import { type EmitDelete } from '@/components/common/events'

const isSwitchOn = ref(false)

const emit = defineEmits<EmitDelete>()
const emitSelected = () => {
  emit('delete')
}
</script>

<template>
  <v-row>
    <v-col cols="auto">
      <v-switch :hide-details="true" base-color="#3e3e3e" color="#930000" v-model="isSwitchOn" />
    </v-col>

    <v-col cols="auto">
      <v-btn :disabled="!isSwitchOn" @click="emitSelected">DELETE</v-btn>
    </v-col>
  </v-row>
</template>

<style scoped>
.v-row {
  align-items: center;
}
</style>
