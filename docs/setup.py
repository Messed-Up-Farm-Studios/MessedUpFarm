import subprocess

subprocess.run(["git", "config", "core.hooksPath", ".githooks"])

print("Set Up Finish! ")
