#!/bin/bash

git switch html-coverage
git show main:htmlcov > .
git show main:.coverage > .

for file in htmlcov
do 
    cp file .
done


git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
