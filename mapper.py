#!/usr/bin/env python3
"""mapper.py"""

import itertools
import sys
import re, string

words = dict()
lines = list()

for i in sys.stdin:
    
    lines.append(i)
    i = i.strip()
    i = i.split()

    if i == []: 
        continue
    for j in i:
        if j in words:
            words[j]+=1
        else:
            words[j]=1

for line in lines:
        
        line = line.strip()
        line = set(line.split())
        line = sorted(line)
        
        for i,j in itertools.combinations(line, 2):

            print(i+' '+j+":"+str(words[i])+' '+str(words[j]))