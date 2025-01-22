# Apply the 75 or 25 steps to each of the values of the stone individually using memoization and
# just count the final no. of stones generated from each and take out the sum


import os
from functools import cache

# Input parsing
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

# Read the input
s = open(infile).read().strip().split()
s = list(map(int,s))

@cache
def count_stones(stone, blinks):
  if blinks == 0:
    return 1
  if stone == 0:
    return count_stones(1,blinks-1)
  x = str(stone); n = len(x)
  if n&1:
    return count_stones(stone * 2024, blinks-1)
  # Call for the parts of the original string and add their answers 
  return count_stones(int(x[:n//2]), blinks-1) + count_stones(int(x[n//2:]), blinks-1)  
        

print("Answer to Problem 2 : ", sum(map(lambda x: count_stones(x, 75), s)))