#!/bin/bash

for py in Task*.py; do
  if [[ -f "$py" ]]; then
    echo
    echo -e "\e[33mRunning: $py\e[0m"
    echo
    python3 "$py"
  fi
done
