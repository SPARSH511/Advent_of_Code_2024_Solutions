# Using Dijkstra's Algorithm for minimal cost (not suitable for finding all the shortest paths)

import os
from heapq import heappush, heappop

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input_sample.txt"

s = open(infile).read().strip().split("\n")
s = [list(row) for row in s]

m, n = len(s), len(s[0])

# locate start and end positions
sx, sy, ex, ey = 0, 0, 0, 0
for i in range(m):
    for j in range(n):
        if s[i][j] == 'S':
            sx, sy = i, j
        if s[i][j] == 'E':
            ex, ey = i, j

# directions: East, South, West, North (clock-wise)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
heap = [(0, sx, sy, 0)] 
visited = set()

while heap:
    cost, x, y, direction, path = heappop(heap)

    if (x, y) == (ex, ey):
        print("Answer to Problem 1 :", cost)
        break 
    
    # already visited, skip
    if (x, y, direction) in visited:
        continue
    visited.add((x, y, direction))
    
    # no rotate
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    if 0 <= nx < m and 0 <= ny < n and s[nx][ny] != '#':
        heappush(heap, (cost + 1, nx, ny, direction))
    
    # left rotate 
    new_direction = (direction - 1) % 4
    if (x, y, new_direction) not in visited:
        heappush(heap, (cost + 1000, x, y, new_direction))

    # right rotate
    new_direction = (direction + 1) % 4
    if (x, y, new_direction) not in visited:
        heappush(heap, (cost + 1000, x, y, new_direction))


