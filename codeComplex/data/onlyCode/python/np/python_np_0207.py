from itertools import *
n,least,highest,x = map(int,input().split())
l = [*map(int,input().split())]
cnt = 0
for i in range(2,n + 1):
    combination = [*map(list,combinations(l,i))]
    for j in range(len(combination)):
        combination[j].sort()
        #print(combination[j])
        total = sum(combination[j])
        if(total >= least and total <= highest and combination[j][-1] - combination[j][0] >= x):
            cnt += 1
print(cnt)