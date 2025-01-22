# Keep this pattern in mind if a problem requires to use Dijkstra for shortest path and asks for all 
# shortest paths possible (basically normal BFS fails or is not optimal) then apply Bellman-Ford algorithm 
# to keep track of best costs for all states stored in the visited set and simulataneously keep track of paths
# like you normally would using extend command in lists in Python or storing all paths as 
# vector of vectors in C++


import os
from collections import deque, defaultdict

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"

s = open(infile).read().strip().split("\n")
s = [list(row) for row in s]

m, n = len(s), len(s[0])

sx, sy, ex, ey = 0, 0, 0, 0
for i in range(m):
    for j in range(n):
        if s[i][j] == 'S':
            sx, sy = i, j
        if s[i][j] == 'E':
            ex, ey = i, j

# directions: East, South, West, North (clock-wise)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = deque([(sx, sy, 0, 0, [(sx, sy)])])  # (x, y, direction, cost, path)
best_cost = defaultdict(lambda: float('inf'))
best_cost[(sx, sy, 0)] = 0

min_cost = float('inf')
all_min_paths = []  # list to store all paths with minimal cost

while queue:
    cx, cy, d, cost, path = queue.popleft()

    # reached the endpoint
    if (cx, cy) == (ex, ey):
        if cost < min_cost:
            min_cost = cost
            all_min_paths = [path]  # reset with a new minimum cost path
        elif cost == min_cost:
            all_min_paths.append(path)  # add path with the same minimum cost
        continue

    # try all moves (no rotate, left rotate, right rotate)
    for move, delta in [("no_rotate", 0), ("left", -1), ("right", 1)]:
        new_dir = (d + delta) % 4
        dx, dy = directions[new_dir]
        nx, ny = cx + dx, cy + dy
        move_cost = 1 if move == "no_rotate" else 1001
        new_cost = cost + move_cost

        # check bounds and walls
        if 0 <= nx < m and 0 <= ny < n and s[nx][ny] != '#':
            # update best cost and track paths (like Bellman Ford's Algo)
            if new_cost <= best_cost[(nx, ny, new_dir)]:
                best_cost[(nx, ny, new_dir)] = new_cost
                queue.append((nx, ny, new_dir, new_cost, path + [(nx, ny)]))

print("Answer to Problem 1:", min_cost)

ans_prob2 = set()
for path in all_min_paths:
    for pt in path:
        ans_prob2.add(pt)

print("Answer to Problem 2:",len(ans_prob2))



