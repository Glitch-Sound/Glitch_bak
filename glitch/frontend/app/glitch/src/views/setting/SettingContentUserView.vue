<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

import type { UserCreate } from '@/types/User'
import useUserStore from '@/stores/UserStore'
import UserService from '@/services/UserService'
import CreateUserDialog from '@/components/dialog/CreateUserDialog.vue'

const headers = [
  { title: 'RID', key: 'rid', width: '50px' },
  { title: 'USER', key: 'user', width: '200px' },
  { title: 'NAME', key: 'name', width: '200px' },
  { title: '', key: '', width: '140px' }
]

const store_user = useUserStore()

const dialog_entry = ref(false)
const dialog_update = ref(false)

const dialogFormData = ref<UserCreate>({
  user: '',
  password: '',
  name: '',
  is_admin: false
})

onMounted(() => {
  store_user.fetchUsers()
})

const users_manager = computed(() => {
  return store_user.users.filter((user) => user.is_admin == true)
})

const users_member = computed(() => {
  return store_user.users.filter((user) => user.is_admin == false)
})

const openEntryDialog = (is_admin: boolean) => {
  dialogFormData.value.is_admin = is_admin
  dialog_entry.value = true
}

const openUpdateDialog = () => {
  dialog_update.value = true
}

const handleSubmit = async (data: UserCreate) => {
  try {
    const service_user = new UserService()
    await service_user.createUser(data)
    store_user.fetchUsers()
    dialog_entry.value = false
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
          <v-btn icon size="x-small" @click="openEntryDialog(true)">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="users_manager"></v-data-table>
      </v-container>

      <v-container class="mb-5">
        <div class="text-h6">
          Member
          <v-btn icon size="x-small" @click="openEntryDialog(false)">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="users_member" :headers="headers">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.rid }}</td>
              <td>{{ item.user }}</td>
              <td>{{ item.name }}</td>
              <td>
                <v-btn
                  size="small"
                  prepend-icon="mdi-pencil"
                  variant="outlined"
                  @click="openUpdateDialog()"
                >
                  UPDATE
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-container>
    </v-sheet>
  </v-main>

  <CreateUserDialog
    :showDialog="dialog_entry"
    :formData="dialogFormData"
    @update:showDialog="dialog_entry = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
.data-table {
  width: 1000px;
}
</style>
