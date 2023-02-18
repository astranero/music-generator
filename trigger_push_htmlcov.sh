#!/bin/bash

git switch html-coverage
git show main:htmlcov > htmlcov
git show main:.coverage > .coverage

for file in htmlcov
do 
    cp file ./
    echo pwd
done

rm -r htmlcov

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
