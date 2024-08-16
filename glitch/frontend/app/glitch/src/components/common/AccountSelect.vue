<script setup lang="ts">
import { ref, onMounted } from 'vue'

import useUserStore from '@/stores/UserStore'
import { type EmitEvents } from '@/components/common/events'

const selectedOption = ref<number | null>(null)

const store_user = useUserStore()

onMounted(() => {
  store_user.fetchUsers()
})

const emit = defineEmits<EmitEvents>()
const itemSelected = () => {
  const selectedItem = store_user.users.find((item) => item.rid === selectedOption.value)
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
    @update:modelValue="itemSelected"
  />
</template>

<style scoped></style>
