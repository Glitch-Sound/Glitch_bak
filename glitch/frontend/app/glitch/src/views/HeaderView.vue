<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import useUserStore from '@/stores/UserStore'
import useProjectStore from '@/stores/ItemStore'
import type { Project } from '@/types/Item'

const store_user = useUserStore()
const store_project = useProjectStore()
onMounted(() => {
  store_user.fetchUsers()
  store_project.fetchProjects()
})

const title = ref('')
const link_project = ref('/')
const link_disabled = ref(true)

const route = useRoute()
watch([() => route.params.rid, () => store_project.projects.length], () => {
  title.value =
    store_project.projects.find((project) => project.rid == Number(route.params.rid))?.title ||
    'Glitch'

  if (route.params.rid) {
    store_project.setSelectedProjectRID(Number(route.params.rid))
  }
})

watch([() => store_project.selected_rid_project], () => {
  link_project.value = '/project/' + store_project.selected_rid_project
  link_disabled.value = false
})

const projectDialog = ref(false)
const toggleDialog = () => {
  projectDialog.value = !projectDialog.value
}

const handleSubmit = async (project: Project) => {
  store_project.setSelectedProjectRID(project.rid)
  projectDialog.value = false
}
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

    <router-link :to="link_project">
      <v-btn icon :disabled="link_disabled">
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
        <ul v-if="store_project.projects.length">
          <li v-for="project in store_project.projects" :key="project.rid">
            {{ project.rid }}, {{ project.state }}, {{ project.risk }},
            <router-link :to="`/project/${project.rid}`" @click="handleSubmit(project)">{{
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
