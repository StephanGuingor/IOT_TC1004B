#!/usr/bin/env bash

diff="$1"
tmpdir="tmp"
packages_to_test=$(git diff --name-status "$diff" | grep -E '^(A|R|M).*\.py$' | awk '{print $NF}' | xargs -n1 dirname | sort -u)
exit_code=0

mkdir -p $tmpdir
for package in $packages_to_test; do
    echo "Testing $package..."
    pytest --cov=$package --cov-branch &> $tmpdir/.res
    cov=$(cat $tmpdir/.res | grep TOTAL | awk '{print $NF}' | tr '%' '\0')
    cat $tmpdir/.res
    if [ $cov -lt 80 ]; then
        echo -e "\033[33mCoverage not pasing...\033[0m"
        exit_code=1
    fi

    if [ $? != 0 ]; then
        exit_code=1
    fi
done;


rm .coverage

exit $exit_code
