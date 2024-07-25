FROM node:lts-buster-slim

WORKDIR /app

COPY ./app/glitch/package*.json ./

RUN apt update && \
    npm install -g npm && \
    npm install

WORKDIR /app/glitch

CMD ["npm", "run", "dev"]
