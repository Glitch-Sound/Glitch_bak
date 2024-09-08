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
    <v-sheet class="main">
      <v-container class="block">
        <div class="title">Release</div>
        <div class="detail">…</div>
      </v-container>

      <v-container class="block">
        <div class="title">How to use</div>
        <div class="detail">…</div>
      </v-container>

      <v-container class="block">
        <div class="title">Bug & Request</div>
        <div class="detail">…</div>
      </v-container>
    </v-sheet>

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
.main {
  max-width: 1200px;
  margin: auto;
  display: flex;
  flex-direction: column;
}

.block {
  margin-bottom: 10px;
}

.title {
  font-size: 24px;
  color: #f0f0f0;
}

.detail {
  margin: 10px 20px;
  font-size: 18px;
  color: #dedede;
}
</style>
