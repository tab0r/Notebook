# Chapter 0:  Galvanize Tools and Workflow

### This is an introduction to the tools and workflow we use during the course.

___________________________________

## Learning Objectives

1. [Install a text editor (Atom)](#text_editor)

2. [Install and use a Terminal (iTerm2)](#terminal)

3. [Install Anaconda](#anaconda)

4. [Running a Python script from the Terminal](#developing)

5. [Version control with Git and GitHub](#git)

6. [Know the Galvanize workflow](#workflow)

___________________________________

## Main resources

  - Cheatsheet n°1: [Basic Command Line](resources/command_line_basics.md)
  - Cheatsheet n°2: [Git Key Concepts](resources/git_keyconcepts.md)
  - Cheatsheet n°3: [Keyboard Shortcuts](resources/keyboard_shortcuts.md)

Further resources are available in each section if you wish to dig a little deeper.

___________________________________

## Assignment

Instructors will be able to help you set up on MacOs. If you want to use Linux, the latest Ubuntu version should work. Some notes are included in various sections of this chapter to guide you in a Linux environment.

<a name="text_editor">
### 1. Install a Text Editor (Atom)
</a>

During the course, we will use Atom, as it is free and works across operating systems. You can dowloaded here: https://atom.io/.

In Atom file menu, select 'Install Shell Commands'. This step will make more sense once you have gone through the next section.

NB: you can make many types of files in Atom (.sql, .py, .csv ...)

Learning and using a programming editor is a foundational skill.  If you know `vi` or `emacs`, continue to use them.  If you haven't mastered them, then `Atom` is a good option.  Editors are a personal choice and the source of bitter religious disputes.  Choose a professional editor which works for you.

Going further: you need to master basics skills in `vi` and `emacs`, as outlined in this [Survival Guide to vi and emacs](resources/vi_emacs_survival_kit.md).

<a name="terminal">
### 2. Install and use a Terminal
</a>

#### iTerm2
The native Terminal is tucked away in MacOs Utilities and rarely used by everyday users. But it's a major tool for a Data Scientist!

During the program, we will be using iTerm2. Install the stable release on https://www.iterm2.com/downloads.html.
- Tip: pin it in your Dashboard, you will be using this app a lot!
- Curious to know why we recommend iTerm2? Read this [apple.stackexchange conversation](http://apple.stackexchange.com/questions/25143/what-is-the-difference-between-iterm2-and-terminal).

**Linux note:** You can use the native Linux terminal.

#### Brew Install

Homebrew is a Mac package utility. To install a package, thype the following in the command line `$ brew install package-name` (NB: do no actually type the `$` sign, this just indicates a command line environment). To see which packages are installed: `$ brew list`.

Install the following package and research what it does on Google (you will be using in to check your assignment).

  ```
  $ brew install tree
  ```

**DO NOT INSTALL MACPORTS ON THE WORKSTATIONS.**

**Linux Note:** Brew is just for Mac, in Linux you will need to use

  ```
  $ sudo apt-get install <package>
  ```

#### Command line
[Assignment 2](assignments/assignment_2_command_line.md): Use commands such as `ls`, `cd directory`, `cd ..`, `mkdir new-dir`, `rm some-file`, `mv`, etc to complete the [assignment_2_command_line.md](assignments/assignment_2_command_line.md). Feel free to go through the [sample version](assignments/assignment_2_command_line_sample.md) to get to know basic commands and to use the [cheatsheet](resources/command_line_basics.md) at first.


<a name="anaconda">
### 3. Install Anaconda
</a>

[Assignment 3](assignments/assignment_3_anaconda.md): We use the `Anaconda Python 2.7` (not Python 3) distribution and will therefore use `conda` to install any additional packages. This assignments makes sure you will have Anaconda on your machine and will take you through installing packages.

Complete the [assignment_3_anaconda.md](assignments/assignment_3_anaconda.md).

<a name="developing">
### 4. Running a Python script from the Terminal
</a>

#### Developing code
Everyday here you'll be writing programs in Python. You have 2 options when
you're developing:

  1. Develop in a text editor [> your tool: Atom] and run the code with the Python
     interpreter [> your tool: iPython in iTerm2]
  2. Develop in an interactive 'repl' ('repl' stand for 'read-eval-print loop'), [> your tool: iPython in iTerm2]

[Assignment 4 - part 1](assignments/assignment_4_developing.md): For the most part, you will use option 1. Option 2 (developing in a repl) is best
when you are trying out small bits of code.

Complete [assignment_4_developing.md](assignments/assignment_4_developing.md) to try out both options.

#### Interactive Development Workflow

[Assignment 4 - part 2](assignments/assignment_4_interactivedeveloping.md): When coding, you should build your programs incrementally and efficiently. This means keeping the feedback loop tight when writing code.

Complete [assignment_4_interactivedeveloping.md](assignments/assignment_4_interactivedeveloping.md) to make sure you are familiar with:
- Adding print statements
- Importing modules and Autoreload
- Interactive Debugging.

<a name="git">
### 5. Version control with Git and GitHub
</a>

The key takehome message: <b>Always be committing</b>. Now let's see what that means and what tools we have for version control.
  * <b>git</b>: git is used for version control. It will be a critical part of your development workflow. Being able to rollback changes and create branches will enable you to be more confident in developing programs because you can change code and try new approaches without worrying about losing a currently working version. git is on your local machine.

  * <b>GitHub</b>:  To make it perfectly clear, git is independent of GitHub. Each copy of a git repository is independent of all the others (hence, *distributed* version control system, or dvcs). GitHub is just a place to put a copy of a repository; the benefit is that because GitHub is web-based, anybody can access that repository at anytime, which makes it an ideal place to host a master version of shared repositories. Many companies use GitHub in just that way.

[Assignment 5 - The Galvanize way ](assignments/assignment_5_gitversions.md): Here at Galvanize, we have our curriculum in git repositories hosted on GitHub. You'll be viewing, cloning, and forking those repositories quite a bit. Let's practice with [assignment_5_gitversions.md](assignments/assignment_5_gitversions.md).

  __DO NOT commit large files to a Github repo (anything larger than ~20mb).__  In case you have accidentally committed a large file (or dataset) use this [tutorial](http://blog.jessitron.com/2013/08/finding-and-removing-large-files-in-git.html) or this [command line tool](http://rtyley.github.io/bfg-repo-cleaner/) to clean up your repo

<a name="workflow">
### 6. Know the Galvanize Workflow
</a>

Having a structured and effective workflow is foundational to your success at Galvanize and as a data scientist in the wild.

#### A Note on Individual Style

While you are pairing here at Galvanize, please follow the tools and workflow as
they are presented here. Consider it the Galvanize Way.

When you're working solo, go ahead and do whatever you'd like. Note however that
it'll be easier to get help from the instructors if you're following the
Galvanize Way.

#### Complements on the Galvanize workflow

- Google Chrome: Our browser of choice here Galvanize. Use it.

#### Recap:
1. Know the tools. Use the tools.
  * iTerm2
  * Text Editor (Atom)
  * iPython
2. Use the keyboard. Don't use the mouse. Know your shortcuts.
3. Keep a tight feedback loop when writing code.
  * Write code in Atom
  * Import file into iPython
  * Write, run, repeat
4. Use git. Always be committing (ABC).

#### Keyboard shortcuts

[Assignment 6](assignments/assignment_6_avoiding_mouse.md): It's a good idea to start learning how to navigate and work without a mouse. This will come in very handy when you will be accessing remote machine and will not have the possibility to use a mouse to switch from one app to the next or from one window to the next.

The aim of [assignment_6_avoiding_mouse.md](assignments/assignment_6_avoiding_mouse.md) is to take you over some of the concepts you have been introduced to in this chapter. Try to do it without your mouse! A [cheatsheet](resources/Keyboard_Shortcuts.md) is available to help you with shortcuts.
