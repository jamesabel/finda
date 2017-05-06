finda
=====

`finda` is a command line tool that searches folder(s) for the occurrence of string(s) in the path, file name or 
file contents.  Execute the program for help messages.

Builds
======

**Windows**

A single `finda.exe` is created.  This can be put anywhere you can execute it (e.g. in your `PATH`)

**Mac/Linux**

A Mac app (a '.app' folder) created in `dist/finda.app`, and a disk image of `finda.app` is in `installs/finda.dmg`.  
Move `finda.app` to a place you have your personal binary tools.  I tend to use a folder `~/b` .

Then you can put the line below in your `~/.bashrc` so you can just run `finda` on the command line:

    alias finda="~/b/finda.app/Contents/MacOS/finda"
