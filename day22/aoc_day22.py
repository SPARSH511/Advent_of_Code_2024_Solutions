import os
from collections import defaultdict

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir + "\\input.txt"
s = list(map(int,open(infile).read().strip().split("\n")))

def secret(n):
    seq,ch = [],[]
    for k in range(2000):
        prev = n
        mid = n
        n <<= 6
        n ^= mid
        n &= 16777215
        mid = n
        n >>= 5
        n ^= mid
        n &= 16777215
        mid = n
        n <<= 11
        n ^= mid
        n &= 16777215
        seq.append(n%10)
        ch.append(prev%10-n%10)
    return (n,seq,ch)

ans1 = 0
key = defaultdict(int)

for num in s:
    res,seq,ch = secret(num)
    ans1 += res
    vis = set()
    for i in range(len(ch)-3):
        lookup = tuple(ch[i:i+4])
        if lookup not in vis:
            key[lookup] += seq[i+3]
            vis.add(lookup)

ans2 = 0
ans_seq = tuple()

for sequence in key:
    chk = key[sequence]
    if chk > ans2:
        ans2 = chk
        ans_seq = sequence 

print("Answer to Problem 1 :",ans1)
print("Answer to Problem 2 :",ans2)


