#!/bin/bash

git checkout html-coverage
git checkout main -- htmlcov
git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
git rm -rf htmlcov
git add .
git commit -m "Remove unnecessary htmlcov files from the 'main' branch."
git push origin main