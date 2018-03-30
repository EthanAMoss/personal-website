#!/bin/bash

if [[ -n $DEBUG && $DEBUG -ne 0 ]]; then
    python debug.py
    exit
fi

DEFAULT_WORKERS="$(($(nproc --all) + 1))"

gunicorn -w ${WORKERS:-"$DEFAULT_WORKERS"} -t 120 -b 0.0.0.0:80 emoss_website:app
