if [ -z ${SCRIPT_PATH+x} ]; then
  echo "This script is not meant to be executed on its own."
  exit 1
fi

function run_backend {
    echo "    Running ${YELLOW}backend$RESET"
    echo ""

    if [[ $IS_CEDRIK_SERVER -eq 1 ]]; then
        pipenv run uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    else
        pipenv run uvicorn app:app --reload
    fi
}

function run_frontend {
    echo "    Running ${YELLOW}frontend$RESET"
    echo ""

    if [[ $IS_CEDRIK_SERVER -eq 1 ]]; then
        cd $SCRIPT_PATH/frontend && pnpm dev --host 0.0.0.0
    else
        cd $SCRIPT_PATH/frontend && pnpm dev
    fi
}

