# Understand the relation between the next values to choose for a and correct values at a level
# Basically question was for DFS or BFS but the tricky part was to identify how to make the neighbors for 
# next round of search

# Replaced the operators here to their bitwise counter-parts for more speed

import os

# Reading input file
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")
p = list(map(int, s[4].replace("Program: ", "").split(",")))
n = len(p)

def run_program(val,onetime = False):
    a,b,c = [val],[0],[0]
    combo = {0:[0],1:[1],2:[2],3:[3],4:a,5:b,6:c}
    console_output = []
    ip = 0
    while ip < n-1:
        opcode, operand = p[ip],p[ip+1]
        if opcode == 0:
            a[0] = a[0]>>combo[operand][0]
        elif opcode == 1:
            b[0] = b[0]^operand
        elif opcode == 2:
            b[0] = combo[operand][0] & 7
        elif opcode == 3:
            if a == 0 or onetime:
                return console_output
            else:
                ip = operand
                continue
        elif opcode == 4:
            b[0] = b[0]^c[0]
        elif opcode == 5:
            console_output.append(combo[operand][0] & 7)
        elif opcode == 6:
            b[0] = a[0]>>combo[operand][0]
        else:
            c[0] = a[0]>>combo[operand][0]
        ip+=2
    return console_output

result = [float('inf')]
def dfs(values, program, a_value, level):
    val = values[-level]
    for i in range(0, 8):
        test = run_program(a_value+i,True)
        if test[0] == val:
            if level == len(values):
                result[0] = min(result[0],a_value+i)
            elif level < len(values):
                dfs(values, program, (a_value+i) << 3, level+1)

dfs(p, p.copy(), 0, 1)

print("Answer to Problem 2: ",result[0])

