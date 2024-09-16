<script setup lang="ts">
import { ref, defineProps, watch } from 'vue'

import useItemStore from '@/stores/ItemStore'
import type { EmitDialog } from '@/components/common/events'

const props = defineProps<{
  dialog_show: boolean
}>()

const store_item = useItemStore()

const emits = defineEmits<EmitDialog>()

const dialog = ref(props.dialog_show)
const target = ref('')

watch(
  () => props.dialog_show,
  (value_new) => {
    dialog.value = value_new
  }
)

watch(dialog, (value_new) => {
  emits('update:showDialog', value_new)
})

const search = () => {
  store_item.setExtractSearch(target.value)
  dialog.value = false
}
</script>

<template>
  <v-dialog v-model="dialog" class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Search</span>
      </v-card-title>

      <v-card-text>
        <v-form>
          <v-text-field v-model="target" label="Target" required />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn color="primary" @click="search">Search</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
@import '@/components/dialog/dialog.css';
</style>
