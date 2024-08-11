#!/usr/bin/env -S just --justfile
set dotenv-load

venv := ".tox/lint"

SERVER_PARAMS := "--ws-ping-interval 5 --ws-ping-timeout 2"
HTTP_PORT := "8000"

run debug="1":
    {{venv}}/bin/uvicorn apiserver.routes:app {{SERVER_PARAMS}} --port {{HTTP_PORT}}

client:
    flutter run
