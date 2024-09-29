FROM nginx:alpine

ARG MODE=development
ENV MODE=$MODE

RUN apk update && apk add --no-cache gettext

COPY ./templates /etc/nginx/templates
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
