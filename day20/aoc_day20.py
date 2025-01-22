# Store the time-stamps as you go through the grid while exploring using BFS and then 
# apply the conditions in the questions (1st part difference in time >= 100+2 (+2 time for cheat steps) 
# and 2nd part manhattan distance <= 20 to make sure all the steps taken are within the limit of reach 
# and time also >= 100)

import os
from collections import deque

# Read input
dir = os.path.dirname(os.path.abspath(__file__))
infile = os.path.join(dir, "input.txt")
s = open(infile).read().strip().split("\n")

# Functions
def part1(grid):
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 'S':
                S = (row, col)
            elif grid[row][col] == 'E':
                E = (row, col)

    queue = deque([(*S, 0, dict())])
    while queue:
        x, y, time, visited = queue.popleft()
        visited[(x, y)] = time

        if (x, y) == E:
            break

        for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (i in range(m) and
                j in range(n) and
                (i, j) not in visited and
                grid[i][j] != '#'
            ):
                queue.append((i, j, time + 1, visited.copy()))

    cheats = 0
    for (x, y), t1 in visited.items():
        for i, j in [(x+2, y), (x-2, y), (x, y-2), (x, y+2)]:
            if visited.get((i, j), 0) - t1 >= 102:
                cheats += 1
                
    return cheats   

def part2(grid):
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 'S':
                S = (row, col)
            elif grid[row][col] == 'E':
                E = (row, col)

    queue = deque([(*S, 0, dict())])
    while queue:
        x, y, time, visited = queue.popleft()
        visited[(x, y)] = time

        if (x, y) == E:
            break

        for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (i in range(m) and
                j in range(n) and
                (i, j) not in visited and
                grid[i][j] != '#'
            ):
                queue.append((i, j, time + 1, visited.copy()))

    cheats = 0
    threshold = 100
    path = sorted(visited, key=visited.get)
    for t2 in range(threshold, len(path)):
        for t1 in range(t2 - threshold):
            x1, y1 = path[t1]
            x2, y2 = path[t2]
            distance = abs(x1-x2) + abs(y1-y2)

            # difference in time stamps but also accounting for the fact that extra time 
            # taken for reaching from 1st point to the other directly via cheat
            if distance <= 20 and t2 - (t1 + distance) >= threshold: 
                cheats += 1
     
    return cheats

print("Answer to Problem 1 :",part1(s))
print("Answer to Problem 2 :",part2(s))
                    