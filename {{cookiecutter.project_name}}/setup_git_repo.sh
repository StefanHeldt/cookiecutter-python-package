#!/bin/bash 

# taken from https://www.viget.com/articles/create-a-github-repo-from-the-command-line
repo_name=$1

dir_name=`basename $(pwd)`


if [ "$repo_name" = "" ]; then
    echo "Repository name (hit enter to use '$dir_name')?"
    read repo_name
fi

if [ "$repo_name" = "" ]; then
repo_name=$dir_name
fi

user_name=`git config github.user`
if [ "$user_name" = "" ]; then
    echo "Could not find username, run 'git config --global github.user <username>'"
    invalid_credentials=1
fi

if [ "$invalid_credentials" == "1" ]; then
    exit 1
fi

if ! command -v gh &> /dev/null 2>&1
then
    echo "Could not find GitHub CLI, attempting to install..."
    brew install gh
fi

if ! gh auth status >/dev/null 2>&1
then
    echo "You need to login to GitHub."
    gh auth login
fi

echo -n "Creating local Github repository '$repo_name' ..."
git init .
git add .
git commit -m "initial setup"
git branch -M master
echo "Done!"

echo -n "Creating remote Github repository '$repo_name' ..."
gh repo create $repo_name --private --source=. --remote=upstream
echo " done."

echo -n "Pushing code to remote ..."
git remote add origin https://github.com/$user_name/$repo_name.git > /dev/null 2>&1
git push -u origin master > /dev/null 2>&1
echo "Done!"
