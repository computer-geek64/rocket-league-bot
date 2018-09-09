# Git.py
# Ashish D'Souza
# September 8th, 2018

import git


def fetch(repository_name):
    git.Repo(repository_name).git.fetch()


def status(repository_name):
    return git.Repo(repository_name).git.status()


def pull(repository_name):
    git.Repo(repository_name).git.pull()


def is_up_to_date(repository_name):
    return "behind" not in status(repository_name)
