#!/bin/bash

git checkout html-coverage
git checkout main -- htmlcov

for file in $pwd/htmlcov
do 
    cp $file ./
    echo pwd
done

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
