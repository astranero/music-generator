#!/bin/bash

git checkout html-coverage
git checkout main -- Documentation/

for file in $pwd/Documentation/
do 
    cp $file ./
    echo pwd
done



rm -r Documentation/

git add .
git commit -m "adding 'htmlcov' directory from 'main' branch to the GitHubs Actions." 
git push origin html-coverage
git checkout main
