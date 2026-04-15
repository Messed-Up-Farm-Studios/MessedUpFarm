REPO_ROOT="$(git rev-parse --show-toplevel)"

RUFF_SOUND="$REPO_ROOT/.githooks/sounds/ruff.wav"

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