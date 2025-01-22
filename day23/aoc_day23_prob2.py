import os
from collections import defaultdict

# Set up the graph
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = open(infile).read().strip().split("\n")
s = [i.split('-') for i in s]

g = defaultdict(set)
for i in s:
    g[i[0]].add(i[1])
    g[i[1]].add(i[0])

# Bron-Kerbosch Algorithm to find the largest clique
def bron_kerbosch(r, p, x):
    global largest_clique
    if not p and not x:
        # If R is a larger clique, update the largest clique
        if len(r) > len(largest_clique):
            largest_clique = r
        return
    
    for v in list(p):
        bron_kerbosch(r | {v}, p & g[v], x & g[v])  # Expand the clique
        p.remove(v)  # Remove v from P
        x.add(v)     # Add v to X (processed)

# Initialize the Bron-Kerbosch algorithm
largest_clique = set()
nodes = set(g.keys())
bron_kerbosch(set(), nodes, set())

# Sort the computers in the largest clique alphabetically and join with commas
password = ",".join(sorted(largest_clique))

print("Answer to Problem 2 :", password)
