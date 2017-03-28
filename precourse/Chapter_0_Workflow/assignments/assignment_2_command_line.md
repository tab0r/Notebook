# Assignment: Working with Command Lines

## Objectives
You will be using commands to create, move and rename files and directories.

If you have never used a Terminal before, follow the guided steps in [assignment_2_command_line_sample.md](assignment_2_command_line_sample.md). This will show you the commands you need to type to create directory, move them, copy files and delete them.

If you are somewhat familiar with a Terminal, figure out the right command lines to achieve the action items described below. The command lines, in the order you typed them, should be placed in the YOUR ANSWER placeholder.

A [cheatsheet](../resources/command_line_basics.md) is available to help you.

_______________________________________

## Questions

Do not use finder, just stay in the Terminal

1. Make a `testing_directory` on your Desktop.
2. Inside this directory, make a `code` directory, a `data` directory, a `raw_data` directory and a `test` directory.
3. Enter the `testing_directory` and create a `readme.md` file and a `do_not_readme.md` file with Atom.
4. Create a `simple_script.py` in the `test` directory with Atom, add the following text: `print('Hello World!')`.
5. Place the `raw_data` directory inside the `data` directory.
6. Get the new path to the `raw_data` directory.
7. Move the `simple_script.py` inside the `code` directory.
8. Rename the python script `hello_world.py`.
9. Delete the `do_not_readme.md` file.

To check your work, you can run `$ tree` in the `testing_directory`. Your output should look like this.

```
├── code
│   └── hello_word.py
├── data
│   └── raw_data
├── readme.md
└── test
```
_______________________________________

## Answers
Please indicate the commands necessary to execute steps 1-9.

YOUR ANSWER:
MacBook:Desktop squalor$ mkdir testing_directory
MacBook:Desktop squalor$ cd testing_directory/
MacBook:testing_directory squalor$ mkdir code
MacBook:testing_directory squalor$ mkdir data
MacBook:testing_directory squalor$ mkdir raw_data
MacBook:testing_directory squalor$ mkdir test
MacBook:testing_directory squalor$ touch readme.md, do_not_readme.md
MacBook:testing_directory squalor$ touch test/simple_script.py
MacBook:testing_directory squalor$ atom test/simple_script.py
MacBook:testing_directory squalor$ mv raw_data/ data/
MacBook:testing_directory squalor$ mv test/simple_script.py code/
MacBook:testing_directory squalor$ mv code/simple_script.py code/hello_world.py
MacBook:testing_directory squalor$ rm do_not_readme.md
MacBook:testing_directory squalor$ tree
-bash: tree: command not found
MacBook:testing_directory squalor$ brew install tree
MacBook:testing_directory squalor$ tree
.
├── code
│   └── hello_world.py
├── data
│   └── raw_data
├── readme.md,
└── test

4 directories, 2 files
