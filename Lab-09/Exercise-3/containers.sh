#!/bin/bash

docker network create CONTAINER_CREATE

for i in {1..10}
do
    docker run --name=bash_container_$i --network=CONTAINER_CREATE ubuntu
done
