FROM docker:latest

ARG DOMAIN_URL
ENV DOMAIN_URL=$DOMAIN_URL

RUN apk add --no-cache bash dcron

WORKDIR /app

COPY . /app/

RUN chmod +x /app/scripts/*.sh

CMD ["sh", "-c", "/app/scripts/entrypoint.sh"]