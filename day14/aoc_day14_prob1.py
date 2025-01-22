import os

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

s = open(infile).read().strip().split("\n")
s = [i.replace("p=","").replace("v=","").split() for i in s]
s = [[tuple(map(int,i.split(','))) for i in item] for item in s]

# For Sample Input
# m,n = 7,11 

m,n = 101,103
q1,q2,q3,q4 = 0,0,0,0
simulation_time = 100

for item in s:
    x,y = item[0]
    vx,vy = item[1]
    x = (x+simulation_time*vx)%m
    y = (y+simulation_time*vy)%n
    if -1 < x < m//2 and -1 < y < n//2:
        q1+=1
    elif -1 < x < m//2 and n//2 < y < n:
        q2+=1
    elif m//2 < x < m and -1 < y < n//2:
        q3+=1
    elif m//2 < x < m and n//2 < y < n:
        q4+=1

print("Answer to Problem 1 :",q1*q2*q3*q4)
    
    
    