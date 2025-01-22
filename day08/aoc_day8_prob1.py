import os
from collections import defaultdict

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"

s = open(infile).read().strip().split("\n")
s = [list(row) for row in s]

m, n = len(s), len(s[0])

# Map to store positions of antennas by frequency
mp = defaultdict(list)
for i in range(m):
    for j in range(n):
        if s[i][j] != '.':
            mp[s[i][j]].append((i, j))

# Set to track unique antinode locations
antinodes = set()

# Process each frequency
for pt in mp:
    pts_pos = mp[pt]
    num_points = len(pts_pos)
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            x1, y1 = pts_pos[i]
            x2, y2 = pts_pos[j]
            # Calculate potential antinode positions
            an1x, an1y = 2 * x1 - x2, 2 * y1 - y2
            an2x, an2y = 2 * x2 - x1, 2 * y2 - y1
            # Check if positions are within bounds and mark them
            if 0 <= an1x < m and 0 <= an1y < n:
                antinodes.add((an1x, an1y))
            if 0 <= an2x < m and 0 <= an2y < n:
                antinodes.add((an2x, an2y))

# Output the result
print("Answer for Problem 1:", len(antinodes))

# Optional: Print the grid with antinodes marked
for i in range(m):
    for j in range(n):
        if (i, j) in antinodes and s[i][j] == '.':
            s[i][j] = '#'

print("\nGrid with antinodes marked for Problem 1:\n")
for row in s:
    print("".join(row))
