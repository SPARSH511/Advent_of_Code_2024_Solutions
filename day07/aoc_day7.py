import os
from collections import deque

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split("\n")

n = len(s)

for i in range(n):
    s[i] = s[i].split(": ")
    res = int(s[i][0])
    lis = list(map(int,s[i][1].strip().split()))
    s[i] = (res,lis)

# for i in s:
#     print(*i)

# Function for problem 1
def bfs1(res,arr):
    q = deque([(0,0)])
    n = len(arr)
    while q:
        curr,indx = q.popleft()
        if indx == n:
            if curr == res:
                return True
            else:
                continue
        q.append((curr+arr[indx],indx+1))
        q.append((curr*arr[indx],indx+1))
    return False

# Function for problem 2
def bfs2(res,arr):
    q = deque([(0,0)])
    n = len(arr)
    while q:
        curr,indx = q.popleft()
        if indx == n:
            if curr == res:
                return True
            else:
                continue
        q.append((curr+arr[indx],indx+1))
        q.append((curr*arr[indx],indx+1))
        q.append((int(str(curr)+str(arr[indx])),indx+1))
    return False

# Answer calculation
sum1,sum2 = 0,0
for res,arr in s:
    if bfs1(res,arr):
        sum1 += res
    if bfs2(res,arr):
        sum2 += res

print("Answer to Problem 1:",sum1)
print("Answer to Problem 2:",sum2)