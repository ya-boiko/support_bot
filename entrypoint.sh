#!/bin/sh

. .venv/bin/activate

uvicorn --host 0.0.0.0 app.main:create_app
