#!/bin/bash
git stash save
git checkout html-coverage
git checkout main -- html-coverage/

for file in $pwd/htmlcov/
do 
    echo $file
done

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
git stash pop
