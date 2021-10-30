#!/usr/bin/env bash

diff=$1

files_to_lint=`git diff --name-status $diff | grep -E '^(A|R|M).*\.py$' | awk '{print $NF}'`

exit_code=0
for file in $files_to_lint; do
    echo "Linting $file..."
    diff=`pylint $file --score=n --msg-template='{path}:{line}:{column}: {msg} ({symbol})' | grep -vE '^\*'`
    if [ `echo -n "$diff" | wc -l` != "0" ]; then
        echo -e "\033[36m$diff\033[0m"
        exit_code=1
    fi
done;

exit $exit_code
