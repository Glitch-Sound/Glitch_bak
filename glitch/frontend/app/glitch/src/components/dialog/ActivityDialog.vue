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
    <v-card>
      <v-card-title>
        <span class="text-h5">Activity</span>
      </v-card-title>

      <v-card-text>
        <div>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</div>

        <v-form>
          <v-text-field />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn>Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
@import '@/components/dialog/dialog.css';
</style>
