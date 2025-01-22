import os
from collections import defaultdict

# Input handling
a1,a2 = [],[]
dir = os.path.dirname(os.path.abspath(__file__))
with open(dir+"\\input.txt", "r") as file:
    for line in file:
        x = line.split()
        a1.append(x[0])
        a2.append(x[1])

# Problem 1
a1.sort()
a2.sort()
sum = 0
for i in range(len(a1)):
    sum += abs(int(a1[i])-int(a2[i]))
print("Distance:",sum)

# Problem 2
similarity = 0
mp = defaultdict(int)
for i in a2:
    mp[i] += 1
for i in a1:
    if i in mp:
        similarity += int(i)*mp[i]
print("Similarity:",similarity)