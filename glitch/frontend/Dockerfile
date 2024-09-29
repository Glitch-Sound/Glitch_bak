FROM node:lts-buster-slim

ARG MODE=development
ENV NODE_ENV=$MODE

WORKDIR /app/glitch

COPY ./app/glitch/package*.json ./

RUN npm install

COPY ./app/glitch ./

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
