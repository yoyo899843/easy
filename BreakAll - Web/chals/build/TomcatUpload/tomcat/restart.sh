#!/bin/bash
while true
do
    docker-compose down -v
    docker-compose up -d --build
    sleep 5m
done
