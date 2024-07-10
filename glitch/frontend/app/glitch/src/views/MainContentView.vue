<script setup lang="ts">
import PanelEvent from '@/components/PanelEvent.vue'
import PanelFeature from '@/components/PanelFeature.vue'
import PanelStory from '@/components/PanelStory.vue'
import PanelTask from '@/components/PanelTask.vue'
</script>

<template>
  <v-main>
    <v-sheet>
      <PanelEvent />
      <PanelFeature />
      <PanelStory />
      <PanelTask />
    </v-sheet>
  </v-main>
</template>

<style scoped></style>
