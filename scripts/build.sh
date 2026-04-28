#!/bin/bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
BUILD_SOUND="$REPO_ROOT/.githooks/sounds/building.wav"

play_sound() {
    SOUND="$1"

    OS="$(uname -s)"

    case "$OS" in 
        Darwin)
        afplay "$SOUND" &
        ;;
        Linux)
        aplay "$SOUND" &
        ;;
        MINGW*|MSYS*|CYGWIN*)
        powershell -c "(New-Object Media.SoundPlayer \"$SOUND\").PlaySync();" &
        ;;
        *)
        echo "No sound support for OS: $OS"
        ;;
    esac
}

cd "$REPO_ROOT"

play_sound  "$BUILD_SOUND"
echo "Building..."

pyinstaller main.py \
  --name MessedUpFarm \
  --onefile \
  --add-data "client/src/assets;client/src/assets" \
  --windowed  # DEBUG by commenting out this line
  
