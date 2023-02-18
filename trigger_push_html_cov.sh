#!/bin/bash

git checkout html-coverage
git checkout master -- html-coverage
git add html-coverage/*
git commit -m "adding 'html-coverage' directory from 'master' branch to the GitHubs Actions." 
git push origin html-coverage
git rm -r html-coverage
