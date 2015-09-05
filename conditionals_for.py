#!/usr/bin/python3

# Works with an iterator
# open() method reads the content ofthe file that is being opened and the params
# are the path to that file and name of that file
# readlines() method just does exactly that: read lines!!
fh = open('lines.txt')
for line in fh.readlines():
    print(line)
