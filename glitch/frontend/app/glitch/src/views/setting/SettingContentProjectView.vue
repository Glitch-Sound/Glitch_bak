<script setup lang="ts">
import { ref, onMounted } from 'vue'
import useProjectStore from '@/stores/ItemStore'
import ItemService from '@/services/ItemService'
import CreateProjectDialog from '@/components/dialog/CreateProjectDialog.vue'
import type { ProjectCreate } from '@/types/Item'

const store_project = useProjectStore()
onMounted(() => {
  store_project.fetchProjects()
})

const dialog = ref(false)
const dialogFormData = ref(null)

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
    <v-container>
      <div>
        Projects
        <v-btn icon size="x-small" @click="openDialog(true)">
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
      <div>
        <ul v-if="store_project.projects.length">
          <li v-for="project in store_project.projects" :key="project.rid">
            {{ project.rid }}, {{ project.state }}, {{ project.risk }}, {{ project.title }},
            {{ project.detail }}, {{ project.result }}, {{ project.datetime_entry }},
            {{ project.datetime_update }}, {{ project.name }},
            {{ project.project_datetime_start }},{{ project.project_datetime_end }}
          </li>
        </ul>
      </div>
    </v-container>

    <CreateProjectDialog
      :showDialog="dialog"
      :formData="dialogFormData"
      @update:showDialog="dialog = $event"
      @submit="handleSubmit"
    />
  </v-main>
</template>

<style scoped></style>
