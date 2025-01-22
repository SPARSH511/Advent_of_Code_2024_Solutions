# Use Cramer's Rule

import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split("\n")
s = [i for i in s if i != '']

n = len(s)
commands = []
for i in range(0,n,3):
    ba,bb,pr = s[i],s[i+1],s[i+2]
    ba = tuple(ba.replace("Button A: ","").replace("X+","").replace("Y+","").strip().split(", "))
    bb = tuple(bb.replace("Button B: ","").replace("X+","").replace("Y+","").strip().split(", "))
    pr = tuple(pr.replace("Prize: ","").replace("X=","").replace("Y=","").strip().split(", "))
    commands.append((ba,bb,pr))

ans = 0
for command in commands:
    d11,d12 = int(command[0][0]),int(command[0][1])
    d21,d22 = int(command[1][0]),int(command[1][1])
    d31,d32 = int(command[2][0]),int(command[2][1])
    
    detA = d11*d22-d12*d21
    num_x = d31*d22-d21*d32
    num_y = d11*d32-d12*d31
    
    if num_y%detA == 0 and num_x%detA == 0:
        ans += (num_x//detA)*3+(num_y//detA)

print("Answer to Problem 1 :",ans)

ans = 0
for command in commands:
    d11,d12 = int(command[0][0]),int(command[0][1])
    d21,d22 = int(command[1][0]),int(command[1][1])
    d31,d32 = int(command[2][0])+10000000000000,int(command[2][1])+10000000000000
    
    detA = d11*d22-d12*d21
    num_x = d31*d22-d21*d32
    num_y = d11*d32-d12*d31
    
    if num_y%detA == 0 and num_x%detA == 0:
        ans += (num_x//detA)*3+(num_y//detA)

print("Answer to Problem 2 :",ans)


