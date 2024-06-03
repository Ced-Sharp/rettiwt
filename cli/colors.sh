if [ -z ${SCRIPT_PATH+x} ]; then
  echo "This script is not meant to be executed on its own."
  exit 1
fi

BOLD=$(tput bold)
UNDERLINE=$(tput smul)
INVERT=$(tput rev)
RESET=$(tput sgr0)
BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)
WHITE=$(tput setaf 7)
BG_RED=$(tput setab 1)
BG_GREEN=$(tput setab 2)
BG_YELLOW=$(tput setab 3)
BG_BLUE=$(tput setab 4)
BG_MAGENTA=$(tput setab 5)
BG_CYAN=$(tput setab 6)
BG_WHITE=$(tput setab 7)

# Small helpers
DONE="    $GREEN$INVERT Done! $RESET"
ERROR="    $BG_RED$YELLOW Error! $RESET"

