#!/usr/bin/env python
"""Script is run after cookiecutter creates repository."""
import os


repo_name = '{{ cookiecutter.project_name }}'
setup_git = True if '{{ cookiecutter.setup_git_repo }}' == "Yes" else False

if setup_git:
    err = os.system('bash ./setup_git_repo.sh %s' %repo_name)
    if err:
        print("Error with GitHub repository setup!")
    

os.system("cd %s" %repo_name)
os.remove("./setup_git_repo.sh")
