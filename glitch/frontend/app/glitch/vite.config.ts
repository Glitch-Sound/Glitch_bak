import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv, ConfigEnv, UserConfigExport } from 'vite'
import vue from '@vitejs/plugin-vue'

export default ({ mode }: ConfigEnv): UserConfigExport => {
  const env = loadEnv(mode, process.cwd(), '')

  return defineConfig({
    base: env.VITE_APP_BASE_URL || '/',
    server: {
      host: '0.0.0.0',
      port: Number(env.FRONTEND_PORT) || 3000,
      hmr: {
        protocol: 'ws',
        host: env.VITE_HMR_HOST || 'localhost',
        port: Number(env.VITE_HMR_PORT) || Number(env.FRONTEND_PORT) || 3000,
        clientPort: Number(env.VITE_HMR_CLIENT_PORT) || 80
      }
    },
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
  })
}
