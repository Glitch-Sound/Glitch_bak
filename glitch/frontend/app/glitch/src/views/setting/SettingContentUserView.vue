<script setup lang="ts">
import { ref, onMounted } from 'vue'
import UserService from '@/services/UserService'
import CreateUserDialog from '@/components/dialog/CreateUserDialog.vue'
import type { User } from '@/types/User'

const users_manager = ref<User[]>([])
const users_member = ref<User[]>([])
const dialog = ref(false)
const dialogFormData = ref({ is_admin: false })

onMounted(async () => {
  try {
    const service_user = new UserService()
    const users = await service_user.getUsers()

    users_manager.value = users.filter((user) => user.is_admin == true)
    users_member.value = users.filter((user) => user.is_admin == false)
  } catch (err) {
    console.error('Error fetching users:', err)
  }
})

const openDialog = (data: { is_admin: Boolean }) => {
  dialogFormData.value = data
  dialog.value = true
}

const handleSubmit = (data: {
  user: string
  password: string
  name: string
  is_admin: Boolean
}) => {
  const service_user = new UserService()
  service_user.createUser({
    user: data.user,
    password: data.password,
    name: data.name,
    is_admin: data.is_admin
  })

  dialog.value = false
}
</script>

<template>
  <v-main>
    <v-container>
      <div>
        Manager
        <v-btn icon size="x-small" @click="openDialog({ is_admin: true })">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="0 < users_manager.length">
          <li v-for="user in users_manager" :key="user.rid">
            {{ user.rid }}, {{ user.user }}, {{ user.name }}, {{ user.is_admin }}
          </li>
        </ul>
      </div>
    </v-container>

    <v-container>
      <div>
        Member
        <v-btn icon size="x-small" @click="openDialog({ is_admin: false })">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="0 < users_member.length">
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
