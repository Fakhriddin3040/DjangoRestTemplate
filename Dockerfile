FROM node:20-alpine as build

WORKDIR /marketplace

COPY . /marketplace

RUN npm install --force

RUN npm run build

FROM nginx:1.17.1-alpine

COPY --from=build /marketplace/dist/marketplace /usr/share/nginx/html

COPY ./nginx/nginx.conf  /etc/nginx/conf.d/default.conf

EXPOSE 80