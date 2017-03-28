# Cheatsheet for Git

Git is a version control tool. Each commit is taking a snapshot of your work so far which enables you to go back in time to older versions of your program. You will most certainly find
yourself in a situation where you had some working code, modified it to add a new
feature or work out some kink, only to find that you've hopelessly ruined everything and
would give your left index finger just to get back to what you had before. Enter
git.

## Objectives

1. Be familiar with [key concepts](#key-concepts)
2. Know the [git workflow](#git-workflow)
3. Have prior exposure to [key commands](#key-commands)

## Study Material

### Key concepts

* Repository (a folder managed by git)
* Workspace (current state)
* Index (staged for commit)
* Commit (take a snapshot)
* Branch (a series of commits)
* Remote (a remote repository that you can push to or pull from)

Any folder can be turned into a git repository with `git init`. Your
**workspace** is the current state of all your files. Some of them will be
different from what was last committed. You can see what's different by running
`git status`. From your workspace, you can use the `git add` command to add
files to the index, which is a sort of staging area for commits. When you run
`git commit`, the files in your index are included in the commit snapshot. You
can use `git reset` to roll back to prior commits and you can use `git log` to
see the history of commits.

### git workflow

1. Choose a feature/segment/thing to work on next
2. Write some code
3. Play with the code
4. Rewrite, play some more, etc.
5. `git add .`: add all your changes to the index
6. `git commit -m "Describe the work you just did"`
7. Repeat

### Key commands

* `git status`: see the status of the workspace, index, and what branch you're
  on
* `git add`: add files to the index (commit staging area)
* `git commit`: take a snapshot of the project, committing the files in the
  index
* `git checkout`: switch to a different branch (use the `-b` option to switch to
  a new branch)
* `git branch`: list the branches
* `git reset`: rollback to a previous commit
* `git push`: push up the changes in a local repository to a remote repository
* `git pull`: pull down the changes from a remote repository to the local
  repository
* `git clone`: copy a remote repository to the local machine
