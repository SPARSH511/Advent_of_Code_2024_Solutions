import os
from collections import deque

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().split("\n")
s = [list(i) for i in s]

m = len(s)
n = len(s[0])

start_pts = {}
for i in range(m):
    for j in range(n):
        if s[i][j] in start_pts:
            start_pts[s[i][j]].append((i,j))
        else:
            start_pts[s[i][j]] = [(i,j)]

# Here I had to accomodate the padding of 1 unit on each side of the visited 2-D array because the edges that 
# are with other elements could be repeatedly counted so to tackle this problem there is a visited section for 
# those points too rest logic is bfs to calculate area and edges of perimeter are the ones not shared with 
# same lettered neighbors or outside of the board (1 unit padding)

dir = [(0,-1),(0,1),(1,0),(-1,0)]
vis = [[0]*(n+2) for _ in range(m+2)]
cost = 0

for char in start_pts:
    for startx,starty in start_pts[char]:
        if not(vis[startx+1][starty+1]):
            perimeter, area = 0, 1
            queue = deque([(startx,starty)])
            vis[startx+1][starty+1] = 1
            while queue:
                x,y = queue.popleft()
                for dx,dy in dir:
                    if -1 < x+dx < m and -1 < y+dy < n and not(vis[x+dx+1][y+dy+1]) and s[x+dx][y+dy] == char:
                        area += 1
                        vis[x+dx+1][y+dy+1] = 1
                        queue.append((x+dx,y+dy))
                    else:
                        if ((x+dx+1 == m+1 or y+dy+1 == n+1 or y+dy+1 == 0 or x+dx+1 == 0) and not(vis[x+dx+1][y+dy+1])):
                            vis[x+dx+1][y+dy+1] = 1
                            perimeter += 1
                        if -1 < x+dx < m and -1 < y+dy < n and s[x+dx][y+dy] != char:
                            perimeter += 1
            # print(char, area, perimeter)
            cost += perimeter * area

print("Answer to Problem 1 :",cost)