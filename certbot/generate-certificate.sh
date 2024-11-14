#!/bin/sh

# This script generates SSL certificate

# Clean folder, where could be old certificates
rm -rf /etc/letsencrypt/live/certfolder*

# Give ourselves certificate
certbot certonly --standalone \
    --email $DOMAIN_EMAIL \
    -d $DOMAIN_URL \
    --cert-name=certfolder \
    --key-type rsa \
    --agree-tos

# Removing old certificates from mounted nginx folder.
rm /etc/nginx/cert.pem /etc/nginx/key.pem

# Copy new certificates from certbot to mounted nginx folder
cp /etc/letsencrypt/live/certfolder/fullchain.pem /etc/nginx/cert.pem
cp /etc/letsencrypt/live/certfolder/privkey.pem /etc/nginx/key.pem