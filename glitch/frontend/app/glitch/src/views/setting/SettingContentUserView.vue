<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

import type { UserCreate } from '@/types/User'
import useUserStore from '@/stores/UserStore'
import UserService from '@/services/UserService'
import CreateUserDialog from '@/components/dialog/CreateUserDialog.vue'

const store_user = useUserStore()

const dialog = ref(false)

const dialogFormData = ref<UserCreate>({
  user: '',
  password: '',
  name: '',
  is_admin: false
})

const headers = [
  { title: 'RID', key: 'rid', width: '50px' },
  { title: 'USER', key: 'user', width: '150px' },
  { title: 'NAME', key: 'name', width: '150px' },
  { title: 'ADMIN', key: 'is_admin', width: '100px' }
]

onMounted(() => {
  store_user.fetchUsers()
})

const users_manager = computed(() => {
  return store_user.users.filter((user) => user.is_admin == true)
})

const users_member = computed(() => {
  return store_user.users.filter((user) => user.is_admin == false)
})

const openDialog = (is_admin: boolean) => {
  dialogFormData.value.is_admin = is_admin
  dialog.value = true
}

const handleSubmit = async (data: UserCreate) => {
  try {
    const service_user = new UserService()
    await service_user.createUser(data)
    store_user.fetchUsers()
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <v-main>
    <v-sheet class="mt-1 ml-1 pa-1 rounded-lg">
      <v-container class="mb-5">
        <div class="text-h6">
          Manager
          <v-btn icon size="x-small" @click="openDialog(true)">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="users_manager"></v-data-table>
      </v-container>

      <v-container class="mb-5">
        <div class="text-h6">
          Member
          <v-btn icon size="x-small" @click="openDialog(false)">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="users_member" :headers="headers">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.rid }}</td>
              <td>{{ item.user }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.is_admin }}</td>
            </tr>
          </template>
        </v-data-table>
      </v-container>
    </v-sheet>
  </v-main>

  <CreateUserDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
.data-table {
  width: 1000px;
}
</style>
