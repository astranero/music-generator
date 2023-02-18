#!/bin/bash

git checkout html-coverage
git checkout master -- htmlcov
git add htmlcov/*
git commit -m "adding 'htmlcov' directory from 'master' branch to the GitHubs Actions." 
git push origin html-coverage
git rm -r htmlcov
