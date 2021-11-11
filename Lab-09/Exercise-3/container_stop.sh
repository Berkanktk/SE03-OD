#!/bin/bash

docker network rm f CONTAINER_CREATE

for i in {1..10}
do
    docker stop bash_container_$i
    docker rm bash_container_$1
done
