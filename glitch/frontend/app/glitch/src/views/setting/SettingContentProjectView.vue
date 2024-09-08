<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import type { ProjectCreate, ProjectUpdate } from '@/types/Item'
import useUserStore from '@/stores/UserStore'
import useProjectStore from '@/stores/ProjectStore'
import ItemService from '@/services/ItemService'
import StateLabel from '@/components/common/StateLabel.vue'
import MarkedText from '@/components/common/MarkedText.vue'
import CreateProjectDialog from '@/components/dialog/CreateProjectDialog.vue'
import UpdateProjectDialog from '@/components/dialog/UpdateProjectDialog.vue'

const headers = [
  { title: 'ID', width: '50px' },
  { title: 'STATE', width: '50px' },
  { title: 'TITLE' },
  { title: 'DETAIL' },
  { title: 'END', width: '120px' },
  { title: 'USER', width: '100px' },
  { title: '', width: '140px' }
]

const route = useRoute()
const store_user = useUserStore()
const store_project = useProjectStore()

const dialog_entry = ref(false)
const dialog_update = ref(false)
const target_delete = ref(0)

const dialog_form_data_entry = ref<ProjectCreate>({
  rid_users: store_user.login_user?.rid ?? 0,
  title: '',
  detail: '',
  datetime_start: '',
  datetime_end: ''
})

const dialog_form_data_update = ref<ProjectUpdate>({
  rid: 0,
  state: 0,
  rid_users: 0,
  rid_users_review: null,
  title: '',
  detail: '',
  result: '',
  datetime_start: '',
  datetime_end: ''
})

onMounted(() => {
  store_project.setSelectedProjectID(Number(route.params.id_project))
})

const openEntryDialog = () => {
  dialog_entry.value = true
}

const openUpdateDialog = (rid: number) => {
  const target = store_project.projects.find((item) => item.rid == rid)
  if (!target) {
    return
  }

  dialog_form_data_update.value = {
    rid: target.rid,
    state: target.state,
    rid_users: target.rid_users,
    rid_users_review: null,
    title: target.title,
    detail: target.detail,
    result: target.result,
    datetime_start: target.project_datetime_start,
    datetime_end: target.project_datetime_end
  }
  target_delete.value = rid
  dialog_update.value = true
}

const handleEntry = async (data: ProjectCreate) => {
  try {
    const service_item = new ItemService()
    await service_item.createProject(data)
    store_project.fetchProjects()
    dialog_entry.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}

const handleUpdate = async (data: ProjectUpdate) => {
  try {
    const service_item = new ItemService()
    await service_item.updateProject(data)
    store_project.fetchProjects()
    dialog_update.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}

const handleDelete = async () => {
  try {
    const service_item = new ItemService()
    await service_item.deleteProject(target_delete.value)
    store_project.fetchProjects()
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
          Projects
          <v-btn icon size="x-small" @click="openEntryDialog()">
            <v-icon>mdi-plus-thick</v-icon>
          </v-btn>
        </div>

        <v-data-table class="ml-5 data-table" :items="store_project.projects" :headers="headers">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.id_project }}</td>
              <td><StateLabel :state="item.state" /></td>
              <td>{{ item.title }}</td>
              <td><MarkedText :src="item.detail" /></td>
              <td>{{ item.project_datetime_end }}</td>
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

  <CreateProjectDialog
    :dialog_show="dialog_entry"
    :data_form="dialog_form_data_entry"
    @update:showDialog="dialog_entry = $event"
    @submit="handleEntry"
  />

  <UpdateProjectDialog
    :dialog_show="dialog_update"
    :data_form="dialog_form_data_update"
    @update:showDialog="dialog_update = $event"
    @submit="handleUpdate"
    @delete="handleDelete"
  />
</template>

<style scoped></style>
