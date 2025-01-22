import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

s = open(infile).read().strip().split("\n\n")

g = [list(row) for row in s[0].split("\n")]
moves = ""
for row in s[1].split("\n"):
    moves += row

m,n = len(g),len(g[0])

stx,sty = 0,0
for i in range(m):
    for j in range(n):
        if g[i][j] == '@':
            stx,sty = i,j
            break

for move in moves:
    if move == '>':
        if g[stx][sty+1] == '.':
            g[stx][sty+1] = '@'
            g[stx][sty] = '.'
            sty+=1
        elif g[stx][sty+1] == 'O':
            i = 1
            while g[stx][sty+i] == 'O':
                i+=1
            i-=1
            if g[stx][sty+i+1] == '#':
                continue
            else:
                while i:
                    g[stx][sty+i+1] = g[stx][sty+i]
                    i-=1
                g[stx][sty+1] = g[stx][sty]
                g[stx][sty] = '.'
                sty+=1   
    elif move == '<':
        if g[stx][sty-1] == '.':
            g[stx][sty-1] = '@'
            g[stx][sty] = '.'
            sty-=1
        elif g[stx][sty-1] == 'O':
            i = -1
            while g[stx][sty+i] == 'O':
                i-=1
            i+=1
            if g[stx][sty+i-1] == '#':
                continue
            else:
                while i:
                    g[stx][sty+i-1] = g[stx][sty+i]
                    i+=1
                g[stx][sty-1] = g[stx][sty]
                g[stx][sty] = '.'
                sty-=1 
    elif move == '^':
        if g[stx-1][sty] == '.':
            g[stx-1][sty] = '@'
            g[stx][sty] = '.'
            stx-=1
        elif g[stx-1][sty] == 'O':
            i = -1
            while g[stx+i][sty] == 'O':
                i-=1
            i+=1
            if g[stx+i-1][sty] == '#':
                continue
            else:
                while i:
                    g[stx+i-1][sty] = g[stx+i][sty]
                    i+=1
                g[stx-1][sty] = g[stx][sty]
                g[stx][sty] = '.'
                stx-=1
    else:
        if g[stx+1][sty] == '.':
            g[stx+1][sty] = '@'
            g[stx][sty] = '.'
            stx+=1
        elif g[stx+1][sty] == 'O':
            i = 1
            while g[stx+i][sty] == 'O':
                i+=1
            i-=1
            if g[stx+i+1][sty] == '#':
                continue
            else:
                while i:
                    g[stx+i+1][sty] = g[stx+i][sty]
                    i-=1
                g[stx+1][sty] = g[stx][sty]
                g[stx][sty] = '.'
                stx+=1

# Final Grid Status of Robot and Obstacles   
# for row in g:
#     print(*row)

ans = 0
for i in range(m):
    for j in range(n):
        if g[i][j] == 'O':
            ans += (i*100+j)

print("Answer to Problem 1:",ans)