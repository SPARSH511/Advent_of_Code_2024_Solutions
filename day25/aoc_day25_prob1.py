import os
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"

s = open(infile).read().strip().split("\n\n")
s = [i.split("\n") for i in s] 

keys = [i for i in s if i[-1].count("#") == len(i[-1])]
locks = [i for i in s if i[0].count("#") == len(i[0])]

n1,n2 = len(keys), len(locks)
for key in keys[:n1]:
    keys.append(list(map(lambda x : x.count('#')-1,zip(*key)))) 
for lock in locks[:n2]:
    locks.append(list(map(lambda x : x.count('#')-1,zip(*lock)))) 
keys,locks = keys[n1:], locks[n2:]

count = 0
for i in range(n1):
    for j in range(n2):
        f = 0
        for k in range(len(keys[i])):
            if keys[i][k]+locks[j][k] > 5:
                f = 1
                break
        if not(f):
            count+=1

print("Answer to Problem 1 :", count)