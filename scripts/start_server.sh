#!/bin/bash

cd /home/ec2-user/app/
docker-compose -d --build up > /dev/null 2> /dev/null < /dev/null &
