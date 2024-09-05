#!/bin/bash

psql -h postgres -U postgres -d dbc -f /api/schema.sql

uvicorn webhook.app.main:app --host 0.0.0.0 --port 9999 --reload &
uvicorn storage.app.main:app --host 0.0.0.0 --port 9998 --reload &
# uvicorn streaming.app.config:app --host 0.0.0.0 --port 9997 --reload &

wait -n