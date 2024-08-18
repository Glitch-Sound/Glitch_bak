FROM node:lts-buster-slim

WORKDIR /app/glitch

COPY ./app/glitch/package*.json ./

RUN apt update
RUN npm install -g npm
RUN npm install

CMD ["npm", "run", "dev"]
