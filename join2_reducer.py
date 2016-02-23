#!/usr/bin/env python
import sys

prev_word    = "  "                #initialize previous word  to blank string
line_cnt     = 0  #count input lines
abc_found    = False
totalCount  = 0

#read lines and split lines into key & value
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1

    #note: for simple debugging use print statements, ie:
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

#if a key has changed (and it's not the first input)
    if curr_word != prev_word:

        if line_cnt>1:
#then check if ABC had been found and print out key and running total,
            if abc_found:
                print('{0}\t{1}'.format(curr_word,totalCount))
            prev_word = curr_word
            abc_found = False
            totalCount = 0

#if value is ABC then set some variable to mark that ABC was found (like abc_found = True)
    if value_in == 'ABC':
        abc_found = True

#otherwise keep a running total of viewer counts
    elif value_in.isdigit():
        totalCount = totalCount + int(value_in)

#last line
if abc_found:
    print('{0}\t{1}'.format(curr_word,totalCount))
