<script setup lang="ts">
import { ref, defineProps, watch, onMounted } from 'vue'

import { type EmitSubmit } from '@/components/common/events'
import useProjectStore from '@/stores/ProjectStore'
import MarkedText from '@/components/common/MarkedText.vue'
import StateLabel from '@/components/common/StateLabel.vue'

const headers = [
  { title: 'ID', key: 'rid', width: '50px' },
  { title: 'STATE', key: 'state', width: '50px' },
  { title: 'TITLE', key: 'title' },
  { title: 'DETAIL', key: 'detail' },
  { title: 'END', key: 'datetime_entry', width: '120px' },
  { title: 'USER', key: 'name', width: '100px' }
]

const props = defineProps<{
  dialog_show: boolean
}>()

const dialog = ref(props.dialog_show)

const store_project = useProjectStore()

onMounted(() => {
  store_project.fetchProjects()
})

watch(
  () => props.dialog_show,
  (new_value) => {
    dialog.value = new_value
  }
)

const emit = defineEmits<EmitSubmit>()
const handleSubmit = async (id_project: number) => {
  store_project.setSelectedProjectID(id_project)
  dialog.value = false
  emit('submit', id_project)
}
</script>

<template>
  <v-dialog v-model="dialog" persistent>
    <v-card class="dialog-card">
      <v-card-title>
        <span class="text-h5">Project</span>
      </v-card-title>

      <v-data-table class="ml-5 data-table" :items="store_project.projects" :headers="headers">
        <template v-slot:item="{ item }">
          <tr>
            <td>{{ item.id_project }}</td>
            <td><StateLabel :state="item.state" /></td>
            <td class="title">
              <router-link
                :to="`/project/${item.id_project}`"
                @click="handleSubmit(item.id_project)"
              >
                {{ item.title }}
              </router-link>
            </td>
            <td><MarkedText :src="item.detail" /></td>
            <td>{{ item.project_datetime_end }}</td>
            <td>{{ item.name }}</td>
          </tr>
        </template>
      </v-data-table>

      <template v-slot:actions>
        <v-btn class="ms-auto" text="Ok" @click="handleSubmit"></v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<style scoped>
.dialog-card {
  padding: 10px 20px;
}

.title {
  color: #ffffff;
  font-weight: bold;
}
</style>
