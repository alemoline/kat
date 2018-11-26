#!/usr/bin/python
# coding: utf-8
# Program that emulates Unix's "cat" command. Written in Python 2.7
# (C) Nov 2018, Ale Moliné

import sys

###  Process command-line parameters. 

if len(sys.argv) < 2:
    print "kat: please specify a file name." # exits if no command-line arguments are given.
    quit()

filecli = sys.argv[1] # file name specified at the command-line. It only takes first parameter into account.

### Start file access

try:
    archivo = open(filecli,"r") # opens the file in read mode as archivo.
except:
    print "kat: error when opening file", filecli  
    quit()
for linea in archivo:  # traditional loop to read a text file in Python, one line at a time
    print linea, # the comma is added so that newline character does not add a blank line

