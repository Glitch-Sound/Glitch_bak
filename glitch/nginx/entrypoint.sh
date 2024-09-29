#!/bin/sh

envsubst '$$FRONTEND_HOST $$BACKEND_HOST $$FRONTEND_PORT $$BACKEND_PORT' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"
