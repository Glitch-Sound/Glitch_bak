#!/bin/sh

if [ "$DISABLE_CACHE" = "true" ]; then
  export CACHE_DIRECTIVES='        add_header Cache-Control "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0";
        proxy_no_cache 1;
        proxy_cache_bypass 1;'
else
  export CACHE_DIRECTIVES=''
fi

envsubst '${FRONTEND_PATH} ${CACHE_DIRECTIVES}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"
