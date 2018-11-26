#!/usr/bin/python
# coding: utf-8
# Program that emulates Unix's "cat" command. Written in Python 2.7
# (C) Nov 2018, Ale Moliné

import sys

# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)

if len(sys.argv) < 2:
    print "kat: please specify a file name." # exits if no command-line arguments are given
    quit()

filecli = sys.argv[1] # file specified at the command-line.
print "So far, so good.",
print "File name specified is:", filecli

### Start file access

archivo = open(filecli,"r") # opens the file in read mode as archivo.

for linea in archivo:
    print linea, # the comma is so that newline character does not add a blank line

