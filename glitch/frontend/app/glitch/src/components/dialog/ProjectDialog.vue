<script setup lang="ts">
import { ref, defineProps, watch, onMounted } from 'vue'

import { type EmitSubmit } from '@/components/common/events'
import useProjectStore from '@/stores/ProjectStore'
import MarkedText from '@/components/common/MarkedText.vue'

const headers = [
  { title: 'RID', key: 'rid', width: '50px' },
  { title: 'STATE', key: 'state', width: '50px' },
  { title: 'TITLE', key: 'title' },
  { title: 'DETAIL', key: 'detail' },
  { title: 'RESULT', key: 'result' },
  { title: 'ENTRY', key: 'datetime_entry', width: '300px' },
  { title: 'USER', key: 'name', width: '100px' }
]

const props = defineProps<{
  showDialog: boolean
}>()

const dialog = ref(props.showDialog)

const store_project = useProjectStore()

onMounted(() => {
  store_project.fetchProjects()
})

watch(
  () => props.showDialog,
  (newValue) => {
    dialog.value = newValue
  }
)

const emit = defineEmits<EmitSubmit>()
const handleSubmit = async () => {
  dialog.value = false
  emit('submit')
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
            <td>{{ item.rid }}</td>
            <td>{{ item.state }}</td>
            <td>
              <router-link :to="`/project/${item.rid}`" @click="handleSubmit">
                {{ item.title }}
              </router-link>
            </td>
            <td><MarkedText :src="item.detail" /></td>
            <td><MarkedText :src="item.result" /></td>
            <td>{{ item.datetime_entry }}</td>
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
</style>
