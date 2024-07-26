<script setup lang="ts">
import PanelEvent from '@/components/panel/PanelEvent.vue'
import PanelFeature from '@/components/panel/PanelFeature.vue'
import PanelStory from '@/components/panel/PanelStory.vue'
import PanelTask from '@/components/panel/PanelTask.vue'
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
