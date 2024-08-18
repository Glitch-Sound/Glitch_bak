<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'

import useUserStore from '@/stores/UserStore'
import useProjectStore from '@/stores/ProjectStore'
import UserDetail from '@/components/common/UserDetail.vue'
import ProjectDialog from '@/components/dialog/ProjectDialog.vue'

const route = useRoute()
const store_user = useUserStore()
const store_project = useProjectStore()

const title = ref('Glitch')
const link_project = ref('/')
const link_disabled = ref(true)
const dialog = ref(false)

onMounted(() => {
  store_project.fetchProjects()
})

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

const toggleDialog = () => {
  dialog.value = !dialog.value
}

const handleSubmit = async () => {
  dialog.value = false
}
</script>

<template>
  <v-app-bar color="#272d38">
    <v-app-bar-title @click="toggleDialog">
      {{ title }}
    </v-app-bar-title>

    <v-btn icon color="iconColor">
      <router-link to="/">
        <v-icon>mdi-home</v-icon>
      </router-link>
    </v-btn>

    <v-btn icon color="iconColor" :disabled="link_disabled">
      <router-link :to="link_project">
        <v-icon>mdi-view-list</v-icon>
      </router-link>
    </v-btn>

    <v-btn icon disabled>
      <v-icon>mdi-account-tag</v-icon>
    </v-btn>

    <v-btn icon disabled>
      <v-icon>mdi-chart-scatter-plot-hexbin</v-icon>
    </v-btn>

    <v-spacer />

    <div class="mx-1">
      <UserDetail />
    </div>

    <v-btn icon disabled class="mx-1">
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <v-btn :disabled="store_user.login_user == null" icon color="iconColor" class="mx-1">
      <router-link to="/setting/main">
        <v-icon>mdi-cog</v-icon>
      </router-link>
    </v-btn>
  </v-app-bar>

  <ProjectDialog :showDialog="dialog" @submit="handleSubmit" />
</template>

<style scoped>
.v-toolbar-title {
  font-size: 26px;
  color: #ffffff;
  line-height: 1.5;
}
</style>
