<script setup lang="ts">
import HeaderView from '@/views/HeaderView.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <v-app>
    <HeaderView />
    <RouterView />
  </v-app>
</template>

<style scoped></style>
