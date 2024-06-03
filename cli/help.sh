if [ -z ${SCRIPT_PATH+x} ]; then
  echo "This script is not meant to be executed on its own."
  exit 1
fi

function show_help {
    cat <<EOF
$BOLD${UNDERLINE}Usage$RESET:
    $0 $YELLOW<command> $MAGENTA[options]$RESET

$BOLD${UNDERLINE}Commands$RESET:
    ${YELLOW}backend$RESET                Run the backend.
    ${YELLOW}frontend$RESET               Run the frontend.
EOF
}

