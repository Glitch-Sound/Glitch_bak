<script setup lang="ts">
import { ref, onMounted } from 'vue'

import type { ProjectCreate } from '@/types/Item'
import useProjectStore from '@/stores/ProjectStore'
import ItemService from '@/services/ItemService'
import MarkedText from '@/components/common/MarkedText.vue'
import CreateProjectDialog from '@/components/dialog/CreateProjectDialog.vue'

const headers = [
  { title: 'RID', key: 'rid', width: '50px' },
  { title: 'STATE', key: 'state', width: '50px' },
  { title: 'TITLE', key: 'title' },
  { title: 'DETAIL', key: 'detail' },
  { title: 'RESULT', key: 'result' },
  { title: 'ENTRY', key: 'datetime_entry', width: '300px' },
  { title: 'USER', key: 'name', width: '100px' }
]

const store_project = useProjectStore()

const dialog = ref(false)

const dialogFormData = ref<ProjectCreate>({
  rid_user: 0,
  title: '',
  detail: '',
  datetime_start: '',
  datetime_end: ''
})

onMounted(() => {
  store_project.fetchProjects()
})

const openDialog = () => {
  dialog.value = true
}

const handleSubmit = async (data: ProjectCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createProject(data)
    store_project.fetchProjects()
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
          Projects
          <v-btn icon size="x-small" @click="openDialog()">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="store_project.projects" :headers="headers">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.rid }}</td>
              <td>{{ item.state }}</td>
              <td>{{ item.title }}</td>
              <td><MarkedText :src="item.detail" /></td>
              <td><MarkedText :src="item.result" /></td>
              <td>{{ item.datetime_entry }}</td>
              <td>{{ item.name }}</td>
            </tr>
          </template>
        </v-data-table>
      </v-container>
    </v-sheet>
  </v-main>

  <CreateProjectDialog
    :showDialog="dialog"
    :formData="dialogFormData"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped></style>
