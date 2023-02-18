#!/bin/bash
FILES = "$pwd/htmlcov/*"
git checkout html-coverage
git checkout main -- htmlcov

for file in $FILES
do 
    echo "$file"
done

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
