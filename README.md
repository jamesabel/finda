finda
=====

`finda` is a command line tool that searches folder(s) for the occurrence of string(s) in the path, file name or 
file contents.  It's like the Linux/Unix `find` command, but easier to use for many use cases.

Execute the program for help messages.

Downloads
=========
Prebuilt executables:

Windows: [finda.exe](https://s3.amazonaws.com/abel.co/finda/finda.exe)

Mac/OSX: [finda.dmg](https://s3.amazonaws.com/abel.co/finda/finda.dmg)

Builds
======

**Windows**

A single, stand-alone file executable file `finda.exe` is created in `dist\finda.exe`.

**Mac/Linux**

A Mac app (a '.app' folder) created in `dist/finda.app`, and a disk image of `finda.app` is in `installs/finda.dmg`.  
Move `finda.app` to a place you have your personal binary tools.  I tend to use a folder `~/b` .

Then you can put the line below in your `~/.bashrc` so you can just run `finda` on the command line:

    alias finda="~/b/finda.app/Contents/MacOS/finda"

Reference
=========
Author: James Abel ([abel.co](http://www.abel.co))
