import re
import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip()

p1 = 0
p2 = 0
enabled = True
for i in range(len(s)):
    if s[i:].startswith('do()'):
        enabled = True
    if s[i:].startswith("don't()"):
        enabled = False
    instr = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', s[i:])
    if instr is not None:
        x,y = int(instr.group(1)), int(instr.group(2))
        p1 += x*y
        if enabled:
            p2 += x*y
            
print("The sum of all multiplications : ", p1)
print("The sum of all multiplications with don't and do keywords : ",p2)