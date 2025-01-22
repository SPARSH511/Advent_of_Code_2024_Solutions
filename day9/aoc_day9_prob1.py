import os

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

# Read the input
s = open(infile).read().strip()
n = len(s)

# Initialize variables
actual = []
flag = 1
id = 0
queue = []
indx = 0

# First pass: Build actual filesystem string and populate queue of insertion indexes
for i in range(n):
    if flag:
        actual.extend([str(id)] * int(s[i]))
        indx += int(s[i])
        id += 1
        flag = 0
    else:
        queue.extend(range(indx, indx + int(s[i])))
        indx += int(s[i])
        flag = 1

# Process the queue
while queue:
    insert_position = queue.pop(0)
    if insert_position < len(actual):
        # Safely pop and reinsert the element
        actual.insert(insert_position, actual.pop())

# Calculate checksum
checksum = sum(i * int(actual[i]) for i in range(len(actual)))


print("Answer to Problem 1 : ", checksum)
# print()
# print("The compacted file system string : ","".join(actual))
