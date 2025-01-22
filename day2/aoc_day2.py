import os

# Input handling
lines = []
dir = os.path.dirname(os.path.abspath(__file__))
with open(dir+"\\input.txt", "r") as file:
    for line in file:
        x = list(map(lambda y: int(y), line.split()))
        lines.append(x)

# Sample Test Case : 
# lines = [[7, 6, 4, 2, 1],
# [1, 2, 7, 8, 9],
# [9, 7, 6, 2, 1],
# [1, 3, 2, 4, 5],
# [8, 6, 4, 4, 1],
# [1, 3, 6, 7, 9]]

# Problem 1
safe = 0
for l in lines:
    f1,f2,n = 1,1,len(l)
    for i in range(1,n):
        if l[i] >= l[i-1] or abs(l[i]-l[i-1]) > 3:
            f1 = 0
            break
    for i in range(1,n):
        if l[i] <= l[i-1] or abs(l[i]-l[i-1]) > 3:
            f2 = 0
            break
    if f1 or f2:
        safe+=1

print("Safe Reports :",safe)


# Problem 2
safe = 0
for l in lines:
    full_len = len(l)
    for indx in range(full_len):
        val = l.pop(indx)
        f1,f2,n = 1,1,full_len-1
        for i in range(1,n):
            if l[i] >= l[i-1] or abs(l[i]-l[i-1]) > 3:
                f1 = 0
                break
        for i in range(1,n):
            if l[i] <= l[i-1] or abs(l[i]-l[i-1]) > 3:
                f2 = 0
                break
        if f1 or f2:
            safe+=1
            break
        l.insert(indx,val)

print("Safe Reports after removal of one level from each is allowed :",safe)
    
