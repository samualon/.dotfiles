#/bin/bash
systemd-analyze | grep 'Startup finished' | awk -F= '{print $2}' | sed 's/^[ \t]*//;s/[ \t]*$//'
