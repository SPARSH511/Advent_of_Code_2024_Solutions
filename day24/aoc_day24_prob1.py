import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n\n")
s[1] = [i.split(" -> ") for i in s[1].split("\n")]

operands = dict([(i.split(": ")[0],int(i.split(": ")[1])) for i in s[0].split("\n")])
ops = [i[0].split()+[i[1]] for i in s[1]]

# Part 1

def solver():
    no_of_ops,completed_ops,indx = len(ops),0,0
    completed = [0]*no_of_ops

    while completed_ops < no_of_ops:
        if completed[indx]: 
            indx = (indx+1) % no_of_ops
            continue
        op1,sign,op2,res = ops[indx]
        if op1 in operands and op2 in operands:
            if res not in operands: 
                operands[res] = -1 # Dummy Value (gonna fill it afterwards)
            if sign == 'AND':
                operands[res] = operands[op1] & operands[op2]
            elif sign == 'XOR':
                operands[res] = operands[op1] ^ operands[op2]
            elif sign == 'OR':
                operands[res] = operands[op1] | operands[op2]
            else:
                print("Invalid Sign")
                return 
            completed_ops += 1
            completed[indx] = 1
        indx = (indx+1) % no_of_ops

    # Getting the bits of the 'z' - starting operands
    mp = []
    for operand in operands:
        if operand[0] == 'z':
            mp.append((operand,operands[operand]))
    mp.sort(reverse=True)

    # Forming the answer after arranging the bits of the 'z' - starting operands
    ans = ''
    for _,bit in mp:
        ans += str(bit)
    return int(ans,2)
    
print("Answer to Problem 1:",solver())

        

