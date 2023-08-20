#!/usr/bin/env python3
"""reducer.py"""

import sys

count = dict() # COUNT(A, B)
words = dict() # COUNT(A)

for line in sys.stdin:
    line = line.strip()
    line = line.split(':')

    if line[0] in count: count[line[0]] += 1
    else: count[line[0]] = 1

    a, b = line[0].split()
    ac, bc = list(map(int,line[1].split()))

    if a not in words:
        words[a] = ac
    if b not in words: 
        words[b] = bc

cprob = dict() # conditional probability

for i in count:
    a, b = i.split()
    
    # P(A|B) = COUNT(A,B)/COUNT(B)
    
    if a+'|'+b not in cprob or b+'|'+a not in cprob:
        cprob[a+'|'+b] = round(count[i]/words[b],4)
        cprob[b+'|'+a] = round(count[i]/words[a],4)

for k,v in cprob.items():
    print(k,v)