# Git.py
# Ashish D'Souza
# September 7th, 2018

import git
import os


def fetch(repository_name):
    repository = git.Repo(repository_name)
    repository.git.fetch()
    # git.Repo(repository_name).git.fetch()


def status(repository_name):
    return git.Repo(repository_name).git.status()


def pull(repository_name):
    git.Repo(repository_name).git.pull()


def is_up_to_date(repository_name):
    return "behind" not in status(repository_name)


def push():
    repository = git.Repo("/root/Documents/git/rocket-league-bot")
    repository.git.add("/root/Documents/git/rocket-league-bot/settings.txt")
    # repository.git.commit("-m", "Update settings.txt")
    # repository.git.push()
    os.chdir("/root/Documents/git/rocket-league-bot")
    print("hey")
    os.system("git push")
