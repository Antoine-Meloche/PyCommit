#!/usr/bin/python

"""
Copyright (C) 2022  Antoine Meloche

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
from git import Repo

print("""
PyCommit  Copyright (C) 2022  Antoine Meloche
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions. For details visit https://www.gnu.org/licenses/
""")

repo = Repo("./")

if not repo.bare:
    print(f"Repo loaded at {os.getcwd()}:")
    print(f"    Description: {repo.description}")
    print(f"    Active Branch: {repo.active_branch}")
    for remote in repo.remotes:
        print(f"    Remote '{remote}' at '{remote.url}'")

    if repo.git.status("--short") == "":
        print("No changes detected in working tree")
        quit()

    isAdd = input(
        "\nShould all the changes be staged for the commit? [Y/n] ")

    if (isAdd.lower() in ["", "y", "yes"]):
        repo.git.add(".")
        print("  ➜ Changes staged")

    print("""
[1] BUGFIX: fixed a bug
[2] FEAT: added a feature
[3] REFAC: code refactoring
[4] DOCS: change to documentation only
[5] STYLE: change to formatting only
[6] TEST: change, addition to tests only
[7] Custom
    """)
    commitTypes = ["", "BUGFIX: ", "FEAT: ", "REFAC: ", "DOCS: ", "STYLE: ", "TEST: "]

    commitTypeChoice = input("Which corresponds to the type of your commit: ")
    try:
        int(commitTypeChoice)
    except:
        print("Input was not a number")
        quit()

    if commitTypeChoice == "7":
        title = input("Title: ")
    else:
        print("Enter your title:")
        title = commitTypes[int(commitTypeChoice)]+input(f"{commitTypes[int(commitTypeChoice)]}")

    body = input("Enter the body of your commit (optional): ")

    print(f"""
{title}
    {body}
author: {repo.git.config("--get", "user.name")}
email: {repo.git.config("--get", "user.email")}
    """)

    isReviewed = input("Are the information fields correct? [Y/n] ")

    if (isReviewed.lower() not in ["", "y", "yes"]):
        print("Commit cancelled")
        quit()

    repo.git.commit("-m", title, "-m", body)
    print("  ➜ Commited")

    isPush = input("Do you want this commit to be pushed to a remote? [Y/n] ")

    if (isReviewed.lower() not in ["", "y", "yes"]):
        print("Push cancelled")
        quit()

    if len(repo.remotes) == 0:
        print("Pushing to remote is impossible, no remote located")
        quit()

    if len(repo.remotes) > 1:
        for i in range(len(repo.remotes)):
            print(f"[{i}]: {repo.remotes[i]} at {repo.remotes[i].url}")
        try:
            remote = repo.remotes[int(input("Which remote would you like to choose: "))]
        except:
            print("Input was not a number")
            quit()
    else:
        remote = repo.remotes[0]
    
    repo.git.push("-u", remote, repo.active_branch)
    print(f"  ➜ Pushed to {remote} at {remote.url}")

else:
    print(f"could not load repository in current directory: {os.getcwd()}")

