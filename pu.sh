#!/bin/sh
find . -type f -name '*.zzz' -delete

git add .
git commit .
git push origin master

## automagically updates the server side as well. Remember to add the SSH key
## for this machine if you plan on doing this.
ssh Vostok@ssh.pythonanywhere.com
pull
exit
