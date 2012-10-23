Unix Commands
============

For a college programming exercise.

Recreating some Unix Commands.

head.py
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Recreating the Head command in python 2.6
NOTE: Requires docopt.
A handy command line parser that takes Old fashioned Unix help strings as input
for a commandline parser
www.docopt.org

pip install docopt

head.py works mostly like head takes a default of 10 lines either from a list of files input
at the commandline or from stdin

-n allows a user to specify number of lines.
-c allows a user to specify a number of bytes.

This script will not take both -n and -c.
It will also not take -n or -c without an arguement value.

-v puts a header on the top of each file. 
-q has not been implemented yet.
+++++++++++++
TODO:
Error Handling for bad entries.
figureout and implement what -q is to do.
Comment the code properly.
