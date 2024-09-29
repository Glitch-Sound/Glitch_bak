import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv, ConfigEnv, UserConfigExport } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'

export default ({ mode }: ConfigEnv): UserConfigExport => {
  const env = loadEnv(mode, process.cwd())

  return defineConfig({
    server: {
      host: '0.0.0.0',
      port: 5173,
      hmr: {
        protocol: 'ws',
        host: env.VITE_HMR_HOST || 'localhost',
        port: Number(env.VITE_HMR_PORT) || 5173,
        clientPort: Number(env.VITE_HMR_CLIENT_PORT) || 80
      }
    },
    plugins: [vue(), VueDevTools()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
  })
}
