#!/bin/sh
find . -type f -name '*.zzz' -delete

git add .
git commit .
git push origin master
