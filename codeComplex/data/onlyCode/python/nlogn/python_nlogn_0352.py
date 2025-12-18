from collections import defaultdict, Counter
from bisect import bisect, bisect_left
from math import sqrt, gcd
 
def read(): return list(map(int, input().strip().split()))
 
ans_ = []

 
# for _ in range(int(input())):
t_p = [2**i for i in range(31)]
n = int(input()); 
arr = Counter(read())
d = defaultdict(int)
m = 1; ans_lis = [[list(arr.keys())[0], 1]]

for i in arr:
    for j in t_p:
        a, b, c = i, i+j, i+2*j
        s = arr[a] + arr[b] + arr[c]
        if s > m:
            m = s
            ans_lis = [[x, arr[x]] for x in [a, b, c]]


ans_.append(m)
t = ""
for i in ans_lis:t += (str(i[0])+" ")*i[1]
ans_.append(t)





 
 
# print(ans_)
for i in ans_:
    print(i)
 
 
"""
0 2 4 
3 5 7


0 8 16


"""