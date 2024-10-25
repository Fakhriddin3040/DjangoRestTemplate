FROM node:20-alpine as build

WORKDIR /app

COPY package*.json ./

RUN npm install --force

COPY . .

RUN npm run build --prod

FROM node:20-alpine

WORKDIR /app

COPY --from=build /app/dist ./dist

CMD ["node", "/app/dist/marketplace-client/server/server.mjs"]

EXPOSE 3000
