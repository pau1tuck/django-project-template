find . -type f \( -name "*.py" -name "*.js" -name "*.css" -name "*.html" -name "*.png" -o  \) -exec sh -c 'echo "\n==== $(basename {}) ====\n"; cat {}' \; > project_dump.txt
