find . -type f \( -name "*.py" -name "*.js" -name "*.css" -name "*.html" -o  \) -exec sh -c 'echo "\n==== $(basename {}) ====\n"; cat {}' \; > django-project-template-dump.txt
