<script setup lang="ts">
import { ref, onMounted } from 'vue'

import { type EmitItemSelected } from '@/components/common/events'

const tickLabels: { [value: number]: string } = {
  1: 'Within an hour',
  3: 'Within half a day',
  7: 'Within a day',
  14: 'Within 2 days',
  21: 'Within 3 days',
  35: 'Within a week'
}
const customSteps = Object.keys(tickLabels).map((key) => Number(key))

const sliderValue = ref(1)

const emit = defineEmits<EmitItemSelected>()
onMounted(() => {
  emit('itemSelected', sliderValue.value)
})

const emitSelected = () => {
  emit('itemSelected', sliderValue.value)
}

const color = () => {
  let value = ''
  switch (sliderValue.value) {
    case 1:
      value = '#28a745'
      break
    case 3:
      value = '#3ea956'
      break
    case 7:
      value = '#74c77c'
      break
    case 14:
      value = '#c1d982'
      break
    case 21:
      value = '#e8a44d'
      break
    case 35:
      value = '#bd533f'
      break
  }
  return value
}

const onSliderInput = (value: number) => {
  const closestStep = customSteps.reduce((prev, curr) => {
    return Math.abs(curr - value) < Math.abs(prev - value) ? curr : prev
  })
  sliderValue.value = closestStep
}
</script>

<template>
  <div class="d-flex flex-row justify-center mt-10">
    <p class="slider">
      <v-slider
        v-model="sliderValue"
        :min="0"
        :max="36"
        :ticks="customSteps"
        :color="color()"
        @update:modelValue="onSliderInput"
        @end="emitSelected"
        show-ticks="always"
      />
    </p>
    <p class="value" :style="{ color: color() }">
      {{ tickLabels[sliderValue] }}
    </p>
  </div>
</template>

<style scoped>
.slider {
  width: 600px;
}

.value {
  width: 200px;
  margin: 0 0 0 20px;
  font-weight: bold;
}
</style>
