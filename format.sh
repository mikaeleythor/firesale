#!/bin/zsh


PYFILES="$(find | cut -c3- | grep \.py$ | awk '! /^\.venv|migration/')"
DJHTMLFILES="$(find | cut -c3- | grep \.html$ | awk '! /^\.venv/')"
JSFILES="$(find | cut -c3- | awk '/\.js$/' | awk '! /^\.venv|admin/')"

autopep() {
    echo "$@" | xargs -I pattern autopep8 -i --experimental -a --max-line-length 80 pattern
}

djlint() {
    echo "$@" | xargs -I pattern python3 -m djlint --indent 2 --reformat pattern
}

prettier() {
    echo "$@" | xargs -I pattern npx prettier -w pattern
}

autopep $PYFILES
djlint $DJHTMLFILES
prettier $JSFILES
