<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

import useProjectStore from '@/stores/ProjectStore'
import useProgressStore from '@/stores/ProgressStore'

const route = useRoute()
const router = useRouter()
const store_project = useProjectStore()
const store_progress = useProgressStore()

onMounted(() => {
  if (store_project.selected_id_project) {
    store_progress.fetchUsers(store_project.selected_id_project)
  }
})

const changeTarget = (rid_users: number) => {
  const idProject = route.params.id_project
  router.push(`/progress/${idProject}/${rid_users}`)
  store_progress.setUser(rid_users)
}
</script>

<template>
  <v-navigation-drawer color="background" class="no-border">
    <v-sheet color="#101010" class="rounded-lg mt-1 ml-1 py-3">
      <template v-for="user in store_progress.users" :key="user.rid">
        <v-list-item
          :class="{
            'extract-selected': store_progress.rid_users === user.rid,
            'extract-unselected': store_progress.rid_users !== user.rid
          }"
          @click="changeTarget(user.rid)"
          >{{ user.name }}</v-list-item
        >
      </template>
    </v-sheet>
  </v-navigation-drawer>
</template>

<style scoped>
@import '@/assets/main.css';

.extract-selected {
  border-left: 4px solid #196fb3;
}

.extract-unselected {
  border-left: 4px solid transparent;
}
</style>
