import os
from collections import defaultdict, deque

# Set up the graph
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")
s = [i.split('-') for i in s]

g = defaultdict(list)
for i in s:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])

def check(path):
    if (
        path[0] in g[path[1]] and path[0] in g[path[2]] and
        path[1] in g[path[0]] and path[1] in g[path[2]] and
        path[2] in g[path[0]] and path[2] in g[path[1]] and
        tuple(sorted(path)) not in ans
    ):
        return True
    return False

# BFS Implementation
ans = set()

for vertex in g:
    queue = deque([(vertex, [vertex])])  # Queue holds (current_node, current_path)
    
    while queue:
        current, path = queue.popleft()
        
        # If we have a path of length 3, check for validity
        if len(path) == 3:
            if check(path):
                ans.add(tuple(sorted(path)))
            continue
        
        # Add neighbors to the queue
        for neighbor in g[current]:
            if neighbor not in path:  # Avoid revisiting nodes in the current path
                queue.append((neighbor, path + [neighbor]))

# Count the triplets where at least one node starts with 't'
count = 0
for triplet in ans:
    if triplet[0][0] == 't' or triplet[1][0] == 't' or triplet[2][0] == 't':
        count += 1

print("Answer to Problem 1:", count)



# DFS IMPLEMENTATION

# ans = set()
# def dfs(vertex,vis=set(),path=[],path_len=0):
#     if path_len == 3 and check(path):
#         ans.add(tuple(sorted(path)))
#         print(sorted(path))
#         return 
#     if vertex not in vis:
#         vis.add(vertex)        
#         path.append(vertex)
#         for neighbor in g[vertex]:
#             dfs(neighbor,vis.copy(),path,path_len+1)
#         path.pop()

# for vertex in g:
#     dfs(vertex)
