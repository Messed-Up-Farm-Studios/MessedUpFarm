REPO_ROOT="$(git rev-parse --show-toplevel)"
REPO_NAME="$(basename "$REPO_ROOT")"

SOUND_QUEUE="/tmp/git_sound_queue_${REPO_NAME}"
PID_FILE="/tmp/git_sound_worker_${REPO_NAME}.pid"


RUFF_SOUND="$REPO_ROOT/.githooks/sounds/ruff.wav"
BUILD_SOUND="$REPO_ROOT/.githooks/sounds/building.wav"

start_sound_worker() {

    if [ -f "$PID_FILE" ]; then
        PID="$(cat "$PID_FILE")"

        if kill -0 "$PID" 2>/dev/null; then
            return
        else
            rm -f "$PID_FILE"
        fi
    fi

    # Create fifo if missing
    if [ ! -p "$SOUND_QUEUE" ]; then
        mkfifo "$SOUND_QUEUE"
    fi

    # Start Worker
    (
        while read -r sound < "$SOUND_QUEUE"; do
            [ -f "$sound" ] && play_sound "$sound"
            done
    ) &

    echo $! > "$PID_FILE"
}

play_sound() {
    SOUND="$1"

    OS="$(uname -s)"

    case "$OS" in 
        Darwin)
        afplay "$SOUND" 
        ;;
        Linux)
        aplay "$SOUND"
        ;;
        MINGW*|MSYS*|CYGWIN*)
        powershell -c "(New-Object Media.SoundPlayer \"$SOUND\").PlaySync();"
        ;;
        *)
        echo "No sound support for OS: $OS"
        ;;
    esac
}

pick_random_success_sound() {
    rand=$((RANDOM % 2 + 1))
    success_sound="success$rand.wav"
    success_path="$REPO_ROOT/.githooks/sounds/success/$success_sound"
    echo "$success_path"
}

pick_random_failure_sound() {
    rand=$((RANDOM % 2 + 1))
    fail_sound="fail$rand.wav"
    fail_path="$REPO_ROOT/.githooks/sounds/fail/$fail_sound"
    echo "$fail_path"
}

pick_random_no_sound() {
    rand=$((RANDOM % 2 + 1))
    fail_sound="no$rand.wav"
    fail_path="$REPO_ROOT/.githooks/sounds/fail/$fail_sound"
    echo "$fail_path"
}

enqueue_sound() {
    echo "$1" > "$SOUND_QUEUE"
}

start_sound_worker
