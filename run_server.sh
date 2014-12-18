#!/usr/bin/env bash

set -e

gunicorn --reload --bind '127.0.0.1:8472' -D app:app
