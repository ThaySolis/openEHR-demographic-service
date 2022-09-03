#!/usr/bin/env bash

# This script runs inside SCONE.
# The following mounted directories are expected:
# - /cas_session -> The folder that will contain the CAS session and related resources.
#   - .../cas-cert.pem  (IN)
#   - .../cas-key.pem (IN)
#   - .../cas-session-template.yml (IN)
#   - .../cas-config-id.out (OUT)
#   - .../cas-session.yml (OUT)
# - /scone_scripts -> The folder that contains this script.

# The following environment variables are expected:
# - FSPF_KEY
# - FSPF_TAG
# - CAS_ADDR
# - CAS_MRENCLAVE

# Install dependencies.
apk add gettext curl

# Paths to useful directories.
SCRIPT_FOLDER=$( dirname -- "$( readlink -f -- "$0"; )"; )
CAS_SESSION_FOLDER=/cas_session
cd "$SCRIPT_FOLDER"

# Generate the session ID.
export SCONE_CONFIG_ID="demographic-service-$RANDOM-$RANDOM-$RANDOM"
echo $SCONE_CONFIG_ID > "$CAS_SESSION_FOLDER/cas-config-id.out"

# Generate the MRENCLAVE of the Python executable.
unset MRENCLAVE
export MRENCLAVE=$(SCONE_HASH=1 python)

# Load variable defaults.
[ -z "${PLAIN_HTTP}" ] && PLAIN_HTTP=no
[ -z "${SERVER_PORT}" ] && SERVER_PORT=12002
[ -z "${SYSTEM_ID}" ] && SYSTEM_ID=demographic.system
[ -z "${INCLUDE_USAGE_STATISTICS}" ] && INCLUDE_USAGE_STATISTICS=yes
[ -z "${USAGE_STATISTICS_MAX_SAMPLES}" ] && USAGE_STATISTICS_MAX_SAMPLES=1000
[ -z "${AUTH_USERNAME}" ] && AUTH_USERNAME=demographic_user
[ -z "${AUTH_PASSWORD}" ] && AUTH_PASSWORD=demographic_password
[ -z "${DB_HOST}" ] && DB_HOST=127.0.0.1
[ -z "${DB_PORT}" ] && DB_PORT=27018
[ -z "${DB_USERNAME}" ] && DB_USERNAME=root
[ -z "${DB_PASSWORD}" ] && DB_PASSWORD=example

# Generate the session file.
envsubst < "$CAS_SESSION_FOLDER/cas-session-template.yml" > "$CAS_SESSION_FOLDER/cas-session.yml"

# Send the session creation request to the CAS.
curl -v -k -s \
    --cert "$CAS_SESSION_FOLDER/cas-cert.pem" \
    --key "$CAS_SESSION_FOLDER/cas-key.pem" \
    --data-binary "@$CAS_SESSION_FOLDER/cas-session.yml" \
    -X POST https://$CAS_ADDR:8081/session
