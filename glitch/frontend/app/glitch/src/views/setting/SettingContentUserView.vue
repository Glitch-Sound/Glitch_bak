<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

import type { UserCreate, UserUpdate } from '@/types/User'
import useUserStore from '@/stores/UserStore'
import UserService from '@/services/UserService'
import CreateUserDialog from '@/components/dialog/CreateUserDialog.vue'
import UpdateUserDialog from '@/components/dialog/UpdateUserDialog.vue'

const headers = [
  { title: 'RID', width: '50px' },
  { title: 'USER', width: '200px' },
  { title: 'NAME', width: '200px' },
  { title: '', width: '140px' }
]

const store_user = useUserStore()

const dialog_entry = ref(false)
const dialog_update = ref(false)
const target_delete = ref(0)

const dialog_form_data_entry = ref<UserCreate>({
  user: '',
  password: '',
  name: '',
  is_admin: false
})

const dialog_form_data_update = ref<UserUpdate>({
  rid: 0,
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
  dialog_form_data_entry.value.is_admin = is_admin
  dialog_entry.value = true
}

const openUpdateDialog = (rid: number) => {
  const target = store_user.users.find((item) => item.rid == rid)
  if (!target) {
    return
  }

  dialog_form_data_update.value = {
    rid: target.rid,
    user: target.user,
    password: '',
    name: target.name,
    is_admin: target.is_admin
  }
  target_delete.value = rid
  dialog_update.value = true
}

const handleEntry = async (data: UserCreate) => {
  try {
    const service_user = new UserService()
    await service_user.createUser(data)
    store_user.fetchUsers()
    dialog_entry.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}

const handleUpdate = async (data: UserUpdate) => {
  try {
    const service_user = new UserService()
    await service_user.updateUser(data)
    store_user.fetchUsers()
    dialog_update.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}

const handleDelete = async () => {
  try {
    const service_user = new UserService()
    await service_user.deleteUser(target_delete.value)
    store_user.fetchUsers()
    dialog_update.value = false
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

        <v-data-table class="ml-5 data-table" :items="users_manager" :headers="headers">
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
                  @click="openUpdateDialog(item.rid)"
                >
                  UPDATE
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
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
                  @click="openUpdateDialog(item.rid)"
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
    :formData="dialog_form_data_entry"
    :is_startup="false"
    @update:showDialog="dialog_entry = $event"
    @submit="handleEntry"
  />

  <UpdateUserDialog
    :showDialog="dialog_update"
    :formData="dialog_form_data_update"
    @update:showDialog="dialog_update = $event"
    @submit="handleUpdate"
    @delete="handleDelete"
  />
</template>

<style scoped>
.data-table {
  width: 1000px;
}
</style>
