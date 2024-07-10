<script setup lang="ts">
import { ref, defineProps, computed } from 'vue'

const expand = ref(false)

const props = defineProps({
  baseDiv: String
})

const classBaseDiv = computed(() => ({
  'd-flex': true,
  'flex-column': true,
  'ma-0': true,
  [`${props.baseDiv}`]: true
}))
</script>

<template>
  <!-- <div class="d-flex flex-column"> -->
  <div :class="classBaseDiv">
    <div class="d-flex flex-row align-baseline">
      <div>1234</div>

      <div>&nbsp;■&nbsp;</div>

      <div @click="expand = !expand"><slot name="title" /></div>

      <v-spacer></v-spacer>

      hogehoge
      <v-btn icon size="x-small">
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <div>&nbsp;information&nbsp;</div>

      <v-btn icon size="x-small">
        <v-icon>mdi-plus-thick</v-icon>
      </v-btn>
    </div>
    <v-expand-transition>
      <div v-show="expand">
        detail<br />
        detail<br />
        detail<br />

        <v-btn icon size="x-small">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>

        <v-btn icon size="x-small">
          <v-icon>mdi-comment-plus-outline</v-icon>
        </v-btn>
      </div>
    </v-expand-transition>
  </div>
</template>

<style scoped></style>
