import os
from collections import deque

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")

s = [tuple(map(int,i.split(','))) for i in s]

m,n = 71,71
st,en = (0,0),(70,70)
directions = ((0,1),(1,0),(0,-1),(-1,0))
obs = set()

for ox,oy in s:
    obs.add((ox,oy))
    exists = 0
    q = deque([(0,0,0)])
    vis = {st}
    while q:
        x,y,d = q.popleft()
        if (x,y) == en:
            exists = 1
            break
        for dx,dy in directions:
            nx,ny = dx+x,dy+y
            if -1 < nx < m and -1 < ny < n and (nx,ny) not in vis and (nx,ny) not in obs:
                q.append((nx,ny,d+1))
                vis.add((nx,ny))
    if not(exists):
        print("Answer to Problem 2 :",str(ox)+','+str(oy))
        exit()
