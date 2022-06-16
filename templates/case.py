#!/usr/bin/python3
# this work only for python > 3.10 !!!!
import sys
error = sys.argv[1]
match (error):
    case '400':
       return "Bad request";
    case '404':
       return "Not found";
    case '418':
       return "I'm a teapot";
    # If an exact match is not confirmed, this last case will be used if provid>
    case other:
       return "Something's wrong with the internet";
