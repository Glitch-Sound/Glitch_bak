<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getUsers } from '@/services/UserService'
import type { User } from '@/types/User'
import PanelTask from '@/components/PanelTask.vue'

const users_manager = ref<User[]>([])
const users_member = ref<User[]>([])

onMounted(async () => {
  try {
    const users = await getUsers()
    users_manager.value = users.filter((user) => user.is_admin == true)
    users_member.value = users.filter((user) => user.is_admin == false)
  } catch (err) {
    console.error('Error fetching users:', err)
  }
})

const dialog = ref(false)
</script>

<template>
  <v-main>
    <v-container>
      <div>
        Manager
        <v-btn icon size="x-small" @click="dialog = true">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="0 < users_manager.length">
          <li v-for="user in users_manager" :key="user.rid">
            {{ user.rid }}, {{ user.name }}, {{ user.name_display }}
          </li>
        </ul>
      </div>
    </v-container>

    <v-dialog v-model="dialog" max-width="600">
      <v-card title="Add Manager">
        <v-card-text> aaa </v-card-text>

        <v-divider />

        <v-card-actions>
          <v-spacer />
          <v-btn text="Close" variant="plain" @click="dialog = false" />
          <v-btn color="primary" text="Save" variant="tonal" @click="dialog = false" />
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-container>
      <div>
        Member
        <v-btn icon size="x-small">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="0 < users_member.length">
          <li v-for="user in users_member" :key="user.rid">
            {{ user.rid }}, {{ user.name }}, {{ user.name_display }}
          </li>
        </ul>
      </div>
    </v-container>
  </v-main>
</template>

<style scoped></style>
