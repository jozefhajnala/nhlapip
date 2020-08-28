#!/bin/sh
set -e

dir_script=$(dirname $(readlink -f "$0"))
dir_root=$dir_script/../
dir_package=$(basename $(dirname $dir_script))
image_name=python
container_name=${dir_package}_check

docker run -id --name $container_name $image_name bash
docker cp $dir_root $container_name:/root

docker exec \
  --workdir /root/$dir_package \
  $container_name \
  sh "$@"

docker stop $container_name
docker rm $container_name
