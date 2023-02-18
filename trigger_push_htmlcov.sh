#!/bin/bash

git checkout html-coverage
git checkout main -- .coverage

git add .coverage
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
