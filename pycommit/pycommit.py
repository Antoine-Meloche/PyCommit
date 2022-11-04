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

import sys
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError


class Colors:
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESETC = "\033[0m"


class PyCommit:
    path_to_repo = "./" # Default path to repo is the current working directory

    def __init__(self):
        print("""
        PyCommit  Copyright (C) 2022  Antoine Meloche
            This program comes with ABSOLUTELY NO WARRANTY;
            This is free software, and you are welcome to redistribute it
            under certain conditions. For details visit https://www.gnu.org/licenses/
        """)
        self.find_directory() # Find directory for git repo if indicated in command
        self.load_repo() # Load the git repo using the repo path

    def find_directory(self):
        if len(sys.argv) == 1: # If no flags are set in command skip process
            return
        try:
            self.path_to_repo = sys.argv[sys.argv.index("-p")]
        except ValueError: # If no repo is set in the command
            pass

    def load_repo(self):
        try:
            self.repo = Repo(self.path_to_repo) # Open repo using path
        except InvalidGitRepositoryError:
            print(f"{Colors.RED}ERROR: Invalid git repository{Colors.RESETC}")

        if self.repo.bare: # If repo is bare skip printing non existing info
            return

        print(f"Repo loaded at {self.path_to_repo}:")
        print(f"    Description: {self.repo.description}")
        print(f"    Active Branch: {self.repo.active_branch}")

        for remote in self.repo.remotes:
            print(f"    Remote '{remote}' at '{remote.url}'")

        if self.repo.git.status("--short") == "": # Check if changes exist in git repo
            print(
                f"{Colors.RED}ERROR: No changes detected in working tree{Colors.RESETC}")
            sys.exit(1)

    def stage_changes(self):
        self.repo.git.add(".")
        print("  ➜ Changes staged")

    def verify_staged(self):
        if self.repo.git.diff("--cached", "--shortstat") == "": # Check if changes are staged
            print(f"{Colors.RED}ERROR: No changes are currently staged")
            sys.exit(1)

    def commit_message(self):
        print("""
    [1] BUGFIX: fixed a bug
    [2] FEAT: added a feature
    [3] REFAC: code refactoring
    [4] DOCS: change to documentation only
    [5] STYLE: change to formatting only
    [6] TEST: change, addition to tests only
    [7] Custom
    """)
        commitTypeChoice = input(
            "Which corresponds to the type of your commit (1-7): ")

        try:
            int(commitTypeChoice)
        except:
            print(f"{Colors.RED}ERROR: Input was not a number{Colors.RESETC}")
            sys.exit(1)

        if commitTypeChoice < 1 or commitTypeChoice > 7: # Make sure the choice of commit type is valid
            print(f"{Colors.RED}ERROR: Input is not valid (Not within range 1-7){Colors.RESETC}")
            sys.exit(1)

        commitTypes = ["", "BUGFIX: ", "FEAT: ",
                       "REFAC: ", "DOCS: ", "STYLE: ", "TEST: "]

        if commitTypeChoice == "7":
            self.title = input("Title: ")
        else:
            print("Enter your title:")
            self.title = commitTypes[int(commitTypeChoice)] + \
                input(f"{commitTypes[int(commitTypeChoice)]}")

        self.body = input("Enter the body of your commit (optional): ")

    def commit_verif(self): # User verification of commit information
        print(f"""
    {self.title}
        {self.body}
    author: {self.repo.git.config("--get", "user.name")}
    email: {self.repo.git.config("--get", "user.email")}
    """)
        isReviewed = input("Are the information fields correct? [Y/n] ")

        if (isReviewed.lower() not in ["", "y", "yes"]):
            print(f"{Colors.YELLOW}Commit cancelled{Colors.RESETC}")
            sys.exit(1)

    def commit(self): # Commit the changes to repo
        self.repo.git.commit("-m", self.title, "-m", self.body)
        print("  ➜ Commited")

    def choose_remote(self): # Select remote to push to if many exist
        if len(self.repo.remotes) == 0:
            print(
                f"{Colors.RED}ERROR: Pushing to remote is impossible; no remote located{Colors.RESETC}")
            sys.exit(1)

        if len(self.repo.remotes) > 1:
            for i in range(len(self.repo.remotes)):
                print(
                    f"[{i}]: {self.repo.remotes[i]} at {self.repo.remotes[i].url}")

            try:
                self.remote = self.repo.remotes[int(
                    input("Which remote would you like to push to: "))]
            except ValueError:
                print(f"{Colors.RED}ERROR: Input was not a number{Colors.RESETC}")
                sys.exit(1)
            except IndexError:
                print(f"{Colors.RED}ERROR: Input was not valid (Not in range 0-{len(self.repo.remotes)}{Colors.RESETC})")
                sys.exit(1)
        else:
            self.remote = self.repo.remotes[0]

    def push(self): # Push commit to selected repo
        try:
            self.repo.git.push("-u", self.remote, self.repo.active_branch)
        except GitCommandError:
            print(
                f"{Colors.RED}ERROR: Remote repository is offline or does not exist{Colors.RESETC}")
            sys.exit(1)

        print(f"  ➜ Pushed to {self.remote} at {self.remote.url}")

    def all(self): # pycommit command wihtout flags or including -p
        self.stage_changes()
        self.commit_message()
        self.commit_verif()
        self.commit()
        self.choose_remote()
        self.push()

    def add(self): # pycommit [a, add] command
        self.stage_changes()

    def commit_only(self): # pycommit [c, commit] command
        self.verify_staged()
        self.commit_message()
        self.commit()

    def push_only(self): # pycommit [p, push] command
        self.choose_remote()
        self.push
