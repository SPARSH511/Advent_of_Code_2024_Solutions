import os
from collections import defaultdict

# Read input
dir = os.path.dirname(os.path.abspath(__file__))
infile = os.path.join(dir, "input.txt")
s = open(infile).read().strip().split("\n\n")

# Parse towel patterns and designs
towel_patterns = s[0].split(", ")
designs = s[1].split("\n")

# Create a dictionary for towel patterns and their lengths
towel_lengths = {pattern: len(pattern) for pattern in towel_patterns}

# Function to count the number of ways to construct a design
def count_ways(design):
    dp = defaultdict(int)
    dp[""] = 1  # Base case: one way to construct an empty string

    for i in range(1, len(design) + 1):
        for pattern, plen in towel_lengths.items():
            if i >= plen and design[i - plen:i] == pattern:
                dp[design[:i]] += dp[design[:i - plen]]
    
    return dp[design]

# Compute the total number of ways for all designs
total_ways = sum(count_ways(design) for design in designs)

# Output the result
print("Answer to Problem 2:", total_ways)


# FOR BETTER UNDERSTANDING 

# # Recursive function to count the number of ways to construct a design
# def count_ways_recursive(design):
#     # Memoization using a dictionary
#     memo = {}

#     def helper(curr):
#         # If we've already computed the result for `curr`, return it
#         if curr in memo:
#             return memo[curr]

#         # Base case: if the current state is empty, there's one way (do nothing)
#         if curr == "":
#             return 1

#         # Initialize the number of ways to construct `curr`
#         ways = 0

#         # Try all towel patterns to see if they can end the current string
#         for pattern in towel_patterns:
#             if curr.endswith(pattern):
#                 # If `curr` ends with `pattern`, recursively compute the ways
#                 remaining = curr[: len(curr) - len(pattern)]
#                 ways += helper(remaining)

#         # Store the result in `memo` and return it
#         memo[curr] = ways
#         return ways

#     return helper(design)