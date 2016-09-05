#!/bin/bash

source ${TAIGA_RUNTIME_DIR}/configure

configure_system

exec "$@"
