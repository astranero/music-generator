#!/bin/bash

git checkout html-coverage
git checkout main -- htmlcov/

git add htmlcov/ 
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage

git checkout main
