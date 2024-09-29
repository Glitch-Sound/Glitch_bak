#!/bin/sh

envsubst '$$FRONTEND_HOST $$BACKEND_HOST' \
  < /etc/nginx/templates/default.conf.template \
  > /etc/nginx/conf.d/default.conf

exec "$@"
