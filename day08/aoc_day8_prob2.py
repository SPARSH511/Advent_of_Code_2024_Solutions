import os
from collections import defaultdict

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")

m, n = len(s), len(s[0])

# Parse the s and group antennas by frequency
antennas = defaultdict(list)
for i in range(m):
    for j in range(n):
        if s[i][j] != '.':
            antennas[s[i][j]].append((i, j))

# Initialize a set to store all unique antinode positions
antinodes = set()

# Function to check collinearity
def are_collinear(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x1) == (x2 - x1) * (y3 - y1)

# Process each frequency group
for freq, positions in antennas.items():
    num_positions = len(positions)
    if num_positions < 2:
        continue  # No antinodes if fewer than 2 antennas of this frequency

    # Add each antenna itself as an antinode
    for pos in positions:
        antinodes.add(pos)

    # Check pairs of antennas
    for i in range(num_positions):
        for j in range(i + 1, num_positions):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            # Generate all collinear points with the pair (x1, y1) and (x2, y2)
            for x in range(m):
                for y in range(n):
                    if (x, y) == (x1, y1) or (x, y) == (x2, y2):
                        continue
                    if are_collinear(x1, y1, x2, y2, x, y):
                        antinodes.add((x, y))

# Output 
print("Answer for Problem 2 :", len(antinodes))