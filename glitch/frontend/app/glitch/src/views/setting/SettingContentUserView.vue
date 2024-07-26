<script setup lang="ts">
import { ref, onMounted } from 'vue'
import UserService from '@/services/UserService'
import CreateUserDialog from '@/components/dialog/CreateUserDialog.vue'
import type { User, UserCreate } from '@/types/User'

const users_manager = ref<User[]>([])
const users_member = ref<User[]>([])
const dialog = ref(false)
const dialogFormData = ref({ is_admin: false })

const fetchUsers = async () => {
  try {
    const service_user = new UserService()
    const users = await service_user.getUsers()

    users_manager.value = users.filter((user) => user.is_admin)
    users_member.value = users.filter((user) => !user.is_admin)
  } catch (err) {
    console.error('Error fetching users:', err)
  }
}

const openDialog = (is_admin: boolean) => {
  dialogFormData.value = { is_admin }
  dialog.value = true
}

const handleSubmit = async (data: UserCreate) => {
  try {
    const service_user = new UserService()
    await service_user.createUser(data)
    await fetchUsers()
    dialog.value = false
  } catch (err) {
    console.error('Error creating user:', err)
  }
}

onMounted(fetchUsers)
</script>

<template>
  <v-main>
    <v-container>
      <div>
        Manager
        <v-btn icon size="x-small" @click="openDialog(true)">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="users_manager.length">
          <li v-for="user in users_manager" :key="user.rid">
            {{ user.rid }}, {{ user.user }}, {{ user.name }}, {{ user.is_admin }}
          </li>
        </ul>
      </div>
    </v-container>

    <v-container>
      <div>
        Member
        <v-btn icon size="x-small" @click="openDialog(false)">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="users_member.length">
          <li v-for="user in users_member" :key="user.rid">
            {{ user.rid }}, {{ user.user }}, {{ user.name }}, {{ user.is_admin }}
          </li>
        </ul>
      </div>
    </v-container>

    <CreateUserDialog
      :showDialog="dialog"
      :formData="dialogFormData"
      @update:showDialog="dialog = $event"
      @submit="handleSubmit"
    />
  </v-main>
</template>

<style scoped></style>
