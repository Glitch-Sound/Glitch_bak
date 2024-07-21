FROM node:lts-buster-slim

WORKDIR /app

RUN apt update && \
    npm install -g npm


WORKDIR /app/glitch

CMD ["npm", "run", "dev"]
