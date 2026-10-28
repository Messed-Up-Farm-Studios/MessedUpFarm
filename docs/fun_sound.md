# Fun Sounds 🔊

Our git hooks and `make` commands play sounds while they run.

## One-time setup

Run these once after cloning, from the repo root:

```sh
# 1. Get the real .wav files (they are stored in Git LFS)
git lfs install
git lfs pull

# 2. Tell git to use our hooks
git config core.hooksPath .githooks

# 3. Install the server's Python tools
cd server
uv sync
```

Linux only: install `aplay` (`sudo apt install alsa-utils`). macOS and Windows (Git Bash) work out of the box.
