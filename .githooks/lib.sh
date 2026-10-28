REPO_ROOT="$(git rev-parse --show-toplevel)"
SERVER_DIR="$REPO_ROOT/server"
SRC="src/server src/model"

SOUNDS="$REPO_ROOT/.githooks/sounds"
RUFF_SOUND="$SOUNDS/ruff.wav"
BUILD_SOUND="$SOUNDS/building.wav"
BLACK_SOUND="$SOUNDS/black.wav"

# PID of the last queued sound, so the next one waits its turn
LAST_SOUND_PID=""

# Let queued sounds finish before the hook exits, otherwise the last one is cut off
trap 'wait' EXIT

play_sound() {
    SOUND="$1"

    case "$(uname -s)" in
        Darwin)
        afplay "$SOUND"
        ;;
        Linux)
        aplay -q "$SOUND"
        ;;
        MINGW*|MSYS*|CYGWIN*)
        powershell -NoProfile -c "(New-Object Media.SoundPlayer '$(cygpath -w "$SOUND")').PlaySync();"
        ;;
        *)
        echo "No sound support for OS: $(uname -s)"
        ;;
    esac
}

# Play sounds in the background, one after another
enqueue_sound() {
    sound="$1"
    prev="$LAST_SOUND_PID"

    if [ ! -f "$sound" ]; then
        echo "Missing sound: $sound" >&2
        return
    fi

    (
        if [ -n "$prev" ]; then
            while kill -0 "$prev" 2>/dev/null; do sleep 0.1; done
        fi
        play_sound "$sound"
    ) >/dev/null 2>&1 &

    LAST_SOUND_PID=$!
}

# Print one random file from the arguments (pass a glob)
pick_random() {
    i=$(awk -v n=$# 'BEGIN { srand(); print int(rand() * n) + 1 }')
    eval echo "\"\${$i}\""
}

pick_random_success_sound() {
    pick_random "$SOUNDS"/success/*.wav
}

pick_random_failure_sound() {
    pick_random "$SOUNDS"/fail/fail*.wav
}

pick_random_no_sound() {
    pick_random "$SOUNDS"/fail/no*.wav
}
