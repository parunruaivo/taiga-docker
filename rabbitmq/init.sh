#!/bin/bash
set -e


create_vhost(){
    if [[ -n ${RABBITMQ_VHOST} ]]; then
        for vhost in $(awk -F',' '{for (i = 1 ; i <= NF ; i++) print $i}' <<< "${RABBITMQ_VHOST}"); do
          if [[ -z $(rabbitmqctl list_vhosts | grep ${vhost};) ]]; then
              echo "Creating vhost: ${vhost}..."
              rabbitmqctl add_vhost ${vhost} >/dev/null

              if [[ -n ${RABBITMQ_USER} ]]; then
                echo "‣ Granting access to ${RABBITMQ_USER} user..."
                rabbitmqctl set_permissions -p ${vhost} ${RABBITMQ_USER} ".*" ".*" ".*" >/dev/null
              fi
          fi
        done
    fi
}

create_user(){
    if [[ -n ${RABBITMQ_USER} ]]; then
        if [[ -z ${RABBITMQ_PASS} ]]; then
          echo "ERROR! Please specify a password for RABBITMQ_USER in RABBITMQ_PASS. Exiting..."
          exit 1
        fi
        if [[ -z $(rabbitmqctl list_users | grep ${RABBITMQ_USER};) ]]; then
          echo "Creating user: ${RABBITMQ_USER}"
          rabbitmqctl add_user ${RABBITMQ_USER} ${RABBITMQ_PASS} >/dev/null
        fi
    fi
}
(
    sleep 15; \
    create_user; \
    create_vhost; \
) &

rabbitmq-server $@