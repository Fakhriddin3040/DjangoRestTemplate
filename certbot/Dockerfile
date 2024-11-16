FROM alpine:latest

# Get env variable from .env
ARG DOMAIN_EMAIL \
    DOMAIN_URL

# Set env variables
ENV DOMAIN_EMAIL=${DOMAIN_EMAIL} \
    DOMAIN_URL=${DOMAIN_URL}

WORKDIR /certbot

COPY . /certbot/

RUN apk update && \
    apk add --no-cache certbot

CMD ["sh", "generate-certificate.sh"]