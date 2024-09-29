FROM nginx:alpine

RUN apk update && apk add --no-cache gettext

COPY ./conf.d /etc/nginx/conf.d
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
