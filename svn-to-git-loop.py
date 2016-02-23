#!/usr/bin/python
# svn-to-git-loop.py
# Created Thu Feb 11 16:54:30 AKST 2016
# Copyright (C) 2016 by Raymond E. Marcil <marcilr@gmail.com>
#
# Script to loop over a list of svn+ssh:// subversion sources
# and ssh:// git repository targets to convert using svn-to-git.
#
# Only only works with htpc /data/svnroot repos at this point.
#
# Removes svn and gti directories created in current working
# directory.  I.e. Be sure to run this script in a temporary
# directory to alleviate directory name conflicts.
#
# Ported from bash to python since the bash while loop would
# not continue with external svn-to-git was called.
#
#
# Links
# =====
# Python Functions
# http://www.tutorialspoint.com/python/python_functions.htm
#

# ==============================================
# Configuration
# ==============================================

# Debugging
debug = "true"

# ==============================================
# Binaries
# ==============================================


# ==============================================
# Functions
# ==============================================

#
# debug()
# Output debugging text.
# INPUT: $1 - Text to output if DEBUG="
#
#def debug (str):

#    print "debug()"

#    if debug == "true":
#        print ("debug()", str);
#    else:
#        print "foo"

#    return;


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;


# Get command line arguments
#def get_cli_arguments():
#    "Get command line arguments."
#    return


# ==============================================
# Main
# ==============================================

printme("main")

print "svn-to-git-loop.py - convert hierarchical svn repo to git"


# Get command line arguments
#get_cli_arguments()
