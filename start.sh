#!/bin/bash

uvicorn apis.webhook.app.main:app --host 0.0.0.0 --port 9999 --reload &
uvicorn apis.storage.app.main:app --host 0.0.0.0 --port 9998 --reload &
uvicorn apis.streaming.app.main:app --host 0.0.0.0 --port 9997 --reload &

wait -n
