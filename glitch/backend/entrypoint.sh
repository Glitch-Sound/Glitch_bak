#!/bin/sh

if [ "$MODE" = "production" ]; then
  uvicorn main:app --host 0.0.0.0 --port $BACKEND_PORT
else
  uvicorn main:app --host 0.0.0.0 --port $BACKEND_PORT --reload
fi
