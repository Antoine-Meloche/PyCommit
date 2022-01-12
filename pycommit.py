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
import sys
from git import Repo
from git.exc import GitCommandError

print("""
PyCommit  Copyright (C) 2022  Antoine Meloche
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions. For details visit https://www.gnu.org/licenses/
""")


class colors:
    RED = "\033[91m"
    RESETC = "\033[0m"


class PyCommit:
    path_to_repo = "./"

    def __init__(self):
        self.find_directory()
        self.load_repo()

    def find_directory(self):
        if len(sys.argv) != 1:
            try:
                self.path_to_repo = sys.argv[sys.argv.index("-p")]
            except ValueError:
                pass

    def load_repo(self):
        self.repo = Repo(self.path_to_repo)

        if not self.repo.bare:
            print(f"Repo loaded at {self.path_to_repo}:")
            print(f"    Description: {self.repo.description}")
            print(f"    Active Branch: {self.repo.active_branch}")
            for remote in self.repo.remotes:
                print(f"    Remote '{remote}' at '{remote.url}'")

            if self.repo.git.status("--short") == "":
                print(
                    f"{colors.RED}ERROR: No changes detected in working tree{colors.RESETC}")
                sys.exit(1)

    def stage_changes(self):
        self.repo.git.add(".")
        print("  ➜ Changes staged")

    def verify_staged(self):
        if self.repo.git.diff("--cached", "--shortstat") == "":
            print(f"{colors.RED}ERROR: No changes are currently staged")
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
            "Which corresponds to the type of your commit: ")

        try:
            int(commitTypeChoice)
        except:
            print(f"{colors.RED}ERROR: Input was not a number{colors.RESETC}")
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

    def commit_verif(self):
        print(f"""
    {self.title}
        {self.body}
    author: {self.repo.git.config("--get", "user.name")}
    email: {self.repo.git.config("--get", "user.email")}
    """)
        isReviewed = input("Are the information fields correct? [Y/n] ")

        if (isReviewed.lower() not in ["", "y", "yes"]):
            print(f"{colors.RED}Commit cancelled{colors.RESETC}")
            sys.exit(1)

    def commit(self):
        self.repo.git.commit("-m", self.title, "-m", self.body)
        print("  ➜ Commited")

    def choose_remote(self):
        if len(self.repo.remotes) == 0:
            print(
                f"{colors.RED}ERROR: Pushing to remote is impossible; no remote located{colors.RESETC}")

        if len(self.repo.remotes) > 1:
            for i in range(len(self.repo.remotes)):
                print(
                    f"[{i}]: {self.repo.remotes[i]} at {self.repo.remotes[i].url}")

            try:
                self.remote = self.repo.remotes[int(
                    input("Which remote would you like to push to: "))]
            except ValueError:
                print(f"{colors.RED}ERROR: Input was not a number{colors.RESETC}")
                sys.exit(1)
        else:
            self.remote = self.repo.remotes[0]

    def push(self):
        try:
            self.repo.git.push("-u", self.remote, self.repo.active_branch)
        except GitCommandError:
            print(
                f"{colors.RED}ERROR: Remote repository is offline or does not exist{colors.RESETC}")
        print(f"  ➜ Pushed to {self.remote} at {self.remote.url}")

    def all(self):
        self.stage_changes()
        self.commit_message()
        self.commit_verif()
        self.commit()
        self.choose_remote()
        self.push()

    def add(self):
        self.stage_changes()

    def commit_only(self):
        self.verify_staged()
        self.commit_message()
        self.commit()

    def push_only(self):
        self.choose_remote()
        self.push


if __name__ == "__main__":
    pycommit = PyCommit()
    if len(sys.argv) == 1:
        pycommit.all()
    elif len(sys.argv) == 2:
        with sys.argv[1] as arg:
            if arg == ("a" or "add"):
                pycommit.add()
            elif arg == ("c" or "commit"):
                pycommit.commit_only()
            elif arg == ("p" or "push"):
                pycommit.push_only()
            else:
                args = arg.split('')
                for arg in args:
                    if arg == "a":
                        pycommit.add()
                    elif arg == "c":
                        pycommit.commit_only()
                    elif arg == "p":
                        pycommit.push_only()
                    else:
                        print(
                            f"{colors.RED}ERROR: Invalid argument: {sys.argv[1]}{colors.RESETC}")
                        sys.exit(1)
    else:
        for arg in sys.argv[1:]:
            if arg == ("a" or "add"):
                pycommit.add()
            elif arg == ("c" or "commit"):
                pycommit.commit_only()
            elif arg == ("p" or "push"):
                pycommit.push_only()
            else:
                try:
                    p_index = sys.argv.index("-p")
                except IndexError:
                    pass

                if arg != ("p" or sys.argv[p_index+1]):
                    print(
                        f"{colors.RED}ERROR: Invalid argument: {arg}{colors.RESETC}")
                    sys.exit(1)
