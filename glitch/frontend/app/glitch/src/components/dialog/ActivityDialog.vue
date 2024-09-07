<script setup lang="ts">
import { ref, defineProps, watch, onMounted } from 'vue'

import useUserStore from '@/stores/UserStore'
import type { Item } from '@/types/Item'
import type { Activity } from '@/types/Activity'
import type { EmitDialog } from '@/components/common/events'
import ActivityService from '@/services/ActivityService'
import MarkedText from '@/components/common/MarkedText.vue'

const props = defineProps<{
  dialog_show: boolean
  item: Item
}>()

const store_user = useUserStore()

const emits = defineEmits<EmitDialog>()

const dialog = ref(props.dialog_show)
const comment = ref('')
const activities = ref<Activity[]>([])

onMounted(async () => {
  const service_activity = new ActivityService()
  activities.value = await service_activity.getActivities(props.item.rid)
})

watch(
  () => props.dialog_show,
  (newValue) => {
    dialog.value = newValue
  }
)

watch(dialog, (newValue) => {
  emits('update:showDialog', newValue)
})

const addData = async () => {
  if (store_user.login_user && comment.value.trim()) {
    const service_activity = new ActivityService()
    await service_activity.createActivity({
      rid_items: props.item.rid,
      rid_users: store_user.login_user.rid,
      activity: comment.value
    })

    activities.value = await service_activity.getActivities(props.item.rid)
  }
}
</script>

<template>
  <v-dialog v-model="dialog" persistent class="panel-common">
    <v-card>
      <v-card-title>
        <span class="text-h5">Activity</span>
      </v-card-title>

      <v-card-text>
        <div v-for="activity in activities" :key="activity.rid" class="mb-5">
          <div class="user">
            <span>{{ activity.datetime_entry }}</span>
            <span class="mx-3">{{ activity.name }}</span>
          </div>
          <div><MarkedText :src="activity.activity" /></div>
        </div>

        <v-form class="mt-8">
          <v-textarea v-model="comment" required />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn @click="addData">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
@import '@/components/dialog/dialog.css';

.user {
  color: #696969;
  font-size: 0.9rem;
}
</style>
