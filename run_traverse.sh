#!/usr/bin/env bash

file_name=$1
run_time=$2
api_num=$3
ecpho=$4

echo "traverse start"
for i in `seq $api_num`
do
#  echo $i
  api_name="gateway"${i}
  echo $api_name
  bash run.sh $file_name $run_time $api_name $ecpho
done
