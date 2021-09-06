#!/usr/bin/env bash

SOURCE_DIR="/source/dir"
BUILD_DIR="/build/dir"

JEKYLL_ENV="production"

USERNAME="user"
SFTP_HOST="host"

cd $SOURCE_DIR && bundle exec jekyll build -s $SOURCE_DIR -d $BUILD_DIR 2>&1

rsync -vrzhc --delete -e ssh $BUILD_DIR $USERNAME@$SFTP_HOST:/home/public/ 2>&1
