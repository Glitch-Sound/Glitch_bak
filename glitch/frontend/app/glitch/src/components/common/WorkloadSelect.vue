<script setup lang="ts">
import { ref, onMounted } from 'vue'

const tickLabels: { [value: number]: string } = {
  1: 'Within an hour',
  3: 'Within half a day',
  7: 'Within a day',
  14: 'Within 2 days',
  21: 'Within 3 days',
  35: 'Within a week'
}
const customSteps = [1, 3, 7, 14, 21, 35]

const sliderValue = ref(1)

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
      value = '#dc3545'
      break
  }
  return value
}

const emit = defineEmits<{
  (e: 'valueSelected', value: any): void
}>()

const onSliderInput = (value: number) => {
  const closestStep = customSteps.reduce((prev, curr) => {
    return Math.abs(curr - value) < Math.abs(prev - value) ? curr : prev
  })
  sliderValue.value = closestStep
}

const emitSelected = () => {
  emit('valueSelected', sliderValue.value)
}

onMounted(() => {
  emit('valueSelected', sliderValue.value)
})
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
    <p class="value">{{ tickLabels[sliderValue] }}</p>
  </div>
</template>

<style scoped>
.slider {
  width: 600px;
}

.value {
  width: 200px;
  margin: 0 0 0 20px;
}
</style>
