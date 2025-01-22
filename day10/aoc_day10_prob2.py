# Same as previous one just remove the visited array from the BFS part 

import os
from collections import deque

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

# Read the input
s = open(infile).read().strip().split("\n")
dir = [(0,1),(0,-1),(1,0),(-1,0)]

m = len(s)
n = len(s[0])

trail_score = 0
for i in range(m):
    for j in range(n):
        if s[i][j] == '0':
            score = 0
            queue = deque([(i,j)])
            while queue:
                x,y = queue.popleft()
                if s[x][y] == '9':
                    score+=1
                for dx,dy in dir:
                    if -1 < x+dx < m and -1 < y+dy < n and s[x+dx][y+dy] == str(int(s[x][y])+1):
                        queue.append((x+dx,y+dy))
            trail_score += score

print("Answer to Problem 2 :",trail_score)
    
