import os
from collections import deque

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")

s = set([tuple(map(int,i.split(','))) for i in s][:1024])
m,n = 71,71

st,en = (0,0),(70,70)
q = deque([(0,0,0)])
vis = {st}
directions = ((0,1),(1,0),(0,-1),(-1,0))

while q:
    x,y,d = q.popleft()
    if (x,y) == en:
        print("Answer to Problem 1 :",d)
        exit()
    for dx,dy in directions:
        nx,ny = dx+x,dy+y
        if -1 < nx < m and -1 < ny < n and (nx,ny) not in vis and (nx,ny) not in s:
            q.append((nx,ny,d+1))
            vis.add((nx,ny))
             

