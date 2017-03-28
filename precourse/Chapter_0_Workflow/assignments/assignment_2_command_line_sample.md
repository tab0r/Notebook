# Assignment: Working with Command Lines

## Objectives
Learn more about basic command lines to answer [assignment_2_command_line.md](assignment_2_command_line.md).

## What?

A Terminal is an application, hidden away in MacOs in the Utilities folder. When you open
the application, you are opening a Unix command-line environment, known as a shell. What you
are seeing is Apple's implementation, a type of shell called Bash.

Using the Terminal is straightforward, you simply type a command on the command line
and enter Return to execute it.

## How?
Let us see how a command line works.

*Step 1:* Without using the Terminal, create a `sample_file.rtf` with Text Edit (write whatever you want in it) and save it in a `sample_directory` directory on your Desktop.

*Step 2:* Open the iTerm2 application.

From now on, all our actions will be taken as instructions from the command line.

*Step 3:* See what files and directory are in the root directory you are currently occupying:
(do not type the '$ ' sign, that is just an indication that the following code is a command)
```
$ ls
```

*Step 4:* Let's enter the Desktop and see what files and directories are there.
```
$ cd Desktop
$ ls
```

*Step 5:* You should see the `sample_directory` directory created in *Step 1*. Let us enter in it.
Try using tap completion.
```
$ cd sample_directory
```

*Step 6:* Let us check our path.
```
$ pwd
```
(`pwd` stands for present working directory)

*Step 7:* One step back, 2 forward.
- Let us go back to the root directory, and enter the sample_directory directory directly. We then want to check its content.
  ```
  $ cd
  $ cd Desktop/sample_directory
  $ ls
  ```

*Step 8:* Let's make a new directory, and call it `inside_directory`.
```
$ mkdir inside_directory
```
Don't hesitate to go check by hand (in Finder window) that you successfully created inside_directory.

*Step 9:* Let's move the text file to that inside_directory.
```
mv Sample_File.rtf inside_directory/Sample_File.rtf
```
You can check that the text file is now in the inside_directory

*Step 10:* Let's rename the text file to Hi_There.rtf. First enter the inside_directory, then use the `mv` command.
```
$ cd inside_directory
$ mv Sample_File.rtf Hi_There.rtf
```
Make sure you now a Hi_There file.

*Step 11:* Let's delete the file Hi_There.rtf.
```
$ rm -i Hi_There.rtf
```
The '-i' allows to have a confirmation request before the file is delete. Type 'y' to proceed.

*Step 12:* Create a file with Atom.
```
$ atom my_new_file.csv
```
The Atom text editor will open and you can make your file. Here's what I wrote:
```
heading1, heading2, heading3
1, 2, 3
```
You can check that the file was actually created (by hand in the Finder, or with `ls` command)

*Step 13:* Now let's remove everything we have created so far. You cannot use the `rf`command on its own to erase a directory. Go back to the Desktop and type the following command:
```
$ cd ../..
$ rm -rf -i sample_directory
```

Look at your desktop, we have just erased any sign of the `sample_directory`, and of the files and directories it contained... but now you know a few useful command lines!

There are naturally a lot of other commands, that you can look up online, such as copying a file (`cp`) or looking at the beginning of a file (`head some-file`). You are no sure what a command does, ask for documentation:
```
$ man some-cmd
```
To exit the documentation, type 'q'
