export APP_MODULE=${APP_MODULE-src.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}

uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"