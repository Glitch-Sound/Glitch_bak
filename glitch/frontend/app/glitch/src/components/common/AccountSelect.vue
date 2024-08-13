<script setup lang="ts">
import { ref, onMounted } from 'vue'

import useUserStore from '@/stores/UserStore'

const store_user = useUserStore()

const selectedOption = ref<number | null>(null)
const options = ref<{ name: string; rid: number }[]>([])

const emit = defineEmits<{
  (e: 'itemSelected', selectedItem: any): void
}>()

onMounted(() => {
  store_user.fetchUsers()
})

const emitSelected = () => {
  const selectedItem = options.value.find((item) => item.rid === selectedOption.value)
  if (selectedItem) {
    emit('itemSelected', selectedItem)
  }
}
</script>

<template>
  <v-select
    :items="store_user.users"
    v-model="selectedOption"
    label="User"
    item-title="name"
    item-value="rid"
    required
    @change="emitSelected"
  ></v-select>
</template>

<style scoped></style>
