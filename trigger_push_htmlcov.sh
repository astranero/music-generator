#!/bin/bash
git checkout html-coverage
git checkout main -- Documentation/

echo $pwd


git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
git stash pop
