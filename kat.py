#!/usr/bin/python
# coding: utf-8
# Programa que emula el comando "cat" de Unix. Escrito en Python 2.7
# (C) Nov 2018, Ale Moliné

import sys

print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)