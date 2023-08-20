PRE_START_PATH=${PRE_START_PATH:-./prestart.sh}  # 2
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

export APP_MODULE=${APP_MODULE-src.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}
# export BACKEND_CORS_ORIGINS=${BACKEND_CORS_ORIGINS}

uvicorn --host $HOST --port $PORT "$APP_MODULE"