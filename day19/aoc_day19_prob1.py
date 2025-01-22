import os
from collections import deque

# Read input
dir = os.path.dirname(os.path.abspath(__file__))
infile = os.path.join(dir, "input.txt")
s = open(infile).read().strip().split("\n\n")

# Parse towel patterns and designs
towel_patterns = s[0].split(", ")
designs = s[1].split("\n")

# Create a dictionary for towel patterns and their lengths
towel_lengths = {pattern: len(pattern) for pattern in towel_patterns}

# Function to check if a design can be constructed
def can_construct(design):
    maxlen = len(design)
    queue = deque([("", 0)])
    visited = set()

    while queue:
        curr, length = queue.popleft()
        if curr == design:
            return True
        if curr in visited or length > maxlen:
            continue
        visited.add(curr)
        for pattern, plen in towel_lengths.items():
            new_design = curr + pattern
            if design.startswith(new_design):
                queue.append((new_design, length + plen))
                
    return False

# Count the number of possible designs
possible_count = sum(can_construct(design) for design in designs)

# Output the result
print("Answer to Problem 1:", possible_count)
