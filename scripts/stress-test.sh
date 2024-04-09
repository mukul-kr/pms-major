#!/bin/bash

count=0
start_time=$(date +%s)

trap 'echo "Executed $count times in 1 second"; count=0; start_time=$(date +%s)' SIGINT

while true; do
  ((count++))
  
  curl -s -o /dev/null -X 'POST' \
    'http://localhost:8080/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'grant_type=&username=mukul0000kumar%40gmail.com&password=mukul&scope=&client_id=&client_secret='
  
  current_time=$(date +%s)
  elapsed_time=$((current_time - start_time))
  
  if [ "$elapsed_time" -ge 1 ]; then
    echo "Executed $count times in 1 second"
    count=0
    start_time=$current_time
  fi
done
