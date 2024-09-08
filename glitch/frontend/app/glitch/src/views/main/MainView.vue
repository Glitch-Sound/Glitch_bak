<script setup lang="ts">
import { ref, onMounted } from 'vue'

import type { UserCreate } from '@/types/User'
import useUserStore from '@/stores/UserStore'
import UserService from '@/services/UserService'
import CreateUserDialog from '@/components/dialog/CreateUserDialog.vue'

const store_user = useUserStore()

const dialog = ref(false)

const dialog_form_data = ref<UserCreate>({
  user: '',
  password: '',
  name: '',
  is_admin: true
})

onMounted(async () => {
  await store_user.fetchUsers()
  if (store_user.users.length === 0) {
    dialog.value = true
  }
})

const handleEntry = async (data: UserCreate) => {
  try {
    const service_user = new UserService()
    const login_user = await service_user.createUser(data)
    store_user.setLoginUser(login_user)
    store_user.fetchUsers()
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <v-main>
    <v-row justify="center" class="mt-13 mx-auto">
      <v-col cols="auto">
        <v-card prepend-icon="mdi-checkbox-multiple-blank-circle" class="card" width="500">
          <template v-slot:title>
            <span class="font-weight-black mx-1">Release</span>
          </template>
          <v-card-text class="px-10 py-3">...</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto">
        <v-card prepend-icon="mdi-help" class="card" width="500">
          <template v-slot:title>
            <span class="font-weight-black mx-1">How to use</span>
          </template>
          <v-card-text class="px-10 py-3">...</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto">
        <v-card prepend-icon="mdi-spider" class="card" width="500">
          <template v-slot:title>
            <span class="font-weight-black mx-1">Bug & Request</span>
          </template>
          <v-card-text class="px-10 py-3">...</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <CreateUserDialog
      :dialog_show="dialog"
      :data_form="dialog_form_data"
      :is_startup="true"
      @update:showDialog="dialog = $event"
      @submit="handleEntry"
    />
  </v-main>
</template>

<style scoped>
.card {
  background-color: #000000;
}
</style>
