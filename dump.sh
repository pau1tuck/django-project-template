find . -type f \( -name "*.py" -name "*.js" -name "*.css" -name "*.html" -name "*.yaml" -o  \) -exec sh -c 'echo "\n==== $(basename {}) ====\n"; cat {}' \; > django-project-template-dump.txt
