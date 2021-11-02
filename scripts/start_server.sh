#!/bin/sh
# Remember to change back to ec2-user
# Very important to traverse to the proper location
cd /home/ec2-user/server
docker-compose pull
docker-compose up -d
cd -
