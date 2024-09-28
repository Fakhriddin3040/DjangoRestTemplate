FROM node:20-alpine as build

WORKDIR /app

COPY package*.json ./

RUN npm install --force

COPY . .

RUN npm run build --prod

RUN mv /app/dist /app/build

RUN mv /app/build /app