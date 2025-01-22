# Brute force is faster here

import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

# Read the input
s = open(infile).read().strip().split()

blink = 0
while blink < 25:
    i = 0
    while i < len(s):
        if s[i] == '0':
            s[i] = '1'
            i+=1
        elif len(s[i])%2 == 0:
            l,r = str(int(s[i][:len(s[i])//2])),str(int(s[i][len(s[i])//2:])) 
            s[i] = r
            s.insert(i,l)
            i+=2
        else:
            s[i] = str(int(s[i])*2024)
            i+=1
    blink+=1

print("Answer to the Problem 1 : ",len(s))





