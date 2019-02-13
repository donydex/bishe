#!/usr/bin/env bash

file_name=$1
run_time=$2
api_name=$3
ecpho=$4

echo "get_requests start"
python get_requests.py $api_name $run_time $ecpho &

echo "docker_output start"
python docker_output.py $file_name $run_time &

echo "sleep start"
sleep $2

echo "zipkin_output start"
python zipkin_output.py $run_time $file_name $ecpho