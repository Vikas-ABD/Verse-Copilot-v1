import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
  // Add this entire 'server' block to enable hot-reloading inside Docker
  server: {
    host: true, // This ensures the server is accessible from outside the container
    port: 5173, // The port we are using in docker-compose
    watch: {
      // This is the crucial part that fixes hot-reloading in Docker
      usePolling: true,
    },
  },
})
