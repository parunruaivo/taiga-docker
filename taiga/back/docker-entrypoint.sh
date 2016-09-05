#!/bin/bash

source ${TAIGA_RUNTIME_DIR}/configure

configure_system

sleep 20

python ${TAIGA_RUNTIME_DIR}/checkdb.py

DB_CHECK_STATUS=$?

if [ $DB_CHECK_STATUS -eq 1 ]; then
    echo "Failed to connect to database server."
    exit 1
elif [ $DB_CHECK_STATUS -eq 2 ]; then
    echo "Configuring initial database"
    python manage.py migrate --noinput
    python manage.py loaddata initial_user
    python manage.py loaddata initial_project_templates
    python manage.py loaddata initial_role
    python manage.py compilemessages
    python manage.py migrate taiga_contrib_slack
fi

python manage.py collectstatic --noinput

(sleep 10; echo "Starting circus"; chown -R taiga $TAIGA_HOME; /usr/local/bin/circusd $TAIGA_HOME/conf/circus.ini --daemon;)&

python manage.py runserver 0.0.0.0:8000 $@