#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item

    #print key_in
    if value_in.isdigit() | value_in == 'ABC':
#        show = key_in
#        channel = value_in
#        value_out = channel+" "+"0"

        print( '%s\t%s' % (key_in, value_in) )

    #else:   #key is only <word> so just pass it through
    #    show = key_in
    #    num = value_in
    #    print( '%s\t%s' % (key_in, value_in) )  #print a string tab and string
