# Takes a while to run (around 5-6 minutes)

import os
from collections import defaultdict

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

# Read the input
s = open(infile).read().strip()
n = len(s)

# Initialize variables
actual, flag, id, indx = [],1,0,0

# Build actual filesystem string
for i in range(n):
    if flag:
        actual.extend([str(id)] * int(s[i]))
        indx += int(s[i])
        id += 1
        flag = 0
    else:
        actual.extend(['.']*int(s[i]))
        indx += int(s[i])
        flag = 1

def compact_files(filesystem):
    n = len(filesystem)

    # Map file IDs to their positions
    file_positions = defaultdict(list)
    for i, block in enumerate(filesystem):
        if block != '.':
            file_positions[int(block)].append(i)

    # Process files in decreasing order of file IDs
    for file_id in sorted(file_positions.keys(), reverse=True):
        positions = file_positions[file_id]
        file_size = len(positions)
        current_start = positions[0]

        # Find leftmost free span before the current file's position
        target_start = -1
        for start in range(current_start - file_size + 1):
            if start < 0:
                continue  # Ignore out-of-bound starts
            if all(filesystem[j] == '.' for j in range(start, start + file_size)):
                target_start = start
                break

        # If no suitable space, skip moving this file
        if target_start == -1:
            continue

        # Move the file to the free space
        for pos in positions:
            filesystem[pos] = '.'  # Clear old positions
        for j in range(target_start, target_start + file_size):
            filesystem[j] = str(file_id)

    # Calculate the checksum
    checksum = sum(i * int(filesystem[i]) for i in range(n) if filesystem[i] != '.')
    return checksum, ''.join(filesystem)

# Input
checksum, compacted_filesystem = compact_files(actual)

print("Answer to Problem 2:", checksum)
# print()
# print("The compacted file system string : ",compacted_filesystem)