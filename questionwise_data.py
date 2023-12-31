# -*- coding: utf-8 -*-
"""3a_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xVVWYnmTls7e3vKRnsXY8gP0kKrU8gOr
"""

from google.colab import drive
drive.mount('/content/drive')

#!/usr/bin/env python3

import itertools
import re, string

"""Data Cleaning:
1. Remove To/From/Subject/Cc
2. Remove special characters (& replace with ' ')
3. Remove numerical characters (& replace with ' ')
4. Convert everything to lowercase
"""

out = open("3a.txt","w")
out = open("3a.txt","a")

# CREATING INPUT FOR 3A MAPPER

with open("emails.txt","r") as fp:
    for i in fp:
        rem = [" -----Original","To:","When:","Where:","Subject:",
               "Sent:","From:","Cc:","cc:","Bcc:",'----',"Tel:",'http']
        
        if i.startswith(tuple(rem)): 
            continue
        if i == '\n':
            continue
            
        i = i.strip()
        
        chars = re.escape(string.punctuation)+'\t'
        
        i = re.sub(r'['+chars+']+', ' ',i)
        
        i = re.sub(r'\d+', ' ', i)
        
        i = i.lower()
        
        out.write(i+'\n')
#         print(i)

# CREATING ITEM COUNT DICTIONARY

words = dict()

with open("3a_line.txt",'r') as fp:
    for i in fp:
        
        i = i.strip()
        i = i.split()

        if i == []: 
            continue
        for j in i:
            if j in words:
                words[j]+=1
            else:
                words[j]=1

# Emit (A, B) : Count(A) Count(B)

file = open("map_out.txt","w")
file = open("map_out.txt","a")

with open('3a_line.txt') as fp:
    
    for line in fp:
        
        line = line.strip()
        line = set(line.split())
        line = sorted(line)
        
        for i,j in itertools.combinations(line, 2):
            file.write(str(i)+' '+str(j)+":"+str(words[i])+' '+str(words[j])+'\n')     
#             print(i+' '+j+":"+str(words[i])+' '+str(words[j])+'\n')



# REDUCER

# FIND 2-ITEMSET COUNT 

count = dict() # COUNT(A, B)
words = dict() # COUNT(A)

with open("map_out.txt","r") as fp:
    for line in fp:
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

