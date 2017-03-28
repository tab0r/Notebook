## Objectives:

This short cheatsheet shows how to perform “survival” edits using `vi` and `emacs` (other editors include `nano` or `pico`). You will learn how to:
- Start/exit these editors
- Perform basic, if inefficient, edits using text-based (non-gui) Unix editors

Note: gui stands for Graphical User Interface

## Resources:

- [vim-adventures.com](http://www.vim-adventures.com) is the place to get started with `vi`.
- An [emacs survival card](https://www.gnu.org/software/emacs/refcards/pdf/survival.pdf)
- Some basic `vi` and `emacs` commands are well explained [here](http://www.cryst.bbk.ac.uk/CCSG/info/software/howto/vi.html).

## Text editor: vi

### Quick background

- `vi` is included in almost all UNIX distribution.
- “vi” is a truncation of the word “visual” and the text editor is dates back to 1976.
- `vi` works in different modes: NORMAL (the letters you type indicate
  commands to be executed e.g. saving a file, deleting a line, exiting the editor, etc.) and
  INSERT (the letters you type are inserted as text in the current file)

### Basic commands

*Step 1:* Starting `vi`
```
$ vi
```
or with a filename
```
$ vi filename
```

The screen is now available to enter text. Note, on the left hand side, a column of tildes (~). They are not part of the text. Also note the bottom line, which is used to show the entry of commands or some information on the file.

*Step 2:* Exiting `vi`
Type in the follow commands and press ENTER. If there are no changes
```
:q
```
To quit without saving the changes (forced quit)
```
:q!
```
To quit and save the changes
```
:qw
```
Note: All text you enter (and subsequent edits you make to it) exists
only in the buffer until you save the file to disk. "Saving" a file
means writing (i.e., transferring) the contents of the buffer to the disk.

*Step 3:* Adding text. By default, you enter `vi` in NORMAL mode, where
letters indicate commands to be executed. But, you can then switch to INSERT mode by typing
```
:i
```
You can then start typing your text. When you are done, press 'ESC' to return to NORMAL
mode and save.

*Step 4:* Editing a file. In the 'normal' mode, move up and down with the arrows (`vi` was designed for QWERTY without keys, so there are commands to move up/down and right/left, you can Google them if your arrows are misbehaving.). Once you reach the desired spot, type `i`, you will see '-- INSERT --' on the bottom line. You can start typing.

There are a lot of shortcuts and commands that can make your life much easier (single character editing, deleting, searching, copying, pasting...)

## Text editor: `emacs`

### Quick background

- Emacs was first appeared in the mid-1970s and is still actively developed!
- GNU Emacs is the most popular and most ported version of Emacs.
- We are barely even skimming the surface here: Emacs has over 2,000 built-in commands.

### Basic commands

*Step 1:* Starting `emacs`
```
$ emacs
```
or with a filename
```
$ emacs filename
```

*Step 2:* Exiting `emacs`.
- To exit `emacs`, press `ctrl + x` followed by `ctrl + c`.
- To save the file, press `ctrl + x` followed by `ctrl + s`.

Note that if you quit the file without saving the changes, `emacs` will ask you to decide what to do with the changes.

*Step 3:* Adding text.  Once the file is open (usually in GNU Emacs), you can start typing. A handy command, is the 'undo', which is obtained by pressing `ctrl + x` followed by `u`.

Please note the bottom line, which is used to show the entry of commands or some information on the file.
