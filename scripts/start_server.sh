#!/bin/sh
# Remember to change back to ec2-user
cd /home/ec2-user/server
docker-compose up -d --build
cd -
