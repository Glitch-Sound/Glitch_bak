<script setup lang="ts">
import { ref, onMounted, watchEffect } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ItemService from '@/services/ItemService'
import type { Project } from '@/types/Item'

const title = ref('Glitch')

const projects = ref<Project[]>([])
const fetchProjects = async () => {
  try {
    const service_item = new ItemService()
    projects.value = await service_item.getProjects()
  } catch (err) {
    console.error('Error:', err)
  }
}

const route = useRoute()
const router = ref(useRouter())
watchEffect(async () => {
  await router.value.isReady()
  const { rid } = route.params
  console.log('ID:', rid)
})

const projectDialog = ref(false)
const toggleDialog = () => {
  projectDialog.value = !projectDialog.value
}

const handleSubmit = async (project: Project) => {
  console.log('ID:', project.rid)
  projectDialog.value = false
}

onMounted(fetchProjects)
</script>

<template>
  <v-app-bar class="elevation-0">
    <v-app-bar-title @click="toggleDialog">
      {{ title }}
    </v-app-bar-title>

    <router-link to="/">
      <v-btn icon>
        <v-icon>mdi-home</v-icon>
      </v-btn>
    </router-link>

    <router-link to="/">
      <v-btn icon>
        <v-icon>mdi-view-list</v-icon>
      </v-btn>
    </router-link>

    <v-btn icon disabled>
      <v-icon>mdi-account-tag</v-icon>
    </v-btn>
    <v-btn icon disabled>
      <v-icon>mdi-chart-scatter-plot-hexbin</v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    Guest
    <v-btn icon>
      <v-icon>mdi-account-circle</v-icon>
    </v-btn>

    <v-btn icon disabled>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <router-link to="/setting">
      <v-btn icon>
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </router-link>
  </v-app-bar>

  <v-dialog v-model="projectDialog" max-width="1500px">
    <v-card>
      <v-card-title class="headline">Project</v-card-title>
      <v-card-text>
        <ul v-if="projects.length">
          <li v-for="project in projects" :key="project.rid">
            {{ project.rid }}, {{ project.state }}, {{ project.risk }},
            <router-link to="/project/1" @click="handleSubmit(project)">{{
              project.title
            }}</router-link
            >, {{ project.detail }}, {{ project.result }}, {{ project.datetime_entry }},
            {{ project.datetime_update }}, {{ project.name }},
            {{ project.project_datetime_start }},{{ project.project_datetime_end }}
          </li>
        </ul>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="projectDialog = false">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
