#!/bin/sh

git pull origin master

echo "> pull complete"

git add .

echo "> add all files"

if [ $# -eq 0 ]; then
    read -p "> enter commit message : " COMMIT_MESSAGE
else
    COMMIT_MESSAGE=${1}
fi

git commit -m "${COMMIT_MESSAGE}"

echo "> commit complete"

git push origin master

echo "> push complete"