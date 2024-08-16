<script setup lang="ts">
import { defineProps } from 'vue'

import { marked } from 'marked'

const props = defineProps<{
  src: string
}>()

marked.setOptions({
  breaks: true
})
</script>

<template>
  <span v-html="marked(props.src)" />
</template>

<style scoped></style>
