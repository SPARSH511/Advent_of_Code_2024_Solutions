import os

def eight_dir_search(s, m, n, x, y):
    cnt = 0
    # Vertical upward
    if x - 3 >= 0 and ''.join([s[x - i][y] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Vertical downward
    if x + 3 < m and ''.join([s[x + i][y] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Horizontal left
    if y - 3 >= 0 and ''.join([s[x][y - i] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Horizontal right
    if y + 3 < n and ''.join([s[x][y + i] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Diagonal: top-left to bottom-right
    if x - 3 >= 0 and y - 3 >= 0 and ''.join([s[x - i][y - i] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Diagonal: bottom-left to top-right
    if x - 3 >= 0 and y + 3 < n and ''.join([s[x - i][y + i] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Diagonal: top-right to bottom-left
    if x + 3 < m and y - 3 >= 0 and ''.join([s[x + i][y - i] for i in range(4)]) == 'XMAS':
        cnt += 1
    # Diagonal: bottom-right to top-left
    if x + 3 < m and y + 3 < n and ''.join([s[x + i][y + i] for i in range(4)]) == 'XMAS':
        cnt += 1

    return cnt
    
def masx_search(s, m, n, x, y):
  if x-1 >= 0 and x+1 < m and y-1 >= 0 and y+1 < n:
    if s[x-1][y-1] == 'M' and s[x+1][y+1] == 'S' and s[x-1][y+1] == 'M' and s[x+1][y-1] == 'S':
      return 1
    if s[x-1][y-1] == 'S' and s[x+1][y+1] == 'M' and s[x-1][y+1] == 'S' and s[x+1][y-1] == 'M':
      return 1
    if s[x-1][y-1] == 'S' and s[x+1][y+1] == 'M' and s[x-1][y+1] == 'M' and s[x+1][y-1] == 'S':
      return 1
    if s[x-1][y-1] == 'M' and s[x+1][y+1] == 'S' and s[x-1][y+1] == 'S' and s[x+1][y-1] == 'M':
      return 1
  return 0
    
# Input grid
dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split("\n")

# Process the input grid
lines = [list(row) for row in s]
m = len(lines)
n = len(lines[0])

# Problem 1 & 2
cnt1,cnt2 = 0,0
for i in range(m):
    for j in range(n):
        if lines[i][j] == 'A':
          cnt2 += masx_search(lines, m, n, i, j) 
        if lines[i][j] == 'X':
          cnt1 += eight_dir_search(lines, m, n, i, j)
          
print("Problem 1 XMAS occurences : ",cnt1)
print("Problem 2 XMAS occurences : ",cnt2)