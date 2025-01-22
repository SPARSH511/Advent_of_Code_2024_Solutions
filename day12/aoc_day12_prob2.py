# Logic is store the edge grid coordinates and their respective change values from direction 
# Then try to add those direction values to the current chosen fence coordinate 
# until they are found again in the fences list
# then remove those 2 from the fences list and count it as a edge


from collections import deque
from itertools import count
import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
grid = open(infile).read().split("\n")
rows, cols = len(grid), len(grid[0])
visited = [[False] * cols for _ in range(rows)]

def bfs(x, y):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    letter = grid[x][y]
    queue = deque([(x, y)])
    fences = set()
    visited[x][y] = True
    area, fence_count = 0, 0

    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == letter:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
            else:
                fences.add((r, c, dr, dc))

    while fences:
        r, c, dr, dc = fences.pop()
        fence_count += 1
        for step in (1, -1):
            # count function generates an infinite loop from the 'step' number to beyond like if step = 1 then sequence = 1,2,3.. 
            # otherwise sequence = -1,-2,-3... for step = -1
            for i in count(step,step):
                neighbor_fence = (r + i * dc, c + i * dr, dr, dc)
                if neighbor_fence in fences:
                    fences.remove(neighbor_fence)
                else:
                    break

    return area, fence_count

def calculate_result():
    total = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, fence_score = bfs(i, j)
                total += area * fence_score
    return total

print("Answer to problem 2 :", calculate_result())