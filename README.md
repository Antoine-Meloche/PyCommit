# PyCommit

A simple CLI utility to create uniform commits.

![Py Commit Logo](imgs/pycommit_logo.svg#gh-dark-mode-only)
![Py Commit Logo](imgs/pycommit_logo_light.svg#gh-light-mode-only)

![](https://img.shields.io/github/last-commit/Antoine-Meloche/PyCommit?style=for-the-badge)
![](https://img.shields.io/maintenance/yes/2022?style=for-the-badge)
![](https://img.shields.io/github/license/Antoine-Meloche/PyCommit?style=for-the-badge)
![](https://img.shields.io/github/v/release/Antoine-Meloche/PyCommit?style=for-the-badge)
![](https://img.shields.io/github/issues-raw/Antoine-Meloche/PyCommit?style=for-the-badge)
![](https://img.shields.io/github/languages/top/Antoine-Meloche/PyCommit?style=for-the-badge)

## Table of Contents
* [Usage](#usage)
    * [Track/Stage Changes](#track/stage-changes-in-working-directory)
    * [Commit Changes](#commit-staged-changes)
    * [Push commit](#push-commit-to-remote)
    * [All in one](#all-in-one)
* [Installation](#installation)
    * [Install from release](#install-from-releases)
        * [Linux](#linux-release)
        * [Windows](#windows-release)
        * [Mac](#mac-release)
    * [Install from source](#install-from-source)
        * [Linux](#linux)
        * [Windows](#windows)
        * [Mac](#mac)

# Usage

### Track/stage changes in working directory
PyCommit equivalent to 'git add .' to add all untracked files or unstaged changes to the current commit.

    pycommit add
or

    pycommit a
---
### Commit staged changes
PyCommit equivalent to 'git commit -m "Title" -m "Message"' to commit the staged changes to the current repository (local only).

    pycommit commit
or
    
    pycommit c
---
### Push commit to remote
PyCommit equivalent to 'git push -u "remote" "branch"' to push the commit to a remote.

    pycommit push
or

    pycommit p
---
### All in one
PyCommit equivalent to 'git add . && git commit -m "Title" -m "Message" && git push -u "remote" "branch"'

    pycommit
---
### Changing path of repo
PyCommit command argument '-p' is used to load a repo that is not in the current running directory.

    pycommit -p /path/to/repo

# Installation

## Install from releases

### Linux release
Available packages:

<!-- ✘ & ✔ -->

| Packaging type | status|
|:--------------:|:-----:|
|       AUR      |   ✘   |
|  Fedora (rpm)  |   ✘   |
|     Flatpak    |   ✘   |
|    AppImage    |   ✘   |
|      Snap      |   ✘   |

For more information visit the [Linux Releases Wiki Page](https://github.com/Antoine-Meloche/PyCommit/Wiki)

### Windows release

### Mac release

## Install from source

Refer to the [Install from source](https://github.com/Antoine-Meloche/PyCommit/wiki/Installation.md#install-from-source) section in the wiki.