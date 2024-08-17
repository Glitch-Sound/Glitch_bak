<script setup lang="ts">
import { ref, defineProps, onMounted } from 'vue'

import { ItemType, ItemState } from '@/types/Item'
import StateLabelLarge from '@/components/common/StateLabelLarge.vue'
import { type EmitItemSelected } from '@/components/common/events'

const props = defineProps<{
  type: ItemType
  state: ItemState
}>()

const selectedState = ref(ItemState.NONE)
const selectedStateSrc = ref(ItemState.NONE)

onMounted(() => {
  selectedStateSrc.value = props.state
})

const emit = defineEmits<EmitItemSelected>()
const emitSelected = () => {
  emit('itemSelected', selectedState.value)
}
</script>

<template>
  <div class="d-flex justify-center">
    <v-chip-group
      v-model="selectedState"
      v-if="selectedStateSrc === ItemState.IDLE"
      @update:modelValue="emitSelected"
    >
      <StateLabelLarge :state="ItemState.IDLE" />
      <StateLabelLarge :state="ItemState.RUN" />
    </v-chip-group>

    <v-chip-group
      v-model="selectedState"
      v-if="selectedStateSrc === ItemState.RUN"
      @update:modelValue="emitSelected"
    >
      <StateLabelLarge :state="ItemState.RUN" />
      <StateLabelLarge :state="ItemState.ALERT" />
      <StateLabelLarge :state="ItemState.REVIEW" />
      <StateLabelLarge :state="ItemState.COMPLETE" />
    </v-chip-group>

    <v-chip-group
      v-model="selectedState"
      v-if="selectedStateSrc === ItemState.ALERT"
      @update:modelValue="emitSelected"
    >
      <StateLabelLarge :state="ItemState.ALERT" />
      <StateLabelLarge :state="ItemState.RUN" />
      <StateLabelLarge :state="ItemState.REVIEW" />
    </v-chip-group>

    <v-chip-group
      v-model="selectedState"
      v-if="selectedStateSrc === ItemState.REVIEW"
      @update:modelValue="emitSelected"
    >
      <StateLabelLarge :state="ItemState.REVIEW" />
      <StateLabelLarge :state="ItemState.RUN" />
      <StateLabelLarge :state="ItemState.ALERT" />
    </v-chip-group>

    <v-chip-group
      v-model="selectedState"
      v-if="selectedStateSrc === ItemState.COMPLETE"
      @update:modelValue="emitSelected"
    >
      <StateLabelLarge :state="ItemState.COMPLETE" />
      <StateLabelLarge :state="ItemState.RUN" />
      <StateLabelLarge :state="ItemState.ALERT" />
    </v-chip-group>
  </div>
</template>

<style scoped>
.v-chip-group {
  margin: 0 0 15px 0;
}
</style>
