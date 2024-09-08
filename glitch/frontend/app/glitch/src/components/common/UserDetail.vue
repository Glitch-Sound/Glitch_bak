<script setup lang="ts">
import { ref, computed } from 'vue'

import type { Login } from '@/types/User'
import useUserStore from '@/stores/UserStore'
import UserService from '@/services/UserService'
import LoginDialog from '@/components/dialog/LoginDialog.vue'

import Identicon from 'identicon.js'
import * as CryptoJS from 'crypto-js'

const store_user = useUserStore()

const dialog = ref(false)

const dialog_form_data = ref<Login>({
  user: '',
  password: ''
})

const openDialog = () => {
  dialog_form_data.value = { user: '', password: '' }
  dialog.value = true
}

const hash = computed(() => {
  if (store_user.login_user == undefined) {
    return ''
  }
  return CryptoJS.MD5(store_user.login_user.rid + store_user.login_user.name).toString()
})

const identiconDataUri = computed(() => {
  const options = {
    background: [0, 0, 0, 0] as [number, number, number, number],
    format: 'svg' as 'svg'
  }
  return 'data:image/svg+xml;base64,' + new Identicon(hash.value, options).toString()
})

const handleLogin = async (data: Login) => {
  try {
    const service_user = new UserService()
    const login_user = await service_user.login(data)
    store_user.setLoginUser(login_user)
    dialog.value = false
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>

<template>
  <div v-if="store_user.login_user == null">
    <v-btn variant="text" @click="openDialog()">Login</v-btn>
  </div>
  <div v-else>
    <div class="align-baseline">
      <span class="mr-1 username">
        {{ store_user.login_user.name }}
      </span>

      <v-btn icon size="small" @click="openDialog()">
        <img :src="identiconDataUri" width="22" height="22" />
      </v-btn>
    </div>
  </div>

  <LoginDialog
    :dialog_show="dialog"
    :data_form="dialog_form_data"
    :is_startup="true"
    @update:showDialog="dialog = $event"
    @submit="handleLogin"
  />
</template>

<style scoped>
.username {
  font-size: 18px;
}
</style>
