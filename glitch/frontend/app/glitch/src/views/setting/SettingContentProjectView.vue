<script setup lang="ts">
import { ref, onMounted } from 'vue'

import type { ProjectCreate } from '@/types/Item'
import useProjectStore from '@/stores/ProjectStore'
import ItemService from '@/services/ItemService'
import StateLabel from '@/components/common/StateLabel.vue'
import MarkedText from '@/components/common/MarkedText.vue'
import CreateProjectDialog from '@/components/dialog/CreateProjectDialog.vue'

const headers = [
  { title: 'RID', key: 'rid', width: '50px' },
  { title: 'STATE', key: 'state', width: '50px' },
  { title: 'TITLE', key: 'title' },
  { title: 'DETAIL', key: 'detail' },
  { title: 'RESULT', key: 'result' },
  { title: 'ENTRY', key: 'datetime_entry', width: '300px' },
  { title: 'USER', key: 'name', width: '100px' },
  { title: '', key: '', width: '140px' }
]

const store_project = useProjectStore()

const dialog_entry = ref(false)
const dialog_update = ref(false)

const dialog_form_data = ref<ProjectCreate>({
  rid_users: 0,
  title: '',
  detail: '',
  datetime_start: '',
  datetime_end: ''
})

onMounted(() => {
  store_project.fetchProjects()
})

const openEntryDialog = () => {
  dialog_entry.value = true
}

const openUpdateDialog = () => {
  dialog_update.value = true
}

const handleSubmit = async (data: ProjectCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createProject(data)
    store_project.fetchProjects()
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
          Projects
          <v-btn icon size="x-small" @click="openEntryDialog()">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="store_project.projects" :headers="headers">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.rid }}</td>
              <td><StateLabel :state="item.state" /></td>
              <td>{{ item.title }}</td>
              <td><MarkedText :src="item.detail" /></td>
              <td><MarkedText :src="item.result" /></td>
              <td>{{ item.datetime_entry }}</td>
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

  <CreateProjectDialog
    :showDialog="dialog_entry"
    :formData="dialog_form_data"
    @update:showDialog="dialog_entry = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped></style>
