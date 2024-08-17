<script setup lang="ts">
import { ref, defineProps, watch } from 'vue'

const props = defineProps<{
  showDialog: boolean
}>()

const dialog = ref(props.showDialog)

watch(
  () => props.showDialog,
  (new_value) => {
    dialog.value = new_value
  }
)
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card
      max-width="400"
      prepend-icon="mdi-update"
      text="Your application will relaunch automatically after the update is complete."
      title="Update in progress"
    >
      <template v-slot:actions>
        <v-btn class="ms-auto" text="Ok" @click="dialog = false"></v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<style scoped>
@import '@/components/dialog/dialog.css';
</style>
