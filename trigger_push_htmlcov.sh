#!/bin/bash
git stash 
git checkout html-coverage
git stash pop

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
