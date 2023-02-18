#!/bin/bash
git checkout html-coverage
git checkout main -- htmlcov

FILES="$PWD/htmlcov/*"
for file in $FILES
do 
    echo "$file"
done

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
