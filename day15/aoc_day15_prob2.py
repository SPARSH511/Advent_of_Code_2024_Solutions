# Use a queue to add new indexes to make moves on each time and if encountering a wall then don't do anything
# Brute force will not work here as it becomes too complicated to mimic for the new graph.

import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

s = open(infile).read().strip().split("\n\n")
moves = ""
for row in s[1].split("\n"):
    moves += row

g = s[0].replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
g = [list(i) for i in g.split("\n")]
m,n = len(g), len(g[0])

stx,sty = 0,0
for i in range(m):
    for j in range(n):
        if g[i][j] == "@":
            stx, sty = i, j
            break

directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
for move in moves:
    dx, dy = directions[move]
    queue = [(stx, sty)]
    f = 1
    for i, j in queue:
        nx, ny = i + dx, j + dy
        if (nx, ny) not in queue:
            if g[nx][ny] == "#":
                f = 0
                break
            elif g[nx][ny] == "[":
                queue.extend([(nx, ny), (nx, ny + 1)])
            if g[nx][ny] == "]":
                queue.extend([(nx, ny), (nx, ny - 1)])
    if f:
        for i, j in queue[::-1]:
            g[i + dx][j + dy], g[i][j] = g[i][j], g[i + dx][j + dy]
        stx, sty = stx + dx, sty + dy

ans = 0
for i in range(m):
    for j in range(n):
        if g[i][j] == '[':
            ans += i*100+j 

print("Answer to Problem 2:",ans)