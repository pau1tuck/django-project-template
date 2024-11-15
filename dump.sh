#!/bin/bash

find . -path "./env" -prune -o -type f \( -name "*.py" -o -name "*.js" -o -name "*.css" -o -name "*.html" -o -name "*.yaml" -o -name "*.json" -o -name "*.conf" -o -name "*.txt" \) \
    -exec sh -c 'echo "\n==== $(basename {}) ====\n"; cat {}' \; > django-project-template-dump.txt
