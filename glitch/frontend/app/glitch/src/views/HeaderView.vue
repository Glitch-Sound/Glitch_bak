<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import { ExtractType } from '@/types/Item'
import useUserStore from '@/stores/UserStore'
import useProjectStore from '@/stores/ProjectStore'
import useItemStore from '@/stores/ItemStore'
import UserDetail from '@/components/common/UserDetail.vue'
import ProjectDialog from '@/components/dialog/ProjectDialog.vue'
import SearchDialog from '@/components/dialog/SearchDialog.vue'

const route = useRoute()
const router = useRouter()
const store_user = useUserStore()
const store_project = useProjectStore()
const store_item = useItemStore()

const title = ref('Glitch')
const link_project = ref('/')
const link_disabled = ref(true)
const dialog_project = ref(false)
const dialog_search = ref(false)

onMounted(() => {
  store_project.fetchProjects()
})

watch([() => route.params.id_project, () => store_project.projects.length], () => {
  title.value =
    store_project.projects.find((project) => project.rid == Number(route.params.id_project))
      ?.title || 'Glitch'

  if (route.params.id_project) {
    store_project.setSelectedProjectID(Number(route.params.id_project))

    switch (Number(route.query.extruct)) {
      case ExtractType.ALL:
        store_item.setExtractAll()
        break
      case ExtractType.INCOMPLETE:
        store_item.setExtractIncomplete()
        break
      case ExtractType.HIGH_RISK:
        store_item.setExtractHighRisk()
        break
      case ExtractType.ALERT:
        store_item.setExtractAlert()
        break
      case ExtractType.ASSIGNMENT:
        store_item.setExtractAssignment()
        break
      case ExtractType.RELATION:
        store_item.setExtractItem(Number(route.query.target))
        break
      case ExtractType.SEARCH:
        store_item.setExtractSearch(String(route.query.target))
        break
    }

    store_item.fetchItems(router)
  }
})

watch([() => store_project.selected_id_project], () => {
  link_project.value = '/project/' + store_project.selected_id_project
  link_disabled.value = false
})

const toggleDialogProject = () => {
  dialog_project.value = !dialog_project.value
}

const toggleDialogSearch = () => {
  dialog_search.value = !dialog_search.value
}

const handleSubmitProject = async () => {
  dialog_project.value = false
}
</script>

<template>
  <v-app-bar color="#000000">
    <template v-slot:image>
      <v-img gradient="to top, rgba(0, 0, 0, 0), rgba(29, 35, 46, 0.4), rgba(59, 65, 79, 0.7)" />
    </template>

    <v-app-bar-title @click="toggleDialogProject" class="app-bar-title">
      <v-icon class="mr-1" size="small">mdi-grain</v-icon>
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

    <v-btn
      icon
      class="mx-1"
      :disabled="store_project.selected_id_project == null"
      @click="toggleDialogSearch"
    >
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <v-btn :disabled="store_user.login_user == null" icon color="iconColor" class="mx-1">
      <router-link to="/setting/main">
        <v-icon>mdi-cog</v-icon>
      </router-link>
    </v-btn>
  </v-app-bar>

  <ProjectDialog :dialog_show="dialog_project" @submit="handleSubmitProject" />
  <SearchDialog :dialog_show="dialog_search" @update:showDialog="dialog_search = $event" />
</template>

<style scoped>
.v-toolbar-title {
  font-size: 26px;
  color: #ffffff;
  line-height: 1.5;
}
</style>
