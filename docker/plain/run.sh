#!/usr/bin/env bash

SCRIPT_FOLDER=$( dirname -- "$( readlink -f -- "$0"; )"; )

SOURCE_FOLDER=$SCRIPT_FOLDER/../..

docker run -it --rm \
    --name "openehr-demographic-service" \
    --env-file "$SOURCE_FOLDER/.env" \
    --network host \
    "openehr-demographic-service-plain"
