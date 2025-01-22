import os
from collections import defaultdict

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"
s = open(infile).read().strip().split("\n\n")

# # Sample test case
# s = ["""47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13""",

# """75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""]


mp = defaultdict(list)
for line in s[0].split("\n"):
    x = line.split("|")
    mp[int(x[0])].append(int(x[1]))

ans1,ans2 = 0,0
for line in s[1].split("\n"):
    x = list(map(int,line.split(",")))
    f = 0
    n = len(x)
    for i in range(n-1):
        try:
            if x[i+1] not in mp[x[i]]:
                f = 1
                break
        except:
            pass
    if not(f):
        ans1 += x[n//2]
    else:
        for i in range(n-1):
            for j in range(i+1,n):
                if x[j] not in mp[x[i]] and x[i] in mp[x[j]]:
                    x[i],x[j] = x[j],x[i]
        ans2 += x[n//2]

print("Answer to problem 1: ",ans1)
print("Answer to problem 2: ",ans2)
