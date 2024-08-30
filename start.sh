#!/bin/bash

uvicorn webhook.app.main:app --host 0.0.0.0 --port 9999 --reload &
uvicorn storage.app.main:app --host 0.0.0.0 --port 9998 --reload &
uvicorn streaming.app.main:app --host 0.0.0.0 --port 9997 --reload &

wait -n
