#!/bin/sh

export VITE_HMR_HOST=localhost
export VITE_HMR_CLIENT_PORT=8888

if [ "$NODE_ENV" = "production" ]; then
  npm run build
  npm run start -- --host 0.0.0.0 --port 5173
else
  npm run dev -- --host 0.0.0.0 --port 5173
fi
