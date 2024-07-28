<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
  rid: Number,
  name: String
})
</script>

<template>
  {{ props.name }}
  <v-btn icon size="x-small">
    <v-icon>mdi-account-circle</v-icon>
  </v-btn>
</template>

<style scoped></style>
