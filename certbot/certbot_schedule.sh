#!/bin/bash

# Use on manipulator service.
crontab -l | { cat; echo "0 0 * * * /bin/bash /scripts/renew_ssl_certificates.sh"; } | crontab -