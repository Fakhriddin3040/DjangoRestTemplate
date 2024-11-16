#!/bin/bash

# Use on manipulator service.

# Check if the cron job already exists
crontab -l | grep -q "/bin/bash ./scripts/certbot_renew.sh"
if [ $? -eq 0 ]; then
    echo "Cron job already exists."
else
    # Add the cron job
    (crontab -l; echo "0 0 * * * /bin/bash ./scripts/certbot_renew.sh") | crontab -
    echo "Cron job added."
fi