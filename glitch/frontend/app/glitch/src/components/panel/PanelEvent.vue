<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useRoute } from 'vue-router'

import type { Item, FeatureCreate } from '@/types/Item'
import useUserStore from '@/stores/UserStore'
import useItemStore from '@/stores/ItemStore'
import CreateFeatureDialog from '@/components/dialog/CreateFeatureDialog.vue'
import TypeLabel from '@/components/common/TypeLabel.vue'
import StateLabel from '@/components/common/StateLabel.vue'
import TitleLabel from '@/components/common/TitleLabel.vue'
import UserLabel from '@/components/common/UserLabel.vue'
import InformationEvent from '@/components/panel/InformationEvent.vue'
import DetailEvent from '@/components/panel/DetailEvent.vue'

const props = defineProps<{
  item: Item
}>()

const route = useRoute()
const store_user = useUserStore()
const store_item = useItemStore()

const expand = ref(false)
const dialog = ref(false)

const dialog_form_data = ref<FeatureCreate>({
  id_project: Number(route.params.id_project),
  rid_items: props.item.rid,
  rid_users: store_user.login_user?.rid ?? 0,
  title: '',
  detail: ''
})

const openDialog = () => {
  dialog.value = true
}

const handleSubmit = (data: FeatureCreate) => {
  store_item.createFeature(data)
  dialog.value = false
}
</script>

<template>
  <div class="panel-common panel-event">
    <v-row class="align-baseline">
      <v-col class="type" cols="auto">
        <TypeLabel :item="props.item" />
      </v-col>

      <v-col class="state" cols="auto">
        <StateLabel :state="props.item.state" />
      </v-col>

      <v-col @click="expand = !expand">
        <TitleLabel :item="props.item" />
      </v-col>

      <v-col cols="auto">
        <UserLabel :item="props.item" />
      </v-col>

      <v-col class="information" cols="auto">
        <InformationEvent :item="props.item" />
      </v-col>

      <v-col cols="auto">
        <v-btn icon variant="text" size="x-small" @click="openDialog()">
          <v-icon>mdi-plus-thick</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <DetailEvent v-bind="{ ...props, expand }" />
  </div>

  <CreateFeatureDialog
    :dialog_show="dialog"
    :data_form="dialog_form_data"
    @update:showDialog="dialog = $event"
    @submit="handleSubmit"
  />
</template>

<style scoped>
@import '@/components/panel/panel.css';
</style>
