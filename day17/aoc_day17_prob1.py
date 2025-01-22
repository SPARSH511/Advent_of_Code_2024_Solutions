# No concept of pointer variables exists in Python so used lists of one element instead of pointer 
# variables and it works

import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")

s.remove("")
a = [int(s[0].replace("Register A: ",""))]
b = [int(s[1].replace("Register B: ",""))]
c = [int(s[2].replace("Register C: ",""))]
p = list(map(int,s[3].replace("Program: ","").split(",")))

ip,n = 0,len(p)

combo = {0:[0],1:[1],2:[2],3:[3],4:a,5:b,6:c}
console_output = []

while ip < n-1:
    opcode, operand = p[ip],p[ip+1]
    if opcode == 0:
        a[0] = a[0]//(2**combo[operand][0])
    elif opcode == 1:
        b[0] = b[0]^operand
    elif opcode == 2:
        b[0] = combo[operand][0]%8
    elif opcode == 3 and a[0] != 0:
        ip = operand
        continue
    elif opcode == 4:
        b[0] = b[0]^c[0]
    elif opcode == 5:
        console_output.append(combo[operand][0]%8)
    elif opcode == 6:
        b[0] = a[0]//(2**combo[operand][0])
    else:
        c[0] = a[0]//(2**combo[operand][0])
    
    ip+=2

console_output = ",".join(map(str,console_output))

print("Answer to Problem 1 :",console_output)



        
