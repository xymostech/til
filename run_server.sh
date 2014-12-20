#!/usr/bin/env bash

set -e

gunicorn --bind '127.0.0.1:8472' \
         --daemon \
         --pid server.pid \
         app:app
