# git config core.hooksPath .githooks

import os
import sys
import random
import platform
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def play_sound(audio):
    if not os.path.exists(audio):
        print(audio)
        print("Sound files not found. :(")
        return

    system = platform.system()
    if system == "Windows":
        subprocess.Popen(["powershell", "-c", f"(New-Object Media.SoundPlayer '{audio}').PlaySync();"])
    elif system == "Linux":
        subprocess.Popen(["aplay", audio])
    elif system == "Darwin":
        subprocess.Popen(["afplay", audio])

def handle_pre_push_result(audio_path, exit_code):
    play_sound(audio_path)
    sys.exit(exit_code)

def pre_push_steps():
    # Run Tests
    # Check Build
    return True

if pre_push_steps():
    # pre-push passed
    success_audio = os.path.join(BASE_DIR, "sounds", "success", f"success{random.randint(1, 2)}.wav")
    handle_pre_push_result(success_audio, 0)
else:
    # pre-push failed
    fail_audio = os.path.join(BASE_DIR, "sounds","fails", f"fail{random.randint(1, 3)}.wav")
    handle_pre_push_result(fail_audio, 1)
