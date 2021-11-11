#!/bin/bash

function task_100ms() {
    echo “task 100ms running”
}

function task_1s() {
    echo “task 1s running”
}

function task_5s() {
    echo “task 5s running”
}

number=0
while true; 
do
    sleep 0.1s
    task_100ms
    number=$((number + 1))

    if [ $number -eq 10 ]
    then
        task_1s
    elif [ $number -eq 50 ]
    then
        task_5s
    fi
done  