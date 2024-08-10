import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from '@/App.vue'
import router from '@/router'

import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css'
import { createVuetify, type ThemeDefinition } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import WebFont from 'webfontloader'
import './assets/main.css'

const app = createApp(App)
const pinia = createPinia()

WebFont.load({
  google: {
    families: ['Noto+Sans+JP:wght@100..900&display=swap']
  }
})

const myDarkTheme: ThemeDefinition = {
  dark: true,
  colors: {
    background: '#000000',
    surface: '#0a0a0a',
    'on-surface': '#cdcdcd'
  },
  variables: {
    fontFamily: 'Noto Sans JP, sans-serif'
  }
}

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'myDarkTheme',
    // defaultTheme: 'dark'
    // defaultTheme: 'light'
    themes: {
      myDarkTheme
    }
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi
    }
  }
})

app.use(pinia)
app.use(router)
app.use(vuetify)

app.mount('#app')
