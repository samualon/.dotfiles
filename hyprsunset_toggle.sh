#!/bin/bash


# Get current user
USER=$(whoami)

# Detect if gammastep is running
if pgrep -u "$USER" -x hyprsunset > /dev/null; then
    pkill -x hyprsunset
else
    hyprsunset > /dev/null 2>&1 &

    # Optional: disown so it doesn't get killed with the terminal
    disown
fi

