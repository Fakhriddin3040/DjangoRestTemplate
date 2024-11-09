FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install --force

COPY . .

CMD ["npm", "run", "start:full"]

EXPOSE 3000
EXPOSE 4200
