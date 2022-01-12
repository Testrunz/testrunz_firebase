# Dockerfile for React client

# Build react client
FROM node:16-alpine3.11

# Working directory be app
WORKDIR /usr/src/app

COPY package*.json ./

# copy local files to app folder
COPY . .
###  Installing dependencies
RUN apk -U upgrade

RUN npm install --force

EXPOSE 3000
CMD ["npm", "run", "build"] # required for creating index.html
CMD ["npm", "run", "start:dev"]
