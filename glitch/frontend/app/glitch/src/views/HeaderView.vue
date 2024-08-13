<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'

import useProjectStore from '@/stores/ProjectStore'
import AccountDetail from '@/components/common/AccountDetail.vue'
import ProjectDialog from '@/components/dialog/ProjectDialog.vue'

const route = useRoute()
const store_project = useProjectStore()

const title = ref('Glitch')
const link_project = ref('/')
const link_disabled = ref(true)
const dialog = ref(false)

const toggleDialog = () => {
  dialog.value = !dialog.value
}

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

const handleSubmit = async () => {
  dialog.value = false
}
</script>

<template>
  <v-app-bar color="#272d38">
    <!-- <v-app-bar-title @click="toggleDialog"> -->
    <v-app-bar-title @click="toggleDialog">
      {{ title }}
    </v-app-bar-title>

    <router-link to="/">
      <v-btn icon color="iconColor">
        <v-icon>mdi-home</v-icon>
      </v-btn>
    </router-link>

    <router-link :to="link_project">
      <v-btn icon color="iconColor" :disabled="link_disabled">
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

    <div class="mx-1">
      <AccountDetail :rid_users="0" :name="'Guest'"></AccountDetail>
    </div>

    <v-btn icon disabled class="mx-1">
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <router-link to="/setting/main">
      <v-btn icon color="iconColor" class="mx-1">
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </router-link>
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
